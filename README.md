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

The page labels 1.0.6 as a TestFlight preview because the public App Store version was 1.0.5 at preparation time. Remove the TestFlight availability note only after confirming 1.0.6 is publicly released.

Deployment uses the repository's GitHub Pages configuration. Commit and push only after authorization, then verify the Pages deployment and the public video URL. Updating files locally does not publish them.

Grokbot's existing host check can be run without installing it:

```sh
PYTHONPATH="$HOME/repos/grokbot/src" python3 -m grokbot.cli legal-urls check --site sonata
```

The canonical GitHub Pages legal URLs redirect to the custom domain. No legal page text or URLs were changed for this campaign.

## Marketing checks — September 16, 2026

The U.S. App Store listing confirms monthly $9.99, annual $69.99, and lifetime $249.99: https://apps.apple.com/us/app/sonata-piano/id6759943429. App Store Connect reports approved monthly and annual products with an active U.S. `FREE_TRIAL` offer lasting `ONE_WEEK`. Prices are labeled USD/U.S.; eligibility and local terms are left to Apple's purchase confirmation. Lifetime has a separate non-trial CTA. No prices or subscription configurations were changed.

The page uses the approved app UI assets instead of invented testimonials, ratings, student counts, or a fake live keyboard demonstration. Real keyboard footage and consented tester testimonials remain future additions requiring source material. Acoustic limitations and the TestFlight-only status of the new guide are visible in the FAQ.

The visual refresh uses warm ivory surfaces and copper accents, a product-led hero, visible keyboard focus, native FAQ disclosure controls, and reduced-motion CSS. Page content remains visible without JavaScript or IntersectionObserver support.
