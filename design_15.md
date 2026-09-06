# Design 15 — Type Storm

## Portfolio position
- Gen-Z: **9/10**
- Premium: **4/10**
- UX clarity: **7/10**
- PNG identity: **5/10**
- Motion: **10/10**
- Complexity: **8/10**
- Similarity target: **0/10**

## Thesis
Make typography itself the homepage interface. The design should communicate connectivity through words moving, transforming and linking — not through conventional telecom card collections.

Core words: **CALL / STREAM / WORK / LEARN / BUILD / CONNECT / ANYWHERE / ANYTIME**. These words become service gateways and visual transitions.

## First viewport
Large Telikom logo + slogan, followed by enormous animated headline words occupying almost the entire screen. At any moment the user can see one dominant word and the associated service label.

Example sequence:
- CONNECT → all services
- MOVE → Mobile
- HOME → home internet
- BUILD → Business
- REACH → Remote / VSAT

A slim task rail provides Top Up, Pay Bill, Coverage and Support.

## Structural model
The page is a series of typographic scenes rather than conventional sections.
1. Brand statement / CONNECT.
2. MOVE — Mobile and data.
3. HOME — household connectivity.
4. BUILD — business and enterprise.
5. REACH — remote PNG.
6. PEOPLE — community stories.
7. DO — Self Care utilities.
8. KNOW — news and support.

Each scene contains real HTML content attached to the giant word.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Mid Blue `#2789CA`
- Powder Blue `#BFE0F3`
- Paper `#F7FBFD`
- Ink `#0A2433`
- White `#FFFFFF`

### Type
Gibson preferred. Use variable font capabilities only if the licensed brand font supports them; do not invent unauthorized brand typography. Prototype fallback may use a variable grotesk. The design should rely on scale, weight and outline/fill states.

### Imagery
Photos appear selectively inside letter masks, narrow full-width strips or side panels. Avoid a standard rectangular hero photo.

## Motion language
- Words can slide horizontally, stretch within safe font ranges, switch outline/fill, or reveal images.
- Scroll should drive progress but not be hijacked.
- Do not move body copy while the user is reading it.
- Hover/focus can animate a word’s associated line/arrow.
- Reduced-motion uses static word scenes.

## Navigation
Header should be very minimal: logo/slogan, Services, Support, Self Care, Top Up. Provide a chapter/index menu listing the scene words so users can jump directly.

## Plans
Do not use four repeated rounded cards. Present plans as typographic rows where data allowance and price dominate, separated by strong horizontal rules. A single highlighted plan may invert to blue.

## Business
The BUILD scene should deliberately become more disciplined: large “BUILD” word on one side, a structured list of enterprise capabilities on the other. This creates contrast without changing design language.

## PNG identity
The PEOPLE and REACH scenes should use strong real PNG photography and place names. Any location or coverage statement must be validated; otherwise speak generally about Papua New Guinea’s varied geography.

## Chatbot
Minimal type-led chatbot. Launcher can be a small “HELP?” label rather than a circular icon, still fixed bottom-right. Opening panel should use normal readable UI, not experimental moving type.

## Mobile
Mobile uses vertical type scenes with text-size ceilings. Giant words may crop intentionally but the service meaning must remain visible. Do not use horizontal overflow as the main navigation. Keep task actions sticky at bottom.

## Accessibility
- Motion does not carry unique information.
- Semantic headings are separate from purely decorative giant lettering where required.
- Ensure outlined text retains sufficient contrast.
- Provide keyboard focus that does not trigger disorienting animation.
- One H1.

## Performance
CSS transforms and IntersectionObserver preferred. Avoid animation libraries unless necessary. Do not render typography to canvas. Use `will-change` sparingly. Keep initial font payload small and use fallback metrics to avoid layout shift.

## CMS
Editors manage normal titles, summaries and links. Display words should come from a small fixed vocabulary controlled by the design, not arbitrary CMS input that can break compositions.

## Do not drift into
- standard hero + image + plan cards;
- random 3D objects;
- neon gradients;
- text that constantly moves while being read;
- over-reliance on all-caps for paragraphs.

## Success
A screenshot of any major section should immediately read as a typography-led identity system rather than a standard telecom page.