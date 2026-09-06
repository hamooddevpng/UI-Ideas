# Design 21 — PNG Signal Map

## Portfolio position
- Gen-Z: **8/10**
- Enterprise / premium: **8/10**
- UX clarity: **8/10**
- PNG identity: **10/10**
- Motion: **8/10**
- Complexity: **9/10**
- Similarity target: **0/10**

## Concept
Make Papua New Guinea itself the primary navigation and storytelling surface. An interactive, stylized PNG map connects people, services, infrastructure and regional stories.

Important: unless Telikom provides validated geographic network data, the map is an **illustrative service/story map**, not a coverage map. Never imply precise coverage from decorative nodes.

## First viewport
The PNG map occupies most of the screen. Telikom logo + slogan sit clearly at top left. A concise statement sits beside or over an empty region of the map: “One network. Across PNG.”

Map modes/toggles may include:
- People
- Services
- Business
- Remote
- Stories

Coverage is a separate explicit action linking to validated coverage tools.

## Map interaction
Nodes represent content, not unsupported infrastructure statistics. Selecting a node opens a side panel with a story/service and relevant CTA. Different node types use shape/icon differences within the Telikom blue palette.

Provide a list view equivalent for accessibility and mobile.

## Page flow
1. Map hero / service-story explorer.
2. “What do you need?” task shortcuts.
3. Personal / Home / Business service routes.
4. Remote connectivity feature tied to PNG geography.
5. People and community stories.
6. Plans / offers.
7. Self Care / Coverage / Stores.
8. News and corporate updates.
9. Footer.

## Palette
- Telikom Blue `#0875C9`
- Map Blue `#126CA8`
- Water/Soft Blue `#BCDFF2`
- Pale `#EAF6FC`
- Ink `#16354A`
- White `#FFFFFF`
- Map line `#C6DCE8`

No green UI layers. Land can be rendered in pale blue/white contours rather than natural map colours.

## Map visual style
Prefer custom SVG/topographic illustration over generic Google Maps styling for the hero. Use province/island outlines carefully. Avoid inaccurate political/geographic labelling; source any detailed boundaries responsibly.

Signal lines can connect illustrative nodes. Keep them sparse and elegant.

## PNG identity
This concept has the highest PNG-identity target. Use local place/context labels where accurate and approved. Show real photographs inside node panels. Balance national pride with practical service discovery.

## Motion
- Gentle node pulses.
- Signal lines draw on initial load.
- Map can pan/zoom within limits.
- Selected node expands into panel.
- No constant camera movement.
- Reduced-motion freezes nodes and removes path animation.

## Task navigation
Map exploration is optional. A persistent utility area must provide:
Top Up / Pay Bill / Buy Data / Coverage / Support / Find Store.

## Mobile
Do not squeeze the full map. Use a simplified map at top with 3–5 featured pins plus a prominent “Explore by service” list. Selecting a pin opens a bottom sheet. Provide a complete text list below.

## Accessibility
- SVG regions/nodes should be keyboard navigable only if interactive.
- Each node has an accessible name.
- Provide “Switch to list view.”
- Do not rely on spatial position alone.
- Semantic service content appears outside the map.
- One H1.

## SEO
Map content must correspond to crawlable HTML stories/services. Do not make canvas the only source. Use meaningful internal links and keyword gateways for mobile, home internet and business solutions.

## Performance
SVG preferred for the stylized national map. Avoid heavyweight mapping libraries unless actual GIS functionality is required. Lazy-load node photos. Keep animations transform/opacity based.

## CMS
CMS can manage map stories with a controlled location/reference field. Do not allow arbitrary coordinates to create misleading coverage claims. A curated set of node positions is safer for the prototype.

## Chatbot
The chatbot may use the active map mode to offer context but stays fixed bottom-right. It should not cover essential map controls.

## Do not do
- Present decorative pins as proof of service coverage.
- Use a generic map provider as the entire visual identity.
- Force map interaction before task actions become available.
- Add green terrain as a brand colour.
- Turn lower sections into the same six-card grids as older concepts.

## Success
The homepage should feel uniquely Papua New Guinean before the user reads a single paragraph. Geography becomes a meaningful interface rather than background imagery.