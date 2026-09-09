# Design 40: Telikom Essential

## Status
Planning brief only for `40.html`. Do not build the HTML in this run.

This design starts a new three-design family with Designs 40, 41 and 42. All three must use the same underlying homepage structure and roughly the same content model. The difference between them is execution complexity, motion and visual ambition, not information architecture.

## Difficulty level
**Easy**

The goal is not to look cheap or unfinished. The goal is to prove that the researched structure works even with very little visual machinery.

Design 40 should feel calm, fast, clear, modern and intentionally minimalist.

## Core idea
Create the simplest credible Telikom homepage that fully respects the reference research.

The page should feel like a clean national telecom service portal with strong art direction, very little decoration and obvious user pathways.

Think:
- excellent spacing;
- strong typography;
- one clear campaign hero;
- useful actions immediately visible;
- clean service hierarchy;
- bright PNG imagery;
- restrained Telikom blue;
- almost no unnecessary animation.

The design should communicate confidence through clarity rather than effects.

## Non-negotiable shared structure
Designs 40, 41 and 42 must preserve this exact high-level section order.

1. Header / navigation
2. Campaign hero
3. Quick actions
4. Offers / plans
5. Service categories
6. Business and Government
7. PNG connectivity / national impact story
8. Service notices and latest news
9. Help / support / stores
10. Footer

Sub-components may change presentation, but no design in this family should reorder or remove these major sections.

## Why this structure is locked
The modern telecom reference cohort repeatedly uses navigation followed by a hero, then quick actions and commercial offers. PNG public-service references add practical service access, notices, news and institutional information.

This design should therefore feel like a modern consumer telecom product on the surface while still functioning as a serious national service website underneath.

## First viewport objective
At roughly 1440 x 900, the first screen should show or clearly reveal:
- Telikom logo and slogan;
- simple primary navigation;
- one focused campaign message;
- one main CTA;
- at least four useful customer actions;
- a visible support route;
- a visible Business pathway;
- a bright PNG-relevant visual.

The visitor should understand both what Telikom is promoting and what they can do immediately.

## 1. Header / navigation
### Layout
Use a clean horizontal header with generous spacing.

Suggested structure:
- left: Telikom logo and slogan;
- center: Mobile, Internet, Business, Offers, About;
- right: Search, Support, Self Care;
- optional compact store/contact icon or link.

### Behaviour
- sticky after the user begins scrolling;
- no mega-menu in the prototype unless absolutely necessary;
- dropdowns, if used, should be simple and keyboard accessible;
- mobile uses a straightforward drawer.

### Visual treatment
White or very pale neutral background.
Use Telikom blue mainly for active states, Self Care and key interaction emphasis.

## 2. Campaign hero
### Purpose
One strong campaign only.

Do not use an automatic carousel.
Do not overload the banner with multiple offers.

### Composition
Desktop:
- approximately 40 to 45 percent copy area;
- approximately 55 to 60 percent visual area;
- image can be full-bleed within the right side or edge-to-edge with reserved negative space for copy.

Suggested content hierarchy:
1. optional small campaign label;
2. large H1;
3. one short support sentence;
4. primary CTA;
5. optional quiet text link.

### Visual direction
Use bright PNG-relevant photography or approved Telikom campaign imagery.
Avoid heavy blue overlays.
Preserve image clarity.

### Example campaign themes
Use only one in implementation:
- mobile connectivity;
- home internet;
- Starlink / remote connectivity if approved;
- national 4G campaign;
- simple product promotion.

Do not invent performance claims.

## 3. Quick actions
### Purpose
This is the functional layer that makes the hero useful rather than decorative.

### Actions
Use four primary actions:
- Recharge / Top Up;
- Self Care;
- Coverage;
- Support.

Secondary links can include:
- Find a Store;
- Buy SIM;
- Pay Bill;
- Business Enquiries.

### Layout
A simple horizontal row immediately below the hero.
It may slightly overlap the hero edge, but keep the geometry very clean.

Do not imitate the six-equal-box tray from the older reference.
Create clear priority.

### Visual style
Minimal icons, labels and perhaps one short descriptor.
No glassmorphism.
No glowing borders.
No exaggerated shadows.

## 4. Offers / plans
### Purpose
Move directly from actions into commercial content.

### Layout
Use a clean editorial grid with 3 featured offers maximum in the first row.

Each offer should have:
- category label;
- concise name;
- short benefit statement;
- price only if verified content is available;
- CTA.

### Design rule
Avoid making every offer a floating rounded card.
Use strong spacing, dividers and image crops to create variety.

Possible treatment:
- one featured offer occupying half the width;
- two smaller offers stacked or aligned beside it.

## 5. Service categories
### Purpose
Explain Telikom's main service ecosystem without making the visitor search the navigation.

Suggested categories:
- Mobile;
- Home Internet;
- Devices and Routers;
- Enterprise Connectivity;
- Support Services.

### Layout
Use a simple service index or image-and-text rows.

This should feel more like a catalogue or editorial directory than another block of identical cards.

## 6. Business and Government
### Purpose
Make enterprise credibility visible early enough that the homepage is not perceived as consumer-only.

### Layout
Use one wide split section.

Left:
- Business and Government heading;
- short description;
- 3 to 4 solution links.

Right:
- strong enterprise / infrastructure image;
- optional compact feature list.

Potential solution vocabulary:
- Business Internet;
- Managed Connectivity;
- Voice;
- VSAT / remote connectivity;
- Data Centre / Hosting if approved;
- Government connectivity.

Do not invent service availability.

## 7. PNG connectivity / national impact story
### Purpose
Give Telikom a national and human layer.

### Composition
Use one large PNG image plus editorial copy.

Possible message themes:
- connecting communities;
- connecting businesses;
- reaching remote areas;
- supporting national digital infrastructure.

### Design treatment
This should be one of the most visually spacious areas on the page.
Do not turn it into a statistics dashboard unless verified statistics are available.

## 8. Service notices and latest news
### Purpose
Blend telecom content with the practical public-service behaviour observed in PNG reference sites.

### Structure
Two-column desktop layout:
- left: Service Notices / Important Updates;
- right: Latest News.

Service notices should be visually utilitarian and easy to scan.
News can be more editorial and image-led.

### Rules
- no fake outage alerts;
- no fake dates presented as live information;
- prototype content should be obviously placeholder if real CMS content is unavailable.

## 9. Help / support / stores
### Purpose
End the main content with practical resolution paths.

Suggested entries:
- Get Support;
- Find a Store;
- Contact Telikom;
- FAQs;
- Chat / assistant access.

### Layout
Use a simple full-width support strip followed by contact links.

The chatbot can remain as a small fixed control at bottom right.

## 10. Footer
### Content groups
- Personal;
- Business;
- Support;
- About Telikom;
- News and Media;
- Careers;
- Tenders / Procurement if required;
- Privacy and legal;
- social links;
- contact details.

Keep the footer structured and useful rather than decorative.

## Visual system
### Palette
Use a restrained, bright Telikom system.

Suggested tokens:
- Telikom Blue: `#0875C9`
- Deep Ink: `#102B3C`
- Soft Sky: `#EAF6FC`
- Warm White: `#FCFDFE`
- Divider: `#D9E5EC`
- White: `#FFFFFF`

Blue should anchor the brand, not cover every surface.

### Typography
Use a clean sans family compatible with the rest of the repo.
Prefer Gibson if already available through the existing project setup.

Typography hierarchy should do most of the visual work:
- large H1;
- large but restrained section headings;
- short paragraphs;
- compact service labels;
- very readable utility links.

### Shape language
- small to medium border radius only where needed;
- mostly rectangular sections;
- subtle dividers;
- very light shadow use;
- no decorative blobs;
- no excessive pills.

## Motion budget
Design 40 should be intentionally restrained.

Allowed:
- simple hover state;
- subtle image scale on hover;
- smooth anchor scrolling;
- small header transition;
- short fade or translate reveal on first appearance if desired.

Avoid:
- bouncing;
- parallax;
- cursor-following elements;
- continuously moving objects;
- section pinning;
- scroll-jacking;
- large animated gradients.

The page must still look complete with JavaScript disabled.

## Mobile strategy
Mobile must preserve the same structure and hierarchy.

Key changes:
- compact sticky header;
- hero becomes vertical, text first or image first depending on crop quality;
- quick actions become a 2 x 2 grid or horizontal swipe row;
- offer layouts collapse without creating endless tiny cards;
- Business section remains prominent;
- notices remain easy to scan;
- support actions are large touch targets.

The first mobile viewport should still communicate one proposition plus immediate utility.

## Accessibility
- semantic header, nav, main, section and footer landmarks;
- one H1;
- visible keyboard focus;
- minimum 44px touch targets;
- sufficient contrast;
- meaningful alt text;
- no essential information embedded only inside imagery;
- icons always paired with labels for important actions;
- respect `prefers-reduced-motion`.

## Performance target
This should be the lightest page of the three.

Target implementation principles:
- no WebGL;
- no 3D libraries;
- no large animation framework required;
- compressed responsive images;
- lazy-load below-fold imagery;
- avoid video in the hero;
- minimal JS;
- content visible immediately.

## Implementation philosophy for the next run
`40.html` should be buildable as a high-quality static prototype using mostly semantic HTML and CSS with a very small JavaScript layer.

Do not introduce complex animation libraries just because Designs 41 and 42 will use more advanced effects.

## Relationship to Designs 41 and 42
Design 40 establishes the baseline structure.

When building 41 and 42 later:
- section order stays the same;
- content categories stay the same;
- primary task hierarchy stays the same;
- only interaction, visual depth and hero mechanics become more sophisticated.

This lets us compare three levels of execution without confusing structure with styling.

## Must avoid
- looking like a wireframe;
- automatic banner carousel;
- excessive blue surfaces;
- six identical quick-action cards;
- card wall after card wall;
- fake statistics;
- generic international stock imagery;
- hiding Business deep down the page;
- burying Support in the footer;
- animation for decoration.

## Definition of success
Design 40 succeeds if the reviewer can say:

"This is simple, but it already feels like the right Telikom website."

It should prove that the structure, content priority, image direction and typography are strong enough to work without relying on effects.