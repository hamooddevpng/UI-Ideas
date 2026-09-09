# Design 41 - Clean Rebuild from Design 10

## Status
Implemented as `41.html` from a clean Design 10 foundation.

The previous Design 41 implementation and its previous planning brief were deleted before this rebuild.

## Core rule
Design 10 is the visual and interaction skeleton.

Do not patch the deleted Design 41. Do not recreate a separate motion engine. Do not add a second proximity or magnet system.

The intended result is:

> This still feels like Design 10, but now it is unmistakably Telikom PNG.

## Foundation preserved from Design 10

- Manrope for primary UI typography
- DM Mono for technical micro-labels
- Telikom blue around `#0875C9`
- deep ink around `#082d46` / `#102b3c`
- pale technical paper around `#f5f8fb`
- oversized editorial typography
- technical grid texture
- floating glass navigation
- custom cursor on fine-pointer desktop devices
- pointer-follow light field
- organic geometry
- thin orbit and signal-line details
- restrained use of blue
- large statement typography
- one inherited Three.js hero sculpture
- Lenis smooth scrolling
- magnetic button treatment
- one global `data-depth` motion field
- Design 10-style `requestAnimationFrame` interpolation
- proximity-based depth movement
- subtle ambient floating movement

## Motion rules

There is one global depth engine.

New content must use `data-depth` values with meaningful differences, commonly around:

- `-24`
- `-18`
- `-12`
- `-6`
- `+6`
- `+12`
- `+20`
- `+28`

The movement should be smooth, slow, fluid, continuous and clearly visible.

Do not add:

- bounce
- spring overshoot
- rubber-band movement
- snapping
- a second magnet engine
- a second proximity engine
- competing continuous transform writers

Entrance reveal effects and pointer depth are separated so they do not compete for the same transform property.

On touch or coarse-pointer devices, desktop pointer depth is disabled rather than faked.

`prefers-reduced-motion: reduce` disables pointer movement and decorative looping while keeping the page fully usable.

## Locked homepage structure

The high-level order is fixed:

1. Header / Navigation
2. Hero
3. Quick Actions
4. Offers / Plans
5. Service Categories
6. Business & Government
7. PNG / National Story
8. Service Notices & News
9. Help / Support / Stores
10. Footer

No section should move just to make the design look different.

## Section composition target

On desktop, major sections should generally feel like approximately 60vh to 80vh compositions.

The 80vh guideline is a composition constraint, not permission to crush content.

Prefer:

- horizontal compositions
- editorial split layouts
- overlapping layers
- fewer, larger elements
- deliberate whitespace
- strong image aspect ratios

Avoid tiny cards, compressed photography and long vertical stacks.

## Header

Use the official Telikom logo from:

`assets/brand/telikom-logo.png`

Required pathways:

- Mobile
- Internet
- Business
- Offers
- About
- Search
- Support
- Self Care

The header keeps the Design 10 floating glass treatment and becomes slightly more compact after scrolling.

## Hero

Use one strong campaign hero, not an automatic carousel.

Current direction:

- campaign label
- oversized editorial H1
- short support copy
- Recharge / Top Up primary CTA
- Explore Services secondary CTA
- clearly PNG-specific image layer
- inherited Design 10 organic Three.js sculpture
- orbit lines and floating labels at visibly different depths

The hero should feel like separate physical layers suspended in space.

## Quick Actions

Primary actions:

- Recharge / Top Up
- Self Care
- Coverage
- Support

Secondary actions:

- Find a Store
- Buy SIM
- Pay Bill
- Internet Plans
- Service Updates
- Business Enquiries

Prototype controls must respond when clicked. No dead buttons.

## Offers / Plans

Use one large editorial feature offer plus supporting pathways.

Do not invent:

- prices
- data allowances
- percentages
- performance claims
- commercial statistics

Keep commercial copy generic until verified.

Photography should have generous space and sensible crops.

## Service Categories

Use a responsive service index rather than a static grid of telecom cards.

Categories:

- Mobile
- Home Internet
- Business Systems
- Business Data
- Regional / Remote Connectivity

Desktop interaction changes:

- image
- title
- description
- micro-label
- CTA state

The same information must be accessible through click, focus and touch.

## Business & Government

Provide clearly selectable Business and Government states.

Switching state can change:

- heading
- supporting copy
- solution chips
- supporting image

Possible solution labels:

- Business Data
- Broadband
- Voice / SIP
- Hosting
- Remote / VSAT
- Government connectivity

The technical diagram is decorative. It must not imply live network information.

## PNG / National Story

This is the human and emotional section.

Focus on what connectivity means for Papua New Guinea:

- families
- communities
- work
- education
- health
- regional connection
- businesses
- communication across distance

Use clearly PNG-specific imagery.

Avoid foreign flags, foreign military imagery, foreign aid branding and ambiguous international identity.

Do not use `gerehu-market-wide.jpg`.

## Tok Pisin

English remains the primary interface language.

Use only a small amount of contextual Tok Pisin microcopy and mark it with `lang="tpi"`.

Do not scatter local words randomly.

## Service Notices + News

Service notices use expandable rows and explicitly generic prototype language unless information is verified.

News uses calm editorial cards with proper imagery.

The reading experience should not be over-animated.

## Help / Support / Stores

Keep these practical actions obvious:

- Recharge
- Self Care
- Coverage
- Support
- Find a Store

The current composition uses a decorative command-centre / coordinate-field treatment.

Any coordinate visual is decorative and must not imply live store or network data.

## Footer

Use the official Telikom logo.

Footer motion is intentionally calmer so the page visually settles.

## Prototype interaction requirements

Implemented interaction targets include:

- Search opens and closes
- Escape closes overlays
- Mobile navigation opens and closes
- Quick Actions open working prototype interactions
- Recharge opens
- Self Care opens
- Coverage opens
- Support opens
- Service category switching works
- Business / Government switching works
- Service Notices expand and collapse
- Chat / help control opens
- footer and support pathways remain usable

## Accessibility

- minimum 44px targets for key controls
- visible keyboard focus
- semantic buttons for state changes
- semantic links for navigation
- hover content is also available by focus or click
- reduced-motion support
- no fake mouse interaction on touch screens

## Performance

- one Three.js scene only
- no additional WebGL engines
- below-fold photography uses lazy loading
- animation relies mainly on transform / opacity / CSS individual translate
- pointer work is disabled on coarse pointers and reduced-motion mode

Design 42 remains the place for the extreme 3D showcase treatment.

## PNG image sources

PNG-specific image source notes remain documented in:

`assets/design41/PNG_SOURCES.md`

The new 41 implementation does not reuse the deleted Design 41 HTML or its deleted planning logic. The rebuild is based on Design 10 plus this brief.