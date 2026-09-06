# Design 19 — Choose Your World

## Portfolio position
- Gen-Z: **8/10**
- Enterprise / premium: **7/10**
- UX clarity: **9/10**
- PNG identity: **8/10**
- Motion: **8/10**
- Complexity: **8/10**
- Similarity target: **0/10**

## Purpose
This is a serious management-ready middle ground: highly distinctive without becoming deliberately weird. The entire homepage begins by asking which Telikom “world” the visitor belongs to rather than promoting a generic hero message.

## Core interaction
Five full-screen or large-screen gateways:
1. Personal / Mobile
2. Home
3. Business & Enterprise
4. Government / Institutional (only if content scope is approved)
5. Remote / Satellite

The user can move between worlds through tabs, wheel, drag or explicit navigation. Each world changes imagery, layout emphasis and featured actions while preserving one coherent Telikom blue design system.

## First screen
Large Telikom logo/slogan plus statement: “Where do you want to connect?” The remainder of the viewport is dominated by 4–5 large world selectors. Avoid a hero image behind the entire page. Use each world’s photo as part of its gateway.

A persistent utility rail gives Top Up, Self Care, Coverage and Support regardless of selected world.

## World behavior
Selecting a world expands it to become the active stage while others collapse to a thin rail/index. The active stage shows:
- 1 strong image;
- 1 short statement;
- 2–4 key service links;
- one primary action.

Do not overload gateways with plan details.

## Page architecture
1. World selector opening.
2. Active-world explorer.
3. “Popular right now” contextual content based on selected world.
4. Cross-world Products / People / Technology story.
5. Plan/service comparison.
6. PNG national/remote story.
7. Self Care task zone.
8. News/support/footer.

The selected world can influence later content client-side, but all content must remain discoverable without selection.

## Palette
- Telikom Blue `#0875C9`
- Deep Blue `#0867AC`
- Soft Blue `#D5EDF9`
- Paper `#F7FBFD`
- Ink `#102F43`
- White `#FFFFFF`
- Divider `#C6DBE7`

## Typography
Gibson preferred. World titles can be very large and editorial. Supporting UI remains quiet and compact.

## Photography
Each world needs authentic contextual PNG imagery:
- Personal: people/mobile life.
- Home: household/learning/entertainment.
- Business: PNG professionals/operations.
- Remote: landscape/remote community/infrastructure.
- Government only with approved appropriate imagery/content.

Images should remain clearly visible; avoid dark overlays.

## Motion
Transitions between worlds can use horizontal sliding, masked image change or panel expansion. Keep transition under roughly 500–700ms and allow instant navigation via reduced-motion.

## Plans
Once a world is selected, plan/service presentation can be contextual. Personal sees mobile first; Home sees fixed offers; Business sees solution categories. Still provide global access to all categories.

## Chatbot
Chatbot greeting can adapt its shortcuts to the active world, but the core panel stays fixed bottom-right and predictable. Do not make chatbot state mandatory for navigation.

## Mobile
Use large stacked world tiles or a full-screen swipe carousel with visible tabs. Avoid hidden horizontal scroll. Once a world is selected, show a bottom sheet of services. Persistent utility bar remains accessible.

## Accessibility
- World tabs use proper tablist only if they truly behave as tabs; otherwise use links/buttons.
- Keyboard can switch worlds.
- Selection is never conveyed only by colour.
- One H1 before world headings.
- Skip link to “Browse all services.”
- Images have meaningful alt text.

## SEO
All world service gateways should be present in semantic HTML and crawlable anchors. Do not inject only the chosen world into the DOM. Use clear keyword gateways for Mobile, Home Internet and Business Solutions.

## Performance
No WebGL necessary. Optimize world images carefully because first-screen image payload can grow quickly. Preload only the initial active world; lazy-load the rest after interaction/idle.

## CMS
Model World as a content grouping with title, image, description, primary CTA and references to service items. Editors can adjust featured content without changing the interaction framework.

## Do not do
- Five cards inside a normal hero.
- Make every world look identical except the photo.
- Hide cross-category navigation after selection.
- Introduce green colour themes per world.
- Reuse designs 1–6 content order unchanged.

## Success
This should be one of the strongest client-facing options: visibly new, intuitive, premium enough for management, and flexible across consumer/business audiences.