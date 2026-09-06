# Design 23 — Telikom OS

## Status
Standalone specification for `23.html`. Do not alter earlier concepts.

## Portfolio position
- Gen-Z affinity: **8/10**
- Enterprise / premium: **8/10**
- UX clarity: **9/10**
- PNG identity: **7/10**
- Motion: **6/10**
- Complexity: **6/10**
- Similarity target: **2/10 or lower**

## Core idea
Treat the homepage like a clean operating system for connectivity. The page is modular and live-feeling, but not a dense dashboard. Telikom services appear as purpose-built widgets with different shapes and information densities: a large network story tile, a narrow service-status strip, plan tiles, a self-care task panel, a PNG story module, business workspace and news ticker.

The key difference from previous card-heavy designs is that the widgets form a deliberate system with functional hierarchy rather than repeated equal cards.

## First viewport
No conventional hero banner. The first screen is a composed “desktop” of 5–7 widgets:
- Brand / slogan widget.
- Large primary service/action widget.
- Self Care task widget.
- PNG image/story widget.
- Mobile/Home switcher.
- Business entry widget.
- Network/support status strip.

One widget should dominate 40–50% of the canvas, so the page does not become a uniform bento grid.

## Layout model
Use a responsive editorial grid with named areas, not an auto-fill card grid. Desktop should feel intentionally composed. Tablet simplifies to 2 columns; mobile becomes a priority-ordered stack.

## Suggested page architecture
1. OS workspace opening.
2. Service workspace: Personal / Home / Business selector.
3. Plan comparison module.
4. People / PNG story module.
5. Business operating panel.
6. Technology / remote connectivity module.
7. Self Care and Support workspace.
8. News / announcements feed.
9. Footer.

## Widget types
Use different component families:
- task list;
- full-bleed image tile;
- large typographic tile;
- comparison strip;
- status line;
- mini map/coverage launcher;
- notification feed;
- service switcher.

Avoid six identical rounded rectangles with icon/title/body.

## Palette
- Telikom Blue `#0875C9`
- Mid Blue `#2A87C7`
- Soft Blue `#DFEFF8`
- Background `#F6FAFC`
- Ink `#17374B`
- White `#FFFFFF`
- Line `#CDDDE7`

No green UI accent. Status indicators should use blue/neutral labels unless a real status system requires semantic colours in production.

## Typography
Gibson preferred. Use large editorial headings for dominant widgets and compact UI typography for utilities. Maintain clear distinction between website content and app-like controls.

## Motion
- Widgets can subtly reflow/expand on selection.
- Hover/focus can expose contextual actions.
- Service mode switch changes 1–2 modules, not the entire page.
- No draggable desktop simulation required.
- Reduced-motion uses instant state changes.

## Self Care
Self Care is a first-class widget, not a CTA lost in navigation. Include Top Up, Pay Bill, Buy Data, Balance, Coverage and Support as task rows or tiles.

## PNG identity
The dominant media widget should use high-quality Papua New Guinea imagery and rotate only on user interaction or via calm slideshow controls. Lower story modules connect the OS metaphor to real people and places.

## Business
Give Business a visibly more structured “workspace” widget with solution rows rather than promotional cards. Include enterprise connectivity, voice, hosting, systems and remote connectivity only where approved.

## Chatbot
Chatbot can resemble a system assistant but should be clearly Telikom-branded. Fixed bottom-right, with context-aware shortcuts if practical. Do not present it as AI unless real capabilities exist.

## Mobile
On mobile, the OS grid becomes a deliberate priority stack:
1. brand + quick tasks;
2. service selector;
3. plan/service module;
4. PNG story;
5. business;
6. news/support.
No masonry gaps or unpredictable reading order.

## Accessibility
- CSS grid visual order must not differ confusingly from DOM reading order.
- Widgets have semantic regions/headings.
- Controls are keyboard reachable.
- One H1.
- All task targets 44px minimum.
- Do not use colour alone for state.

## SEO
Render core services as crawlable anchors. Do not hide content exclusively behind widget mode selection. Use a semantic service index in the DOM and appropriate Mobile/Home/Business headings.

## Performance
Moderate. No WebGL. Use CSS Grid, container queries where supported, and small vanilla JS. Load one dominant image eagerly, rest lazily. Keep layout shift low with fixed aspect ratios.

## CMS
Very CMS-friendly if widget contracts are defined. CMS should supply content to widget slots via types such as Promotion, Service Group, Plan Group, Story, News, Utility. The design must tolerate missing optional widgets.

## Must avoid
- Copying Apple/Windows branding literally.
- Making every surface rounded and glassy.
- A dashboard so dense that ordinary customers cannot scan it.
- Reverting beneath the first screen to designs 1–6 section order.

## Success
The page should feel like a coherent digital service system — modern enough for younger users, structured enough for enterprise stakeholders, and clearly different from a marketing landing page.