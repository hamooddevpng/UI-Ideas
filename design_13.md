# Design 13 — Telikom Stories

## Status
Build target: `13.html`. This is a standalone concept.

## Portfolio position
- Gen-Z affinity: **10/10**
- Enterprise / premium: **2/10**
- UX clarity target: **7/10**
- PNG identity target: **9/10**
- Motion: **9/10**
- Complexity: **7/10**
- Similarity to existing directions: **1/10 or lower**

## Concept
Reinterpret the homepage as a sequence of full-screen “stories,” inspired by familiar swipe-based social interfaces but adapted responsibly for a telecom website. Every story has a clear job: Mobile, Home, Business, PNG, Remote, Self Care, Support.

This is not a literal Instagram clone. It uses the mental model of chapters, progress and tap/swipe navigation to create a young, image-led experience.

## First-screen experience
A full-viewport PNG image/video-still with high-contrast readable text, minimal controls and a visible story progress indicator across the top. The first story introduces Telikom and the slogan; lower thumb-zone controls give “Next,” “Explore services,” and essential utilities.

Desktop: split click zones or arrow navigation plus wheel/keyboard support.
Mobile: natural swipe or tap zones.

The primary navigation should remain accessible outside the story progression so users are never trapped.

## Story sequence
Suggested 8 chapters:
1. **Telikom / Connected PNG** — brand + slogan.
2. **Mobile** — everyday communication / Gutpela data.
3. **Home** — households, learning, entertainment.
4. **Business** — people at work, enterprise connectivity.
5. **Remote** — islands/highlands/VSAT.
6. **People & Community** — PNG identity and stories.
7. **Self Care** — Top Up, Pay Bill, Buy Data, Coverage.
8. **Support / One Network** — stores, 1555, contact, CTA.

After the story sequence, provide a conventional but visually consistent scrollable content index containing plan comparison, news and footer. This protects SEO/accessibility and gives power users a stable fallback.

## Visual style
Large full-bleed photography with extremely restrained blue overlays. Imagery must remain visible. Use the official Telikom blue for progress indicators, interactive labels and CTA accents.

### Palette
- Telikom Blue: `#0875C9`
- Mid Blue: `#3594D1`
- Light Blue: `#D7EDFA`
- Near White: `#F8FCFE`
- Ink: `#122E3F`
- White: `#FFFFFF`

Avoid green outside the official logo.

## Typography
Gibson preferred. Keep story headlines short and large. Supporting copy should rarely exceed 2–3 lines per story. The page should feel visual, not text-heavy.

## Interaction details
- Top segmented progress bar.
- Wheel, swipe, arrow-key and accessible button navigation.
- Pause progression when the user interacts; never auto-advance critical content without control.
- Subtle image pan/zoom can create movement.
- Optional slide transitions or mask reveals.
- `prefers-reduced-motion` converts transitions to simple fades.
- Do not autoplay audio.

## Service actions
Each chapter must contain 1 primary and no more than 2 secondary actions. Example: Mobile → “View mobile plans”; Home → “Explore home internet”; Business → “Business solutions.”

Persistent quick utilities should remain reachable via a bottom dock or utility button: Top Up, Pay Bill, Coverage, Support.

## PNG storytelling
This direction succeeds or fails on imagery. Use Papua New Guinean people, communities, homes, businesses and landscapes. Avoid generic stock. Use alt text that describes the actual scene rather than keywords.

## Chatbot
Chatbot should look like a compact story reply control. Fixed bottom-right on desktop; on mobile it should sit above the browser safe area and not conflict with story navigation. Initial greeting: “Need help while you explore?” Actions: Top Up / Plans / Coverage / Support.

## Desktop architecture
Stories occupy 100svh sections with scroll snapping but must not trap scroll. Provide visible chapter navigation. After the final chapter, transition naturally into the standard content index.

## Mobile architecture
Make mobile the native version:
- 100dvh slides.
- Safe-area padding.
- Tap left/right or swipe.
- Text occupies top/bottom zones away from faces.
- Utility actions in thumb-friendly bottom sheet.
- Support browser back/forward gracefully; do not alter history on every story.

## Accessibility / SEO
Story content must exist as real semantic HTML, not canvas text. Each chapter uses headings in logical order. Only chapter 1 uses H1. Provide skip link: “Skip stories and browse services.” All gestures need visible control equivalents. Keyboard and screen-reader users must be able to navigate sequentially.

## Performance
- Prefer optimized images / AVIF/WebP.
- Preload only first story visual; lazy-load later chapters.
- No heavy video required for prototype.
- JS should orchestrate navigation, not render content.

## CMS
Model each story as a configurable content item: title, label, image, body, CTA, theme alignment. Editors should be able to reorder or disable chapters.

## Must avoid
- Recreating a normal hero then card grid beneath it.
- Tiny unreadable text over photos.
- Automatic rapid slide changes.
- Dark navy overlays hiding PNG imagery.
- Social-media gimmicks that interfere with task completion.

## Success
A young user should understand the interaction within seconds, while a Telikom stakeholder should still find Mobile, Home, Business, Remote and Support clearly represented.