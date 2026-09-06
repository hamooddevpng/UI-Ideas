# Design 12 — Neo-Brutal Telikom

## Status
Standalone build brief for `12.html`. Existing designs remain unchanged.

## Portfolio position
- Gen-Z affinity: **10/10**
- Enterprise / premium: **1/10**
- UX clarity: **8/10**
- PNG identity: **6/10**
- Motion: **5/10**
- Complexity: **4/10**
- Similarity to existing Telikom family: **0/10 target**

## Design thesis
Build a deliberately raw, confident, anti-polish homepage that uses large typography, hard borders, visible grid lines and almost no decorative rounded-card language. This should feel like a contemporary editorial/poster system rather than a telecom website template.

The concept is not “ugly.” It is precise, bold and stripped back. It achieves youth relevance through typography and visual confidence rather than glossy animation.

## First screen
No photographic hero banner.

Use a full viewport poster made from:
- Large Telikom logo and slogan.
- One massive statement such as “CONNECT / PNG / NOW.”
- A hard-edged grid with 3–4 high-priority actions embedded into the typography.
- One narrow real-PNG photo strip rather than a normal hero image.
- A vertical service index numbered 01–05.
- Chatbot fixed bottom-right.

The navigation itself can appear as a visible rule/grid rather than a floating capsule.

## Page architecture
1. Poster hero / index.
2. Full-width service selector where each row is a huge typographic block: Mobile, Home, Business, Remote, Support.
3. Gutpela plans as a comparison table with oversized price/data typography, not cards.
4. People / PNG story section using hard split-screen photos and captions.
5. Business section as a monochrome information matrix.
6. Technology / infrastructure statement with diagrams or line art.
7. Self Care task list.
8. News as newspaper-like rows.
9. Footer as a strong blue block.

## Visual system
### Palette
- Telikom Blue: `#0875C9`
- Deep Blue: `#064F87`
- White: `#FFFFFF`
- Pale Blue: `#EAF4FB`
- Ink: `#0B2535`
- Rule Grey: `#D5E4EE`

Use nearly flat colour. Avoid gradients except extremely subtle image overlays when absolutely necessary.

### Typography
Gibson preferred. Use extreme contrast between display size and micro-labels. Headings can approach poster scale. Do not use script, handwritten or decorative fonts.

### Shapes
- Square corners or very small radius (0–4px).
- 1–3px borders.
- Thick horizontal rules.
- Numbered modules.
- No pill epidemic.
- No shadow-heavy floating cards.

## Interaction
Hover should be simple and physical: invert blue/white, shift text 4–8px, reveal arrow or enlarge a line. No 3D. No complex scroll hijacking.

Optional kinetic type can move gently on section entry. Reduced-motion must disable all movement without losing hierarchy.

## Navigation
A persistent grid header can use three regions: brand, primary navigation, utilities. Self Care and Top Up should read as explicit tasks. The header should not resemble the rounded floating headers in designs 8–10.

## PNG identity
Use real PNG people, landscapes and telecom infrastructure in narrow crops and editorial bands. Where PNG motifs are introduced, they must be abstracted into blue linework — not copied decorative patterns without context.

## Mobile
The design should translate exceptionally well to mobile because the system is essentially typography + rules.
- Scale display typography using `clamp()`.
- Convert wide matrices into horizontal scroll only where necessary; otherwise stack rows.
- Keep task actions full-width.
- Minimum touch targets 44px.
- Preserve hard-grid feel rather than converting everything into rounded cards.

## Chatbot
Use a blunt, rectangular mini-panel that reads like another interface block. Example initial line: “TELIKOM HELP / WHAT DO YOU NEED?” Use four text actions. No cartoon mascot.

## Accessibility and SEO
- Semantic heading structure despite oversized typography.
- Avoid all-caps for long paragraphs.
- High contrast throughout.
- Visible keyboard focus states should match the hard-rule system.
- One H1.
- Descriptive service links.
- Real links for plan actions and CTAs.

## Performance
This should be one of the lighter experimental concepts. Target CSS-first implementation with minimal vanilla JavaScript. No canvas/WebGL. Keep font loading conservative. Use responsive images and explicit dimensions.

## CMS model
Strong CMS compatibility. Content types can render into rows rather than complex cards. Promotions should be optional; absence of a promotion must not break the grid.

## Do not do
- Do not soften the concept with lots of 20px-radius cards.
- Do not add generic telecom hero photography above the fold.
- Do not use multiple accent colours.
- Do not turn brutality into messy spacing; every edge should be intentional.
- Do not copy designs 1–6 section rhythm.

## Success criterion
The page should look like Telikom commissioned a bold contemporary design studio to rethink the website from first principles. It should be instantly distinct even in a monochrome screenshot.