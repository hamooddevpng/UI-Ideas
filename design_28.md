# Design 28 — Nation Connected

## Portfolio position
- Gen-Z: **6/10**
- Enterprise / premium: **9/10**
- UX clarity: **8/10**
- PNG identity: **10/10**
- Motion: **7/10**
- Complexity: **7/10**
- Similarity target: **0/10**

## Core concept
Build the homepage as a chronological/narrative journey showing how connectivity moves through national life: person → home → community → business → remote operations → future technology. Unlike Design 9’s immersive 3D journey, this is an elegant HTML/editorial timeline suitable for production.

## First screen
Large brand statement with a vertical or horizontal timeline beginning at “01 / PEOPLE.” Use visible Telikom logo/slogan and one bright PNG photograph. The timeline itself should be the compositional spine.

## Narrative chapters
1. **People** — mobile communication and everyday data.
2. **Homes** — home internet/voice/entertainment.
3. **Communities** — access and local connection.
4. **Business** — enterprise connectivity, voice, systems.
5. **Remote PNG** — VSAT/satellite services.
6. **Technology** — infrastructure/future-ready positioning.
7. **Support** — Self Care, stores, customer care.

Products are embedded within relevant chapters rather than grouped into a generic marketing block.

## Timeline behavior
Desktop: a persistent chapter index or vertical line tracks progress. Each chapter has distinct layout composition: full image, split story, data matrix, diagram, etc. Do not use the same two-column module seven times.

Mobile: simple vertical timeline with chapter markers and stable reading order.

## Palette
- Telikom Blue `#0875C9`
- Deep `#0B629E`
- Soft `#D3E8F4`
- Background `#F5F9FC`
- Ink `#15364A`
- White `#FFFFFF`
- Timeline `#BFD7E5`

## Typography
Gibson preferred. Numbered chapter labels in compact uppercase; chapter headlines large and editorial.

## Photography
Strong PNG documentary imagery tied to each chapter. Use visible captions where appropriate. Keep photographs bright and authentic.

## Products and plans
Place mobile plan comparison within People, home offers within Homes, enterprise services within Business, VSAT within Remote. Provide a persistent service directory link so users need not consume the whole narrative.

## Motion
- Timeline line fills as user scrolls.
- Chapter marker activates.
- Images can reveal with masks/fades.
- No scroll-jacking or mandatory chapter snapping.
- Reduced-motion keeps the progress indicator static/simple.

## Self Care
Support chapter should be task-first and visually simpler than narrative chapters. Top Up, Pay Bill, Buy Data, Coverage, Stores, FAQs and contact should be immediate.

## Chatbot
Fixed bottom-right and conventional. It can display current chapter shortcuts, but context adaptation is optional.

## PNG identity
Maximum. The sequence itself should tell a nationally specific story, not generic telecom categories. Avoid unsupported claims about exact national reach; rely on approved wording.

## Accessibility
Timeline is decorative enhancement over semantic sections. Users should not need to manipulate the timeline. All sections have headings and links. Keyboard focus jumps normally. One H1.

## SEO
Strong. Each chapter creates natural topical content gateways. Use crawlable service links and appropriate headings. Avoid excessive slogan copy at the expense of service terms.

## Performance
Moderate: images dominate. Use responsive media, lazy loading, explicit sizing. Timeline animation can be CSS/IntersectionObserver. No WebGL.

## CMS
CMS models Chapter content and associated services/stories, but layout variants should be selected from a controlled set so editors cannot accidentally make all chapters visually identical.

## Must avoid
- Repeating the same split layout for every chapter.
- Becoming a corporate-history timeline about company dates; this is a connectivity journey, not Telikom corporate chronology.
- Hiding products until very late in the page.
- Over-dark imagery.

## Success
The homepage should communicate Telikom’s national role through an elegant story structure while remaining practical enough to become a real production direction.