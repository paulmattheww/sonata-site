#!/usr/bin/env python3
"""Refresh website assets from approved listing-v4 artwork and actual app footage.
Usage: python3 tools/refresh_release_preview.py SONATA_OUTPUT_RELEASES
Does not generate or upload App Store screenshots.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess, sys, shutil
ROOT=Path(__file__).resolve().parents[1]
RELEASES=Path(sys.argv[1])
SOURCE=RELEASES/'sonata-listing-v4'
VIDEO=RELEASES/'sonata-composer-49/raw-videos'
OUT=ROOT/'assets/composer-preview'
PAPER='#FFF4DE'; INK='#14120F'; COPPER='#9C4928'
SERIF='/System/Library/Fonts/Supplemental/Georgia.ttf'; SANS='/System/Library/Fonts/HelveticaNeue.ttc'
def font(size,serif=False): return ImageFont.truetype(SERIF if serif else SANS,round(size))
def text(im,xy,t,size,color=INK,serif=False): ImageDraw.Draw(im).text(xy,t,font=font(size,serif),fill=color,anchor='lt')
for name,dest,bounds in [('release49-ipad-10-classics-sheet.png','classics-highlights.png',(1600,1200)),('release49-iphone-12-difficult-fullscreen.png','fullscreen-highlights.png',(1600,1200)),('daily-scales.png','practice-sheet.png',(1000,1500))]:
    im=Image.open(SOURCE/'sources'/name).convert('RGB'); im.thumbnail(bounds,Image.Resampling.LANCZOS); im.save(OUT/dest,optimize=True)
shutil.copyfile(RELEASES/'sonata-composer-50/pdf/daily-scales.pdf',OUT/'daily-scales.pdf')
for name,bounds in [('header',(1920,1080)),('search-results',(1600,1200))]:
    im=Image.open(SOURCE/f'artwork/promotional/{name}.png').convert('RGB'); im.thumbnail(bounds,Image.Resampling.LANCZOS); im.save(OUT/f'{name}.jpg',quality=92)
share=Image.new('RGB',(1200,630),INK)
tile=ImageOps.contain(Image.open(SOURCE/'artwork/promotional/header.png'),(1200,570),Image.Resampling.LANCZOS)
share.paste(tile,(0,30)); ImageDraw.Draw(share).text((45,590),'COMING IN SONATA 1.1',font=font(19),fill=PAPER); share.save(OUT/'share.jpg',quality=92)
clips=[]
for n,(key,lines,sub) in enumerate([
 ('highlights',['Follow','the music.'],['Highlighted notes.','Note names to guide you.']),
 ('arpeggios',['Build a','piano phrase.'],['C – Am – F – G','Arpeggios with a bass pattern.']),
 ('scales',['Practice in','your key.'],['C major. G major. E minor.','Scales, modes and local PDFs.']),
]):
 overlay=Image.new('RGB',(1920,1080),PAPER)
 text(overlay,(62,65),'SONATA PIANO',30,COPPER)
 text(overlay,(62,120),'SCORES · SCALES · COMPOSER MODE',17,COPPER)
 for j,line in enumerate(lines):text(overlay,(62,350+j*80),line,62,serif=True)
 for j,line in enumerate(sub):text(overlay,(62,575+j*44),line,27)
 text(overlay,(62,920),'Coming in Sonata 1.1',22,COPPER)
 text(overlay,(62,967),'sonatapiano.app',24)
 plate=OUT/f'plate-{n}.png';overlay.save(plate)
 raw=VIDEO/f'2041A106-1EF4-4A29-AFD5-B4794F2A0DD4-{key}.mp4'
 clip=OUT/f'clip-{n}.mp4';clips.append(clip)
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','3.4','-t','8','-i',str(raw),'-loop','1','-i',str(plate),'-filter_complex','[0:v]transpose=1,scale=1300:975,setsar=1,fps=30[app];[1:v][app]overlay=570:52:shortest=1,format=yuv420p[out]','-map','[out]','-t','8','-an','-c:v','libx264','-preset','medium','-crf','20',str(clip)]
 subprocess.run(cmd,check=True)
concat=OUT/'concat.txt';concat.write_text(''.join("file '"+p.name+"'\n" for p in clips))
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(OUT/'sonata-composer-preview.mp4')],check=True)
subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','5','-i',str(OUT/'sonata-composer-preview.mp4'),'-frames:v','1',str(OUT/'video-poster.png')],check=True)
for p in clips+[concat]+list(OUT.glob('plate-*.png')):p.unlink()
