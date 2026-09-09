# Design 42: Telikom Horizon

## Status
Planning brief only for `42.html`. Do not build the HTML in this run.

This is the hard-complexity member of the Design 40 to 42 family.

It must preserve the exact same homepage information architecture as Designs 40 and 41, while pushing the visual and interaction execution as far as practical for a standalone prototype.

## Difficulty level
**Hard**

This design is intended to be the technical and visual showcase.

It may use advanced JavaScript animation, layered 3D transforms, canvas or WebGL where genuinely useful, rich pointer interaction, complex masks, dynamic hero states and section-specific interaction systems.

The advanced technology must serve the same clear Telikom structure rather than replacing it.

## Core idea
Build the most advanced version of the researched Telikom homepage without changing what the homepage is fundamentally made of.

The structure should stay familiar and useful.
The execution should feel cinematic, interactive and highly crafted.

The page should communicate three things at once:
- Telikom is a modern consumer telecom brand;
- Telikom can deliver sophisticated digital services;
- Telikom is a serious national connectivity provider for PNG.

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

No major section may be moved, removed or replaced by an experimental sequence.

The advanced design challenge is to make each of these same sections feel exceptional.

## Main design principle
**Advanced visuals, stable architecture.**

The user should never have to decode the website just because the animation is sophisticated.

Navigation stays understandable.
CTAs stay obvious.
Content remains semantic.
The user can always scroll normally.

## Hero concept: dynamic campaign stage
Unlike Designs 40 and 41, Design 42 can use multiple banner scenes.

However, this should not behave like a conventional automatic advertising carousel.

### Hero behaviour
Use a user-controlled dynamic campaign stage with 3 primary scenes.

Controls:
- visible scene labels or pagination;
- previous / next controls;
- swipe on touch;
- keyboard operation;
- no mandatory autoplay;
- if autoplay is experimented with, it should stop after interaction and should be disabled under reduced motion.

The user should always know which scene is active.

### Shared hero structure across scenes
Each scene should retain:
- short campaign label;
- one H1 or campaign headline;
- one concise support line;
- one primary CTA;
- optional secondary link;
- a strong visual object or image environment.

Keep text positioning broadly consistent so switching scenes does not feel like loading a different website.

## Hero Scene 1: Pocket Telikom evolved
This scene is inspired by the strongest idea from Design 17, but should be rebuilt as a more mature and cinematic product composition.

### Visual
Use an oversized Telikom phone / digital service device as the hero object.

Possible composition:
- phone appears partly outside the normal grid;
- subtle depth layers behind it;
- bright PNG lifestyle photography or a soft environmental background;
- Telikom app interface visible inside the phone;
- small utility widgets around the phone, used sparingly.

### Interaction
The phone should respond to the pointer:
- restrained 3D tilt;
- soft reflection or light response;
- screen UI subtly changes with selected mini-action;
- device settles back with spring physics.

### App content
Use illustrative, non-personal content:
- Top Up;
- Buy Data;
- Pay Bill;
- Coverage;
- Support.

Do not imply real logged-in account data.

### Transition into / out of scene
The phone can rotate a few degrees and move in depth while text crossfades or slides.
Avoid a full spinning device transition.

## Hero Scene 2: Starlink / remote connectivity
This scene should be visually very different while keeping the same text and CTA structure.

### Background
Use a full-width PNG environment image suitable for remote connectivity, rural infrastructure or open landscape.

Image should remain bright and visible.
Do not cover it with a heavy blue overlay.

### Foreground hero object
Use a Starlink-style satellite dish or approved remote-connectivity hardware visual as a separate foreground object.

Preferred implementation order:
1. real 3D model if a lightweight approved model is available;
2. layered cutout image with CSS 3D transforms;
3. high-quality transparent PNG with perspective transforms as fallback.

### Pointer interaction
The hardware should:
- rotate subtly toward the pointer;
- respond on both X and Y axes;
- move within a tightly controlled range;
- have a separate shadow / base response to reinforce depth;
- slowly settle back after pointer leave.

Do not let the object spin freely.
Do not make it chase the cursor aggressively.

### Signal visual
A restrained signal beam or orbital line may animate in response to the dish direction.

This is decorative only and must not imply real coverage geometry.

### Mobile
Replace pointer tracking with a slow device-orientation-like staged animation only if stable and permission-free, otherwise use a simple entrance and gentle idle pose.

## Hero Scene 3: Enterprise network / national infrastructure
This scene should communicate Telikom's enterprise and national capability.

### Visual direction
Possible composition:
- fibre strands or luminous network lines;
- data infrastructure;
- enterprise building / operations image;
- PNG map silhouette used only as abstract composition, not a live coverage map;
- controlled depth layers connecting infrastructure to locations.

### Interaction
- network paths react to pointer position;
- data nodes brighten sequentially;
- CTA and heading remain stable;
- foreground infrastructure can have subtle depth movement.

Avoid fake network statistics or simulated live traffic data.

## Hero scene transition system
Transitions between scenes are a major quality point.

Desired behaviour:
- background crossfade or mask wipe;
- foreground object exits on a depth path;
- new object enters with coordinated scale and perspective;
- text changes quickly and cleanly;
- scene indicator animates to the active state.

Avoid:
- generic left-right slideshow movement;
- large content flashes;
- full-screen white transitions;
- long transition times.

Suggested full transition duration: 700 to 1100ms.

## 1. Header / navigation
### Structure
Same information architecture as Designs 40 and 41:
- logo + slogan;
- Mobile;
- Internet;
- Business;
- Offers;
- About;
- Search;
- Support;
- Self Care.

### Advanced treatment
The header can react to the active hero scene while preserving contrast.

Examples:
- subtle surface tint changes;
- active nav indicator uses a small signal line;
- header compacts after scroll;
- logo remains stable and readable;
- quick utility controls can open elegant command-style panels.

### Search interaction
Search may open into a polished full-width overlay or command panel, but it must remain a normal accessible search experience.

## 2. Campaign hero
The dynamic three-scene stage described above is the primary technical showcase.

### First viewport acceptance test
Even with advanced animation, the first viewport must expose:
- brand;
- current campaign;
- CTA;
- scene controls;
- at least three customer actions at the bottom edge or immediately below;
- Support;
- Business pathway.

The hero must still earn the scroll.

## 3. Quick actions
### Shared actions
Preserve:
- Recharge / Top Up;
- Self Care;
- Coverage;
- Support.

Secondary actions may include:
- Find a Store;
- Buy SIM;
- Pay Bill;
- Business Enquiries.

### Advanced interaction system
Turn this section into a responsive utility deck.

Possible behaviour:
- cards or tiles respond to pointer depth;
- icons have small physically based motion;
- active tile expands locally without pushing the whole page around;
- selected action can reveal a compact micro-panel;
- hover light tracks inside the tile using CSS custom properties;
- SVG icon paths animate once on interaction.

### Important rule
The quick actions must remain faster to use than they are impressive to watch.

No interaction should delay navigation.

## 4. Offers / plans
### Structure
Same content and hierarchy as Designs 40 and 41.

### Advanced visual direction
Create a high-end product gallery without losing scanability.

Potential approach:
- one large offer stage with image, product object and pricing / CTA;
- supporting offer rail beside or below it;
- selecting a supporting offer morphs the large feature area;
- image background and object layer animate independently;
- offer tabs have a liquid or signal-line active indicator;
- on mobile, the same content becomes a clean swipe rail.

### Product object motion
Devices, routers or SIM graphics can use layered 3D rotation or floating depth.

Do not animate all product cards simultaneously.

## 5. Service categories
### Purpose
Keep the same service taxonomy.

### Advanced interaction concept
Build an interactive service matrix or full-width service index.

Desktop concept:
- left side contains large service names;
- right side is a visual stage;
- hover / focus changes the visual stage;
- each service has a distinct short animation language;
- background typography or signal line changes with active service.

Examples:
- Mobile: handset / signal visual;
- Internet: router / home environment;
- Devices: product stack;
- Enterprise: network grid;
- Support: map / assistance visual.

### Accessibility
All service states must be keyboard focusable and their text content must exist in the DOM independent of visual state.

## 6. Business and Government
### Visual goal
This section should feel like a different scale of Telikom, more infrastructural and enterprise-grade, while still clearly belonging to the same site.

### Advanced treatment
Possible layered composition:
- dark or deep-neutral section for contrast;
- luminous network lines;
- infrastructure image;
- business solution list;
- interactive nodes tied to solution categories;
- perspective panel showing solution architecture.

### Interaction
Hover or focus over Business Internet, Managed Connectivity, Voice, VSAT or Hosting can update the visual system.

Do not present unavailable or unverified products as confirmed offerings.

### Scroll effect
A short local parallax or depth reveal is allowed.
Avoid a long pinned sequence.

## 7. PNG connectivity / national impact story
### Goal
This should be the most emotional section after the hero.

### Advanced visual concept
Create an editorial PNG story with layered photography and signal paths.

Potential composition:
- full-width bright PNG photograph;
- foreground text panel;
- subtle animated connection path;
- image crop shifts as the user scrolls;
- small story markers or captions reveal naturally.

### Optional map motif
An abstract PNG outline can be used as a visual motif.
It must not look like a precise coverage map unless real coverage data is available.

### Depth
Foreground and background can move at slightly different speeds.
Maintain text stability.

## 8. Service notices and latest news
### Purpose
This remains the practical information layer.

### Service notices
Use a sophisticated but calm system:
- status chips;
- expandable rows;
- clear dates;
- optional category filter;
- animated disclosure icons.

Prototype data must be clearly placeholder unless sourced from real content.

### Latest news
Use a premium editorial layout:
- one leading article;
- smaller supporting items;
- image masks;
- typography-led hover transitions;
- optional drag interaction for additional articles.

Do not turn news into a noisy carousel.

## 9. Help / support / stores
### Advanced support stage
This section can become a highly polished assistance hub.

Possible components:
- Support search field;
- Find a Store action;
- Contact Telikom;
- FAQ shortcuts;
- floating assistant / chatbot;
- compact map-like visual if store data is available.

### Chat interaction
The chatbot can expand from a floating orb or button into a layered support drawer.

Use spring animation and backdrop depth.
Keep it accessible and dismissible.

### Store locator visual
If real location data is not integrated, use a generic static visual and normal links rather than fake map pins.

## 10. Footer
### Goal
After an advanced page, the footer should restore calm and certainty.

Use:
- strong column structure;
- logo and slogan;
- Personal;
- Business;
- Support;
- About;
- Careers;
- News;
- Tenders / Procurement if required;
- legal;
- social;
- contact.

### Motion
Only micro interactions.
No large 3D effect in the footer.

## Visual system
### Palette
Use the Telikom brand as the anchor with a broader cinematic range.

Suggested tokens:
- Telikom Blue: `#0875C9`
- Electric Blue: `#21A0F3`
- Deep Navy: `#071D2B`
- Ink: `#102B3C`
- Sky: `#EAF6FC`
- Ice: `#F6FBFE`
- White: `#FFFFFF`
- Signal Glow: use a controlled translucent blue, not a neon page-wide effect.

Hero scenes may temporarily introduce scene-specific environmental tones from their imagery.

### Typography
Typography must remain disciplined even when visuals become complex.

Rules:
- one primary H1 at a time;
- short campaign text;
- large editorial section headings;
- strong contrast;
- no chaotic text animation;
- no illegible outlined body text.

## Advanced technology plan
### Core stack
Preferred prototype architecture:
- semantic HTML;
- modern CSS with custom properties;
- CSS transforms and masks;
- GSAP for coordinated hero and scroll timelines if needed;
- `requestAnimationFrame` for pointer-linked motion;
- IntersectionObserver for activation and cleanup;
- optional Three.js only for the Starlink / hardware scene if a real 3D asset makes the result materially better.

### WebGL rule
WebGL is allowed in Design 42, but only where it creates a visual result that cannot be achieved cleanly with layered DOM / CSS.

The whole site should not become one canvas.

Content must remain normal DOM content.

### 3D asset strategy
Prefer small optimized GLB / GLTF assets.

If an optimized asset is unavailable, use transparent product images with layered perspective rather than blocking the prototype on a heavy 3D model.

### Scene architecture
Treat the hero as a state machine:
- `scenePhone`;
- `sceneStarlink`;
- `sceneEnterprise`.

Each scene has:
- text data;
- visual layers;
- enter timeline;
- idle behaviour;
- exit timeline;
- reduced-motion state;
- mobile state.

This will make the implementation easier to reason about than ad-hoc animation code.

## Section-specific visual systems
Design 42 should not reuse the exact same effect everywhere.

Suggested distribution:
- Hero: dynamic scene + depth;
- Quick actions: tactile utility deck;
- Offers: product morph / feature stage;
- Services: interactive service visual switcher;
- Business: network system;
- PNG story: cinematic photography and signal path;
- Notices/news: editorial utility;
- Support: assistant / command surface.

This prevents the page from feeling like one animation trick repeated ten times.

## Motion choreography
### Page-level rhythm
The user should experience alternating intensity.

Suggested rhythm:
1. high intensity hero;
2. quick, useful actions;
3. polished offers;
4. interactive services;
5. deeper enterprise section;
6. slower emotional PNG story;
7. calm practical notices/news;
8. responsive support hub;
9. calm footer.

Do not keep every section at maximum intensity.

### Timing
Suggested ranges:
- micro interaction: 150 to 300ms;
- spring response: 300 to 650ms;
- scene UI transition: 450 to 800ms;
- full hero scene switch: 700 to 1100ms;
- large image / mask reveal: 700 to 1300ms.

## Pointer-follow system
Use one shared normalized pointer service rather than separate event handlers for every component.

Concept:
- calculate normalized X/Y values once;
- publish as CSS variables or shared JS state;
- each active component maps those values to a small local range;
- pause updates when tab is hidden;
- disable on touch / reduced motion.

This keeps the page performant and consistent.

## Scroll system
Native scrolling must remain intact.

Allowed:
- ScrollTrigger-like timelines;
- local parallax;
- reveal masks;
- section progress values;
- brief sticky compositions if they do not trap the user.

Avoid:
- global scroll-jacking;
- forced scroll snapping;
- very long pinning;
- horizontal scroll as the primary navigation method;
- delayed scroll response.

## Mobile strategy
Mobile should feel designed, not downgraded.

### Hero
- dynamic scenes become swipeable;
- phone scene removes excessive 3D depth;
- Starlink object uses controlled entrance / idle movement rather than pointer following;
- enterprise scene simplifies network layers;
- scene labels remain visible.

### Quick actions
Use 2 x 2 grid or compact horizontal rail with large touch targets.

### Offers
Swipeable product stage.

### Service categories
Accordion / tap states.

### Business
Simplified network visual, no expensive continuous canvas if performance is weak.

### PNG story
Single strong photo and minimal parallax.

### Support
Bottom sheet or full-width drawer.

## Reduced motion strategy
Mandatory.

When reduced motion is enabled:
- all hero scenes remain usable;
- scene switches become crossfades;
- phone and Starlink stop following the pointer;
- 3D idle motion stops;
- parallax stops;
- animated network paths become static;
- support drawer uses short fade / slide only;
- no decorative loops.

## Accessibility
Advanced interaction cannot reduce accessibility.

Requirements:
- keyboard-operable hero scene controls;
- clear focus styles;
- semantic buttons and links;
- ARIA only where needed, not as a substitute for semantic HTML;
- no hover-only information;
- stable text during pointer effects;
- minimum 44px touch targets;
- content order in DOM matches reading order;
- hero canvas or 3D layers marked decorative when appropriate;
- meaningful fallback imagery;
- one clear H1 for the active page context.

## Performance strategy
This is critical because Design 42 can easily become impressive but unusable.

### Performance rules
- lazy-load all heavy below-fold assets;
- load only the first hero scene immediately;
- preload next hero asset after first meaningful paint;
- dynamically import or initialize Three.js only if needed;
- stop animation loops when elements are offscreen;
- use transforms instead of layout animation;
- cap device pixel ratio for canvas rendering;
- compress PNG / WebP / AVIF assets;
- use responsive image sizes;
- avoid giant video backgrounds;
- do not run multiple canvas loops simultaneously;
- disable nonessential effects on low-power / touch devices if performance drops.

### Progressive enhancement
Base page:
- fully readable HTML / CSS.

Enhanced page:
- motion and interactive states.

Advanced enhancement:
- optional 3D / WebGL hero object.

If the advanced layer fails, the page should still look intentional.

## Asset checklist for the implementation run
Before building `42.html`, identify or create:
- Telikom logo / slogan asset;
- PNG lifestyle hero image for phone scene;
- phone device mockup or CSS device shell;
- Starlink / remote-connectivity hardware image or lightweight 3D asset;
- PNG landscape / remote-connectivity background;
- enterprise / infrastructure image;
- offer / product imagery;
- PNG national story photography;
- news imagery or safe placeholders;
- service icons;
- support / store visual assets.

Avoid downloading random unrelated stock visuals just to fill the page.

## Relationship to Design 17
Design 17 proved that the phone can become a central interaction object rather than a decorative mockup.

Design 42 should borrow that principle only for Hero Scene 1.

Do not turn the entire page into the Design 17 app shell.
The broader page structure must remain the new researched structure shared with Designs 40 and 41.

## Relationship to Design 40
Design 40 is the structural baseline.

Every major section in Design 42 should be traceable back to the same section in Design 40.

If a section cannot be mapped directly, the structure has drifted too far.

## Relationship to Design 41
Design 41 adds springy premium interaction.

Design 42 keeps that quality but introduces distinct advanced systems:
- dynamic hero scenes;
- rich foreground object animation;
- optional 3D hardware;
- section-specific state machines;
- deeper visual storytelling;
- stronger progressive enhancement strategy.

## Must avoid
- changing the structure;
- making the hero a generic autoplay carousel;
- WebGL for its own sake;
- free-spinning Starlink hardware;
- cursor effects that make controls hard to click;
- hiding content inside canvas;
- huge video backgrounds;
- fake live network data;
- fake coverage maps;
- fake account data;
- excessive blur and glass everywhere;
- every section being pinned;
- scroll-jacking;
- animation that blocks reading;
- making mobile a stripped-down afterthought.

## Definition of success
Design 42 succeeds if it feels like a premium global telecom campaign site and a practical PNG service portal at the same time.

The ideal reaction is:

"This is clearly the same well-structured Telikom homepage as 40 and 41, but every major section has been crafted to a much higher technical and visual level."

The design should feel advanced because of coordination, depth, interaction quality and section craftsmanship, not because the screen is constantly moving.