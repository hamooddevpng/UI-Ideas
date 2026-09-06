# Design 17 — Pocket Telikom

## Status
Standalone implementation brief for `17.html`. Keep designs 1–16 unchanged.

## Portfolio position
- Gen-Z affinity: **9/10**
- Enterprise / premium: **5/10**
- UX clarity: **9/10**
- PNG identity: **6/10**
- Motion: **8/10**
- Code complexity: **7/10**
- Similarity target: **1/10 or lower**

## Core concept
Design the homepage as if Telikom already had a beautifully mature consumer “super-app,” then enlarge that interaction language onto desktop. The phone is not merely a decorative mockup inside a normal hero; the entire page follows an app-like task model.

The user should feel that Telikom is a modern digital service they can operate, not just a company whose products they browse.

## First-screen architecture
Create a split but non-standard opening:
- Left: large brand statement and a small number of direct actions.
- Right/center: an oversized interactive “Telikom phone” or app surface showing balance, Buy Data, Pay Bill, Top Up, Coverage and Support.
- Behind or around the app surface, use one restrained PNG lifestyle photo to ground the digital UI in real people.
- Large Telikom logo and slogan visible in the header.

The phone UI must be functional enough to change tabs or preview tasks, not a static screenshot.

## Primary interaction model
Users can browse the homepage through app-style modules:
1. Home / account overview.
2. Mobile plans.
3. Home internet.
4. Business gateway.
5. Coverage.
6. Support / stores.

Desktop uses the phone/app as a focal interaction object while supporting standard anchor navigation. Mobile removes the “phone frame” and becomes the app interface itself.

## Page flow
1. App-first opening.
2. Quick action dock rendered as large OS-style widgets.
3. “Your Telikom” plan and service recommendations.
4. Home connectivity module.
5. Business switch / professional mode.
6. PNG stories and network reach.
7. Devices / routers as app catalogue.
8. News / service notices as notifications feed.
9. Support + chatbot.
10. Footer.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- App Blue `#1D82C7`
- Pale Blue `#D5EDFA`
- Background `#F1F9FD`
- Ink `#15354A`
- White `#FFFFFF`
- Divider `#C8DCE8`

### Surfaces
Use app-like surfaces with 14–24px radii, but vary the geometry: balance card, circular actions, list rows, notification strips, full-bleed media. Do not make every item the same card.

### Typography
Gibson preferred. Keep app labels compact and readable. Major section headings can be larger and more editorial to prevent the whole page from looking like a dashboard.

## Motion
- App tab transitions.
- Phone may float/tilt subtly on desktop.
- Widgets can expand into full website sections.
- Use short spring-like transitions sparingly.
- No infinite device rotation.
- Reduced-motion removes tilt and turns transitions into instant state changes.

## Self Care
This concept should have the strongest Self Care storytelling after Design 5, but with a more polished consumer-app feel. Do not expose or imply real account data in the prototype. Example data should be clearly illustrative.

## Business pathway
A visible “Switch to Business” action changes the app shell from consumer tasks to enterprise services: connectivity, hosting, voice, VSAT and business systems. This can be a visual state toggle while maintaining normal links beneath it.

## PNG identity
Use contextual photography behind/around the digital surface and within story/notification modules. The message should be “digital tools built for people in PNG,” not a generic fintech app.

## Chatbot
The floating chatbot can look like an in-app support notification. Fixed bottom-right on desktop. On mobile, integrate it as a persistent Help tab or floating action button above safe-area controls.

## Mobile implementation
Mobile is the hero version, not a fallback:
- Remove external phone bezel.
- Sticky bottom navigation with 4–5 entries.
- Large task targets.
- Content continues as normal scroll below the app overview.
- Ensure browser navigation and accessibility are not replaced by pseudo-native behavior.

## Accessibility / SEO
- App controls use semantic buttons; destinations are links.
- Keyboard can operate tabs and actions.
- Clear focus indicators.
- One H1 outside decorative phone text.
- Service descriptions and links exist in semantic page content, not only inside interactive states.
- Minimum 44px targets.

## Performance
No WebGL. Use CSS transforms and lightweight state management. Avoid embedding video inside the device. Lazy-load below-fold imagery. Use explicit image dimensions and responsive sources.

## CMS
CMS content should feed the same service/plan/news components on desktop and mobile. Do not store content separately inside hard-coded phone markup. Allow promotions and notices to be toggled.

## Must avoid
- A normal hero with a decorative iPhone mockup on the right.
- Copying a banking dashboard aesthetic too closely.
- Fake account balances presented as real user data.
- Hiding normal website navigation behind app interactions.
- Overusing rounded rectangles until it resembles designs 5/8.

## Definition of success
The page should feel like a credible future Telikom digital product ecosystem while remaining a public website. A user should understand within seconds that they can do things, not merely read marketing.