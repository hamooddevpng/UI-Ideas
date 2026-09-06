# Design 30 — Cardless Corporate

## Portfolio position
- Gen-Z: **5/10**
- Enterprise / premium: **10/10**
- UX clarity: **9/10**
- PNG identity: **6/10**
- Motion: **3/10**
- Complexity: **4/10**
- Similarity target: **0/10**

## Design thesis
Build an ultra-refined corporate homepage with almost **no cards**. Hierarchy comes from typography, whitespace, rules, photography and layout proportion. This is deliberately different from the modern-web habit of placing every piece of content inside a rounded rectangle.

The page should feel expensive because it is disciplined, not because it has effects.

## First viewport
Use an asymmetric editorial composition:
- large Telikom logo + slogan in the navigation;
- huge but restrained statement on a white/light background;
- one tall or wide PNG photograph occupying a defined grid area;
- a short vertical index of Personal / Home / Business / Remote;
- direct Top Up / Self Care buttons.

No text over a dark image. No floating hero panel. No quick-action card dock.

## Page architecture
1. Cardless opening.
2. Services as large typographic rows separated by rules.
3. Mobile/Home product comparison as columns/table.
4. People / PNG photographic feature.
5. Business and enterprise as a precise two-column service index.
6. Technology / remote connectivity as image + text + diagram.
7. Self Care utility strip.
8. News as editorial headlines/list.
9. Corporate/company links.
10. Footer.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Deep Slate Blue `#154B6E`
- Pale Grey Blue `#DDE8EE`
- Paper `#F7F9FA`
- Ink `#142A36`
- White `#FFFFFF`
- Rule `#CBD8DE`

### Typography
Gibson preferred. Typography is the primary design asset. Use strong baseline rhythm and large headline scales. Body width must remain readable; do not use oversized type everywhere.

### Geometry
- mostly square/no-container layouts;
- 1px rules;
- occasional image radius 0–8px maximum;
- buttons may use modest radius but avoid pills everywhere;
- no shadows unless extremely subtle and functional.

## Services
Represent services as large text rows with a concise descriptor and arrow. Hover/focus can reveal an image crop or secondary description. On mobile, rows stay rows.

## Plans
Use a proper comparison grid. Data allowance, price and validity should align in columns. Highlight one plan with a blue rule or blue column, not a floating card.

## Business
The Business section should be visually strongest: a clear corporate statement, service taxonomy, contact CTA and one high-quality PNG business image. Avoid dark full-width corporate slabs.

## PNG identity
Use 2–3 exceptional local images rather than many mediocre images. Large photographs with captions have more impact than thumbnail cards.

## Motion
Very restrained:
- image reveal on scroll;
- underline/arrow motion on links;
- subtle nav transition.
No horizontal rails, WebGL, floating objects or parallax required.

## Chatbot
Standard professional fixed bottom-right. Use a small rectangular greeting bubble; launcher may be circular. Keep it visually secondary.

## Mobile
This should translate cleanly:
- headline scales down;
- service rows become stacked;
- comparison table becomes labelled row groups;
- image/text sequence follows semantic order;
- keep whitespace generous but not wasteful.

## Accessibility
Excellent target:
- semantic headings/lists/tables;
- clear focus states;
- strong contrast;
- no information dependent on hover;
- one H1;
- 44px touch targets.

## SEO
Excellent. Text-first structure ensures crawlability. Use descriptive service links, one keyword-focused H1 and useful section headings. Ensure images have dimensions/alt text and all primary CTAs are real anchors.

## Performance
Very light. CSS-first, minimal JS. This concept should be a performance benchmark. Use optimized responsive images and avoid unnecessary libraries.

## CMS
Excellent CMS friendliness. Content maps to service lists, plan tables, stories and news rows. The design should survive content updates without requiring pixel-perfect card copy lengths.

## Must avoid
- Adding cards during implementation “for neatness.”
- Rounded dashboard aesthetics.
- A hero overlay.
- Generic corporate stock photography.
- Multiple blue gradients.

## Definition of success
It should look more premium than the previous corporate concepts while using fewer visual components. The difference from the existing site must come from composition and restraint, not effects.