# Design 29 — Network Observatory

## Status
Standalone specification for `29.html`. Existing concepts must remain untouched.

## Portfolio position
- Gen-Z affinity: **6/10**
- Enterprise / premium: **10/10**
- UX clarity: **8/10**
- PNG identity: **8/10**
- Motion: **8/10**
- Code complexity: **9/10**
- Similarity target vs current Telikom / Shahbaz-Nasir / designs 1–6: **0/10**

## Design thesis
Present Telikom as a sophisticated national telecommunications operator through the visual language of a network observatory: elegant data visualisation, infrastructure diagrams, status-like modules, national connectivity stories and enterprise capability. The experience should feel authoritative and technical without becoming a dark “network operations centre” dashboard.

This is the premium infrastructure/data extreme of the portfolio.

## First viewport
Do not use a traditional photo hero.

Create an observatory stage containing:
- large Telikom logo + clearly readable slogan;
- a concise headline such as “See the network behind every connection.”;
- a large abstract network/topology visual or PNG-based geographic diagram;
- 3–4 validated or clearly non-numeric service indicators such as Mobile / Fixed / Enterprise / Remote;
- direct utilities: Personal, Business, Self Care, Support.

If real operational metrics are not approved, **do not invent uptime, capacity, province counts or live status values**. Use qualitative labels or clearly marked demonstration data.

## Page architecture
1. Network observatory opening.
2. Service-layer explorer: Mobile / Home / Business / Remote.
3. PNG infrastructure/geography feature.
4. Enterprise capability matrix.
5. Products/plans in a restrained comparison module.
6. Technology chapter: fibre, fixed, voice, hosting, satellite — only approved portfolio items.
7. People/community story to keep the site human.
8. Self Care / Support operational panel.
9. News, service notices and corporate updates.
10. Footer.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Deep Blue `#075D98`
- Steel Blue `#BFDDED`
- Pale Blue `#EDF6FA`
- Ink `#102C3D`
- White `#FFFFFF`
- Line `#C5D8E2`

The page should be predominantly light. Use dark blue only for short high-contrast modules; avoid the overly dark treatment Christopher criticised.

### Typography
Approved Gibson preferred. Technical labels can use a compact mono-style fallback only as a secondary decorative/metadata layer if needed, never as the main brand font. Headings should remain premium and readable.

### Geometry
- thin grid/rule lines;
- restrained square/8–12px corners;
- data panels with hierarchy rather than repeated cards;
- charts/diagrams integrated into whitespace;
- no excessive glassmorphism.

## Data visualisation rules
Any graph, metric or network diagram must belong to one of three categories:
1. **Approved factual data** — can be presented as real.
2. **Illustrative conceptual diagram** — label as illustrative where needed.
3. **Prototype demo data** — clearly label as sample/demo; do not make it look authoritative.

Never fabricate network uptime, bandwidth capacity, customer numbers or coverage.

## Interaction
- service-layer toggles update the main diagram;
- hover/focus highlights a network path and associated service description;
- scroll may progressively reveal layers;
- optional SVG animation for signal flow;
- avoid mandatory scroll-jacking.

Reduced-motion freezes signal animation and uses immediate state changes.

## Business / enterprise emphasis
This is one of the strongest enterprise concepts. Provide a clear matrix of business data, connectivity, voice, hosting/systems and remote services based on approved scope. Use contact/proposal CTAs without implying unsupported SLAs or capabilities.

## People / PNG balance
The technical aesthetic must not erase the People pillar. Include at least one major PNG photographic section showing people or organisations using connectivity. This should break the diagram rhythm and reinforce local identity.

## Self Care
Use a calm operational task panel: Top Up, Pay Bill, Buy Data, Coverage, Store Locator, Contact Support. Do not overload with mock account metrics.

## Chatbot
Fixed bottom-right. Visual style can resemble an operations assistant, but wording stays human and simple. No “AI network analyst” claims. Actions: Consumer Help, Business Help, Coverage, Support.

## Mobile
Mobile should not attempt to display a complex desktop topology at full detail. Simplify to:
- overview diagram;
- service-layer tabs;
- stacked data/description panels;
- a text service index.
Keep critical utilities above the fold.

## Accessibility
- charts/diagrams need text equivalents or summaries;
- interactive SVG nodes keyboard accessible where necessary;
- colour is never the only distinction;
- one H1;
- visible focus states;
- high contrast labels;
- avoid tiny “data dashboard” type below accessible sizes.

## SEO
All technical/service content exists as semantic HTML, not canvas-only. Use clear Mobile, Home Internet, Business and Remote headings. Any structured data must reflect actual approved content.

## Performance
SVG is preferred over canvas where practical. If canvas/WebGL is used for a premium hero visual, provide a static fallback and lazy-init after first content paint. Pause animations when offscreen. Optimize image and script payload aggressively.

## CMS
CMS controls service descriptions, approved facts, stories, notices and CTAs. Visualisation configuration should be constrained and mapped to predefined service layers. Editors should never have to edit raw chart code.

## Must avoid
- Fake live network metrics.
- Dark cyberpunk/neon styling.
- Tiny unreadable dashboards.
- A generic hero image behind charts.
- Reusing the plan-card/business-card rhythms of designs 1–6.

## Definition of success
The page should make Telikom feel technically capable, nationally important and enterprise-ready, while remaining light, modern and credible enough for customers and government stakeholders.