# Design 14 — Signal Quest

## Portfolio position
- Gen-Z: **9/10**
- Enterprise / premium: **2/10**
- UX clarity: **5/10**
- PNG identity: **8/10**
- Motion: **10/10**
- Complexity: **9/10**
- Similarity target: **0/10**

## Purpose
This is the gamified exploration concept. It should answer: “What if the Telikom homepage felt like discovering a connected world rather than browsing a corporate catalogue?” It is a boundary concept, not the default production recommendation.

## Core metaphor
The user travels through a stylized PNG network world. Different destinations represent Mobile, Home, Business, Remote, Community and Support. Progress through the world reveals services, people and technology.

The experience must remain grounded in real Telikom tasks. The gamification is navigation language, not a game that forces users to earn access to information.

## Opening scene
Instead of a hero banner, render a large illustrated/3D network landscape or topographic map inspired by Papua New Guinea. A signal path begins at the Telikom logo and branches toward visible destinations.

Immediate escape routes must exist: Top Up, Self Care, Support and “View all services” in a persistent header/HUD.

## Journey nodes
1. Start / Telikom brand.
2. Mobile tower / mobile and Gutpela data.
3. Home cluster / home internet and voice.
4. Business district / enterprise services.
5. Remote island or highland node / VSAT and satellite.
6. Community node / PNG people and stories.
7. Service centre / support, stores and Self Care.

Each node opens a readable HTML panel; the world is only the navigation canvas.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Deep Blue `#055D9C`
- Mist `#CBEAF9`
- Dark Ink `#071E2D`
- Pale Sky `#ECF8FE`
- White `#FFFFFF`

Green must not become a UI accent. If vegetation exists in realistic imagery/3D landscape, it is environmental content, not a brand interface colour.

### Style
Stylized but credible: topographic lines, signal arcs, route labels, translucent blue nodes, subtle atmospheric depth. Avoid cartoon mascots.

## Interaction
Desktop can use scroll or drag to move the camera along a guided path. Users can click directly on visible nodes. A timeline/index allows immediate jumps.

Mobile must switch to a simpler guided scene or illustrated vertical map. Do not run an expensive desktop 3D scene unchanged on low-end devices.

## Motion
This is motion level 10 but motion must be intentional:
- camera glides between nodes;
- signal pulses travel along network paths;
- scene elements parallax subtly;
- panels animate in separately from the world.

Reduced-motion mode should use static node artwork and instant panel changes. The site remains fully useful.

## Content fallback
Under or alongside the interactive world, include a semantic service index in the DOM. Search engines and assistive technologies must not rely on WebGL/canvas.

## Chatbot
Treat chatbot as a “guide” rather than mascot. Fixed bottom-right with simple Telikom branding. It may offer “Take me to Mobile / Business / Remote / Support,” jumping to journey nodes.

## Task shortcuts
Persistent task rail:
- Top Up
- Pay Bill
- Buy Data
- Coverage
- Support
These must bypass the exploratory journey.

## PNG identity
Use PNG geography as a real structural idea. Do not invent precise coverage claims from decorative map nodes. Label the map as illustrative unless actual validated GIS data is integrated.

## Performance strategy
- Progressive enhancement mandatory.
- Load lightweight HTML/CSS first.
- Delay WebGL until after first paint.
- Avoid huge external 3D dependencies where possible.
- Use low-poly geometry and compressed textures.
- Pause rendering when tab is hidden.
- Cap pixel ratio on mobile.
- Provide CSS/illustration fallback if WebGL fails.

## Accessibility
- “Skip interactive journey” link before canvas.
- Full keyboard node navigation.
- Node buttons have descriptive labels.
- HTML panels use semantic headings.
- Avoid motion that can trigger vestibular discomfort; reduced-motion bypasses camera movement.

## CMS
The world can be fixed in structure while content panels are CMS-driven. Do not make editors manage 3D coordinates. A service configuration should map each CMS content type to a predetermined node.

## Must avoid
- Making users scroll through 900vh with no visible way to jump.
- Rendering plan tables or critical text only into canvas.
- Using unvalidated network-status or coverage claims as “game stats.”
- Heavy animation before the logo/nav becomes usable.

## Success
This should be the most exploratory concept in the portfolio and visually impossible to confuse with a normal telecom homepage, while still letting a task-driven user escape to Top Up/Support immediately.