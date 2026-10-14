#!/usr/bin/env python3
"""Compose promotional assets from unaltered build-49 app captures/recordings.
Usage: python3 tools/render_composer_preview.py CAPTURE_DIR VIDEO_DIR ASC_OUTPUT
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps
import subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
CAP, VIDEO, ASC=map(Path,sys.argv[1:4])
OUT=ROOT/'assets/composer-preview'; OUT.mkdir(parents=True,exist_ok=True)
SERIF='/System/Library/Fonts/Supplemental/Georgia.ttf';SANS='/System/Library/Fonts/HelveticaNeue.ttc'
PAPER='#F4EFE6';INK='#28231F';COPPER='#9C4928'
def font(size,serif=False):return ImageFont.truetype(SERIF if serif else SANS,round(size))
def text(im,xy,t,size,color=INK,serif=False):ImageDraw.Draw(im).text(xy,t,font=font(size,serif),fill=color,anchor='lt')
def contain(im,src,box):
 x,y,w,h=map(int,box);tile=ImageOps.contain(src.convert('RGB'),(w,h),Image.Resampling.LANCZOS);im.paste(tile,(x+(w-tile.width)//2,y+(h-tile.height)//2))
def capture(device,name):return Image.open(CAP/f'release49-{device}-{name}.png')
stories=[
 ('02-sheet',['Follow every','note.'],'Highlighted notes. Names when you need them.'),
 ('03-arpeggios',['Build music','in key.'],'Chords, arpeggios and your own piano notes.'),
 ('05-scales-setup',['Practice in','your key.'],'Major, minor and modes. Choose each run.'),
 ('06-scale-sheet',['Your practice.','On paper.'],'Key-labeled sheets. Save locally. Export PDF.'),
 ('04-compose-play',['Hear it.','Play it again.'],'Pause, resume and repeat your whole piece.'),
]
for device in ['iphone','ipad']:
 # Use accepted portrait iPhone and landscape 13-inch iPad dimensions.
 w,h=(1320,2868) if device=='iphone' else (2752,2064)
 for i,(story,lines,sub) in enumerate(stories,1):
  im=Image.new('RGB',(w,h),PAPER)
  if device=='iphone':
   text(im,(86,80),'S O N A T A   P I A N O',34,COPPER)
   for j,line in enumerate(lines):text(im,(84,185+j*134),line,116,serif=True)
   # Keep long subheads at a readable size, inside the canvas.
   size=min(36,1120/font(36).getlength(sub)*36)
   text(im,(86,492),sub,size)
   contain(im,capture(device,story),(50,605,w-100,h-675))
  else:
   text(im,(100,80),'S O N A T A   P I A N O',38,COPPER)
   text(im,(100,175),' '.join(lines),116,serif=True)
   text(im,(100,325),sub,42)
   contain(im,capture(device,story),(80,455,w-160,h-510))
  target=ASC/device/f'{i:02}-{story}.png';target.parent.mkdir(parents=True,exist_ok=True);im.save(target)
# Web gallery retains full actual UI at efficient display sizes.
for device,name,out in [('ipad','01-highlights','highlights'),('ipad','04-compose-play','arpeggios'),('ipad','05-scales-setup','scales'),('ipad','06-scale-sheet','practice-sheet'),('iphone','02-sheet','phone-highlights')]:
 im=capture(device,name).convert('RGB');im.thumbnail((1600,1800),Image.Resampling.LANCZOS);im.save(OUT/f'{out}.png',optimize=True)
clips=[]
for n,(key,lines,sub) in enumerate([
 ('highlights',['Follow','the music.'],['Highlighted notes.','Note names to guide you.']),
 ('arpeggios',['Build a','piano phrase.'],['C – Am – F – G','Arpeggios with a bass pattern.']),
 ('scales',['Practice in','your key.'],['C major. G major. E minor.','Scales, modes and local PDFs.']),
]):
 overlay=Image.new('RGB',(1920,1080),PAPER)
 text(overlay,(62,65),'SONATA PIANO',30,COPPER)
 text(overlay,(62,120),'NEXT RELEASE PREVIEW',20,COPPER)
 for j,line in enumerate(lines):text(overlay,(62,350+j*80),line,62,serif=True)
 for j,line in enumerate(sub):text(overlay,(62,575+j*44),line,27)
 text(overlay,(62,920),'Actual app · Internal testing',22,COPPER)
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
(OUT/'demo.vtt').write_text('WEBVTT\n\n00:00.000 --> 00:08.000\nNext release preview: follow highlighted notes and note names.\n\n00:08.000 --> 00:16.000\nBuild C–Am–F–G arpeggios with a bass pattern in Composer Mode.\n\n00:16.000 --> 00:24.000\nPractice C major, G major and E minor. Choose scales and modes; export PDF.\n')
