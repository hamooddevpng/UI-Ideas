# Design 25 — Coverage First

## Portfolio position
- Gen-Z: **6/10**
- Enterprise / premium: **8/10**
- UX clarity: **10/10**
- PNG identity: **9/10**
- Motion: **5/10**
- Complexity: **8/10**
- Similarity target: **0/10**

## Core idea
Invert the typical telecom sales funnel. Before showing a wall of plans, ask the practical question: **“What can I get where I am?”** The homepage leads with a location/coverage discovery experience and then presents relevant service categories.

Important: the prototype must not fabricate coverage results. Without a validated coverage API/data source, the UI should demonstrate the interaction using clearly labelled demo states or route users to the existing coverage resource.

## First viewport
- Telikom logo + slogan.
- Large location/coverage prompt.
- Optional stylized PNG map or geographic image.
- Service type choices: Mobile / Home / Business / Remote.
- Direct Top Up / Self Care / Support actions.
- Clear disclaimer for prototype/demo data if simulated.

No conventional hero banner.

## Primary flow
1. User chooses a service type.
2. User enters or chooses a location.
3. UI shows a clearly labelled result state or directs to validated coverage tool.
4. Relevant services/actions are presented.

A “Skip and browse all services” path is always visible.

## Page architecture
1. Coverage-first discovery.
2. Service results / available pathways.
3. Personal/Home plans.
4. Remote connectivity explanation.
5. Business solutions.
6. PNG network/geography story.
7. Self Care / Stores / Support.
8. News/service updates.
9. Footer.

## Palette
- Telikom Blue `#0875C9`
- Geographic Blue `#106EA9`
- Soft Blue `#D0E7F5`
- Background `#EDF7FC`
- Ink `#16364A`
- White `#FFFFFF`
- Line `#C4D9E5`

## Map language
Use blue topographic contours, province/island silhouettes or a light map texture. Avoid green map styling as a brand treatment. If real mapping is later integrated, keep Telikom UI controls blue and accessible.

## Typography
Gibson preferred. The location question should be simple and large. Results need strong labels and plain language.

## Motion
Minimal: map/location highlight, result reveal, smooth transition between service types. No camera flyovers. Reduced-motion uses instant state.

## Data integrity rules
- Never show fabricated “4G available” or bandwidth values as factual.
- Clearly mark placeholder/demo states.
- Keep coverage claims separated from marketing copy.
- Actual production behavior depends on Telikom-approved network/coverage data or API.

## PNG identity
High by design. Geography is central, and lower sections should use PNG landscapes/communities to explain why Telikom needs mobile, fixed and satellite technologies across varied terrain.

## Business
Business users can choose office/site connectivity, multi-site or remote-site pathways without receiving fake technical recommendations. CTA can lead to Business Solutions or contact/proposal request.

## Chatbot
Chatbot may offer “Need help checking coverage?” but should not answer coverage itself unless integrated with approved data. Fixed bottom-right and clear separation from map controls.

## Mobile
Location prompt stays first. A simple search + service type selector is preferable to a tiny full map. Map becomes optional visual preview; results and actions take priority.

## Accessibility
- Location input has visible label.
- Search suggestions use accessible combobox patterns if implemented.
- Map is not the only means of obtaining information.
- Results announced appropriately.
- One H1.
- High contrast and 44px touch targets.

## SEO
Core service content remains present below the interactive tool, with crawlable gateways for Mobile, Home Internet, Business and Remote connectivity. Coverage tool itself should not hide content from crawlers.

## Performance
If using an illustrative SVG map, keep it lightweight. Avoid loading full map SDK before interaction. Lazy-load mapping library only after user requests detailed map functionality.

## CMS
CMS controls service copy, result CTA language and explanatory content. Coverage data should come from a dedicated approved source, not CMS marketing text.

## Must avoid
- Fake precise coverage.
- Generic hero + small map card.
- Forcing location permissions.
- Asking for GPS access automatically on load.
- Using red/green availability indicators without accessible labels.

## Success
The page should feel practical and uniquely appropriate to PNG’s geography, giving customers a reason for the homepage structure beyond visual novelty.