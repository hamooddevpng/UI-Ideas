# Design 11 — Sticker Signal

## Status
Specification only. Do not modify designs 1–10 when implementing this concept. The implementation target is `11.html` plus design-specific assets only when necessary.

## Position in the portfolio
- Gen-Z affinity: **10/10**
- Enterprise / premium: **0/10 by intent**
- UX clarity target: **6/10 minimum**
- PNG identity target: **8/10**
- Motion level: **8/10**
- Code complexity: **6/10**
- Similarity target vs current Telikom / Shahbaz-Nasir / designs 1–6: **0–1/10**

## Purpose
This is the deliberate youth extreme in the concept portfolio. It should prove that Telikom can look energetic, expressive and culture-aware without abandoning the official logo or blue-led identity. Management may never select this direction in full; that is acceptable. Its job is to establish the outer boundary of what “fresh and distinctive” can mean.

The design must not look like a conventional telecom homepage with a hero image and tidy service cards. It should feel closer to a curated digital scrapbook, youth campaign microsite or creator platform — while still remaining usable.

## Core idea
Treat every Telikom service as a collectible “signal sticker.” The page is made of layered, slightly rotated objects: plan tickets, handwritten-style annotations, photo cut-outs, signal arrows, location stamps, PNG map fragments, oversized service labels and small utility chips. The composition should feel intentionally assembled rather than generated from a standard 12-column corporate template.

Use controlled visual chaos. Important actions must still snap into a predictable utility rail.

## First-screen experience
No classic left-copy/right-photo hero.

The opening viewport should contain:
1. Large Telikom logo and visible slogan at top left.
2. Oversized headline occupying roughly half the screen, e.g. “PNG / ALWAYS / CONNECTED.”
3. A central collage made from 4–6 floating objects: Mobile, Home, Business, Remote, Self Care, Coverage.
4. A bottom or side utility strip with Top Up, Pay Bill, Buy Data, Coverage and Support.
5. A fixed chatbot greeting in the bottom-right corner.
6. At least one real PNG photograph treated as a cut-out or irregular mask rather than a rectangular hero photo.

Avoid dark overlays. The overall page should feel bright and blue-led.

## Information architecture
Suggested order:
1. Sticker-collage introduction.
2. “Pick your signal” interactive service wall.
3. Gutpela plan tickets displayed like event passes / collectible cards.
4. PNG people-and-place collage with three real-life stories.
5. Self Care as a phone-shaped utility panel.
6. Business / enterprise section that intentionally becomes calmer and more structured.
7. Remote connectivity / VSAT represented as a route or location stamp.
8. Latest news presented like stacked clippings.
9. Support and store locator as a clean final utility zone.
10. Footer.

## Visual system
### Palette
- Telikom Blue: `#0875C9`
- Bright Blue: `#2B91D5`
- Sky Tint: `#B9DFF4`
- Paper Blue: `#EEF8FD`
- Ink: `#0D2D42`
- White: `#FFFFFF`
- Divider: `#C7DCE8`

Do **not** introduce green, orange, purple, red or neon accent families. Youthfulness comes from composition, typography and movement, not rainbow colour.

### Typography
Use approved Gibson when available. For prototype fallback, use a strong grotesk/sans pairing with radically different scale levels. Headline type can be huge and compressed; utility and legal text must remain conventional and readable.

### Geometry
- Rotations: usually ±2–6 degrees; never random enough to hurt scanning.
- Mix circles, ticket perforations, irregular photo masks and hard rectangular labels.
- Avoid a page full of identical rounded cards.
- Shadows should feel like physical paper layers, not generic SaaS cards.

## Interaction and motion
- Stickers can drift a few pixels based on pointer movement.
- Hover can straighten a tilted object or pull it to the top layer.
- Section transition can slide labels or stamps into place.
- Plan tickets may fan out slightly.
- No continuous high-frequency animation.
- Respect `prefers-reduced-motion`; in reduced-motion mode everything becomes static but fully understandable.

## Navigation
Use an unconventional but stable top strip. The logo remains fixed; core navigation can appear as compact pills or text labels. Do not hide critical navigation behind experimentation. A mobile hamburger is acceptable.

## Chatbot
Chatbot should match the playful visual language: compact blue speech label with a friendly initial message such as “Hey 👋 What do you want to do?” It must stay fixed bottom-right. Actions: Top Up, Plans, Coverage, Support.

## Mobile behavior
Mobile is not a squeezed collage. Convert the experience into a vertical “sticker feed.”
- One dominant object at a time.
- Sticky utility bar at bottom.
- No pointer-driven effects.
- Photo cut-outs become full-width masked blocks.
- Minimum 44px touch targets.
- Avoid overlapping elements that could block text.

## Content rules
- Products, People and Technology must all be visible.
- Use approved/validated plan and product data only when finalising.
- Do not use “Cheap Plans”; use approved customer-friendly wording such as “Affordable Plans.”
- Real PNG photography should dominate over generic global stock.

## Accessibility / SEO / performance
- One real H1.
- All service actions are anchors/links, not fake buttons.
- Logical heading order despite the collage appearance.
- Decorative stickers receive `aria-hidden=true`; meaningful imagery has useful alt text.
- Lazy-load below-the-fold imagery.
- Avoid large JS frameworks for draggable effects; CSS + small vanilla JS preferred.
- No WebGL required.
- The full page must remain usable with JavaScript disabled.

## CMS considerations
Every visual object should map back to a small number of content types: Promotion, Service Gateway, Plan, Story, News Item, Utility Action. Editors should change copy/images without needing to understand the collage positioning code.

## Must not drift into
- A centered hero banner followed by six equal quick-action cards.
- Dark navy backgrounds covering photography.
- Generic glassmorphism.
- Random multicolour gradients.
- A standard card grid with stickers merely added as decoration.

## Definition of success
At a glance, nobody should confuse this with the current Telikom website, Shahbaz/Nasir’s implementation or designs 1–6. A young user should find it unusually expressive; a corporate reviewer should immediately understand that it is intentionally the youth-end benchmark of the portfolio.