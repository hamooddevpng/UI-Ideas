# Design 18 — Signal Wave

## Portfolio position
- Gen-Z: **9/10**
- Enterprise / premium: **4/10**
- UX clarity: **6/10**
- PNG identity: **7/10**
- Motion: **9/10**
- Complexity: **8/10**
- Similarity target: **0/10**

## Design thesis
Turn the idea of telecommunications into a visible moving signal. A continuous wave/line travels through the homepage and changes meaning from voice to data to home to enterprise to remote connectivity. The line is the main compositional device, not a decorative SVG placed behind normal cards.

The visual energy can borrow from music/festival motion graphics, but the brand remains Telikom blue and the service content stays clear.

## First viewport
Use large typography and a live signal waveform occupying the visual center. The Telikom logo/slogan anchors the top. The wave passes through labelled nodes such as Mobile, Home, Business and Remote. A short headline explains the concept: “One signal. Millions of moments.”

Do not use a large photographic hero. Instead, reveal small PNG photo fragments inside wave nodes or masks.

## Structural journey
1. Signal origin / Telikom brand.
2. Voice + Mobile — wave becomes call/data pulse.
3. Home — wave broadens into household connectivity.
4. Business — wave becomes structured network paths.
5. Remote — wave extends over PNG landscape imagery.
6. People — photo mosaic synchronized to signal points.
7. Self Care — line resolves into task buttons.
8. Support/news/footer.

## Palette
- Telikom Blue `#0875C9`
- Bright Blue `#3A94CF`
- Light Signal Blue `#A9D8F1`
- Pale Background `#EAF6FC`
- Ink `#0B293C`
- White `#FFFFFF`
- Rule `#C8DCE8`

No neon rainbow waveform. Blue-only hierarchy is part of the challenge.

## Graphic language
- SVG paths / curves.
- Concentric signal arcs.
- Wave dots and labelled nodes.
- Cropped photography appearing through circular or wave-shaped windows.
- Typography may follow or intersect the path occasionally, but never for body copy.

## Interaction
Scroll controls the progress of one major signal line. Users should still be able to jump through navigation links; jumping should move directly to the appropriate section without replaying long animations.

Hover on nodes reveals concise service summaries. On touch, nodes become tap targets or simple stacked modules.

## Motion rules
- Animate path drawing with stroke-dashoffset or SVG path progress.
- Pulse only a few nodes at a time.
- Keep movement at 60fps using transforms/SVG, avoiding DOM-heavy particle systems.
- Reduced-motion displays the full signal path statically.
- Never move text continuously while users read.

## Plans
Plans can be represented as points on a data waveform or as horizontal rows intersecting the signal line. Avoid classic card decks. Price, allowance and validity must remain directly readable.

## Business
In the Business section, the freeform wave should become a precise network diagram/grid — a visual metaphor for enterprise reliability. Services appear as endpoints rather than six rounded cards.

## PNG identity
The Remote/People chapters should reveal strong Papua New Guinea landscapes, professionals and communities. The signal path may trace an abstract shape inspired by PNG geography, but must not imply exact coverage unless backed by validated data.

## Navigation
Minimal fixed header. Optional small progress waveform in header showing where the user is. Persistent utility actions for Top Up / Self Care / Support.

## Chatbot
Launcher can look like a small pulsing signal node fixed bottom-right. The panel itself must be stable and readable. Initial greeting: “Need help finding the right signal/service?” Actions remain conventional.

## Mobile
Do not try to preserve a huge lateral wave composition. Convert the signal into a vertical path running down the page with service nodes alternating left/right. Keep actions full-width and touch-friendly.

## Accessibility
- SVG is decorative unless interactive; decorative paths are hidden from assistive tech.
- Interactive nodes are real buttons/links with labels.
- Semantic HTML provides all service content.
- One H1.
- High contrast even where path crosses photos.
- Reduced-motion support is mandatory.

## Performance
Prefer SVG/CSS over canvas/WebGL. Keep path count small. Use IntersectionObserver to pause offscreen animation. Responsive/lazy images. No large animation library unless a small custom implementation becomes impractical.

## CMS
CMS controls text/images/services; the signal structure remains a design layer. Editors must not need to edit SVG coordinates. Allow services to map to pre-existing node slots.

## Must avoid
- A normal hero + waveform decoration.
- EDM/neon nightclub colours.
- Excessive looping pulses.
- Inaccessible text following curves.
- Making the page unreadable when JS fails.

## Success
The telecom idea should be visible in the page’s structure itself. Even with all images removed, the flowing signal language should make this concept recognizable.