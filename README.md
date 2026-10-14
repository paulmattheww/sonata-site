# Sonata Piano website

Static GitHub Pages site for https://sonatapiano.app. Preserve `CNAME`, `privacy.html`, and `terms.html` when updating promotional content.

## Local preview

```sh
python3 -m http.server 8767 --bind 127.0.0.1
```

Open http://localhost:8767. There is no build step or package installation.

## Version 1.0.6 campaign

Approved assets live in `assets/campaign-1.0.6/`. The video is an 18-second silent H.264 MP4, with a poster and English caption track. `assets/video-preview.js` requests muted inline playback once, when at least half the player is visible. It pauses when scrolled out of view or the tab is hidden. Native controls remain available, and scrolling back does not override a pause or restart a finished video. Reduced-motion preferences, supported data-saving preferences, unsupported observers, and browser autoplay restrictions all retain manual playback. Screenshots are linked at full resolution and lazy-loaded with explicit dimensions.

These visuals were rendered from the updated app's production Flutter widgets, not a live recording of microphone or MIDI recognition. Do not claim that the campaign demonstrates recognition accuracy. The falling-note guide is iPad-only; iPhone imagery shows the notation and keyboard view.

1.0.6 is publicly released on the App Store. Landing copy treats the iPad falling-note guide as publicly available on the App Store.

Deployment uses the repository's GitHub Pages configuration. Commit and push only after authorization, then verify the Pages deployment and the public video URL. Updating files locally does not publish them.

Grokbot's existing host check can be run without installing it:

```sh
PYTHONPATH="$HOME/repos/grokbot/src" python3 -m grokbot.cli legal-urls check --site sonata
```

The canonical GitHub Pages legal URLs redirect to the custom domain. No legal page text or URLs were changed for this campaign.

## Marketing checks — September 16, 2026

The U.S. App Store listing confirms monthly $9.99, annual $69.99, and lifetime $249.99: https://apps.apple.com/us/app/sonata-piano/id6759943429. App Store Connect reports approved monthly and annual products with an active U.S. `FREE_TRIAL` offer lasting `ONE_WEEK`. Prices are labeled USD/U.S.; eligibility and local terms are left to Apple's purchase confirmation. Lifetime has a separate non-trial CTA. No prices or subscription configurations were changed.

The page uses the approved app UI assets instead of invented testimonials, ratings, student counts, or a fake live keyboard demonstration. Real keyboard footage and consented tester testimonials remain future additions requiring source material. Acoustic limitations and the iPad-only status of the new guide are visible in the FAQ.

The visual refresh uses warm ivory surfaces and copper accents, a product-led hero, visible keyboard focus, native FAQ disclosure controls, and reduced-motion CSS. Page content remains visible without JavaScript or IntersectionObserver support.

## First Light and Composer mode — October 12, 2026

The header, hero, favicon and touch icon use the approved First Light artwork
from Sonata's iOS asset catalog (source app commit `1556b75`). The 1024 px master
and existing 180/40 px catalog assets are copied directly without regenerating
the logo. Orange actions use dark text for contrast; existing campaign
screenshots and video are retained. Legal text, links and CNAME are unchanged;
only favicon references changed in the legal-page heads.

The Composer mode section describes the internal testing milestone: blank piano,
chord/arp guidance, passing-note suggestions, themes, exact range, section bass,
mixed meters, looping, local collections and generated-score PDF export. It is
clearly labeled upcoming and unavailable in the public App Store build. Remove
that qualification only after public release is verified.

## Composer preview — October 14, 2026

The new 24-second silent H.264 video and gallery are actual build-49 captures:
Amazing Grace's documented Mutopia public-domain hymn edition, original C–Am–F–G
arpeggios with a 1–5–1–8 bass pattern, and C-major/G-major/E-minor scale runs.
The page labels these capabilities as upcoming/internal testing. Composer Mode
is not yet available in the public App Store build. No public app release is
implied by publishing this website preview.

Five ASC screenshots per device were prepared alongside this campaign (iPhone
1320×2868 portrait; iPad 2752×2064 landscape). They are not published to ASC by
this repo. Source captures and screenshots are in Sonata's local
`output/releases/sonata-composer-49/` report folder. Reproduction is in
`tools/render_composer_preview.py`; source UI capture is in Sonata commit
`e1803ac`, `mobile/integration_test/release49_capture_test.dart`.

Paul subsequently confirmed that the older catalogue is already cleared. The
release preview now also uses the approved Für Elise captures; this records the
owner's clearance, rather than a new independent legal determination.
First Light artwork, the existing native video controls/reduced-motion logic,
and the legal pages remain in place. Library engraving credits Verovio.

Checks: all local asset paths and anchor targets resolve, image aspect ratios
match their attributes, screenshots use RGB with accepted device dimensions,
and video is 1920×1080 H.264 / 24 seconds with no audio track. All generated
screenshots and sample video frames were inspected. The local website browser
preview was denied by a saved browser-permission setting; no local browser
layout verification is claimed.


## Sonata 1.1 release preview refresh — October 14, 2026

The site now uses First Light cream/orange accents, the approved header and search
artwork, a 1200×630 social sharing image, and actual highlighted Für Elise captures.
Composer Mode copy covers configurable scales/modes, 1–5–1–8 bass patterns,
collection time signatures with section overrides, and portrait PDF export.
The old measure-card PDF preview is replaced with the corrected build-51 score;
`assets/composer-preview/daily-scales.pdf` is a downloadable original exercise.

The 24-second video uses the same real build-49 recordings with updated title
plates. Reproduce this refresh with:

```sh
python3 tools/refresh_release_preview.py ../sonata/output/releases
```

The earlier renderer is retained for historical reproduction only; it generates
older ASC screenshots and must not be used for the current listing.

Availability remains **Coming in Sonata 1.1** until the public App Store release
is verified. Publishing this site does not submit or release the app. The owner
reports attaching the production build in ASC; submission encountered a missing
Spanish (Mexico) What's New field. No app availability is inferred from that.

Validation: asset paths, image dimensions, internal anchors, PDF identity and
video encoding/duration are checked locally. Assets and video frames are inspected.
No browser layout verification is claimed because the browser preview permission
was unavailable. Legal pages, tracking parameters and subscription prices remain
unchanged.
