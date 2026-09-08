# Design 37 - Pick Your Path

## Status
New-round concept specification for `37.html`. This is the most interaction-led direction in designs 35 to 38.

## Portfolio position
- Gen Z affinity: **10/10**
- Enterprise / premium: **8/10**
- UX clarity: **10/10**
- PNG identity: **7/10**
- Above-the-fold utility: **10/10**
- Motion: **9/10**
- Code complexity: **8/10**
- Similarity target vs designs 1 to 34: **0/10 in hero behaviour**

## Core premise
Most telecom homepages decide what to advertise first. This concept asks the visitor what they came for first.

The first viewport is an interactive service selector with four clear paths:

- Mobile
- Internet
- Business
- Help Me

Selecting a path changes the hero content, image, CTA and supporting actions instantly. It is not an auto-rotating carousel. The visitor controls the state.

The result should feel fast, personalised and current while preserving a serious enterprise-grade visual system.

## Why this fits the feedback
The reviewer is judging the banner before scrolling. This concept makes the banner itself useful.

Instead of one static hero trying to satisfy every audience, the visitor can immediately choose what matters to them. That allows the first screen to contain more relevance without becoming visually crowded.

This direction borrows the service-first logic seen across major telecom sites, but pushes it into a more deliberate interactive homepage model.

## First viewport
### Header
Light, minimal and stable across all hero states.

Left:
- Telikom logo + slogan.

Centre:
- Mobile
- Internet
- Business
- Offers
- About

Right:
- Search
- Support
- Self Care

Optional slim top utility:
- Personal / Business
- Contact / Store

Do not duplicate too many links between levels.

### Hero intro
Small label:
**What brings you to Telikom?**

Large H1 in default state:
**Choose your connection.**

Below it, a four-option path switcher.

The options should be large and tactile, closer to navigation tabs / destination boards than small pills.

## Hero states
### State 1: Mobile
Visual:
Young PNG mobile user or product-focused mobile image.

Headline direction:
**Data, calls and plans that move with you.**

Primary CTA:
Explore Mobile

Quick actions:
- Top Up
- View Data Options
- Self Care

### State 2: Internet
Visual:
Modern home / household connectivity or router / broadband context.

Headline direction:
**Bring better connectivity home.**

Primary CTA:
Explore Internet

Quick actions:
- View Internet Options
- Get Support
- Self Care

### State 3: Business
Visual:
PNG business / infrastructure / professional team.

Headline direction:
**Connectivity built around your organisation.**

Primary CTA:
Explore Business

Quick actions:
- Business Internet
- Remote Connectivity
- Talk to Telikom

Only use product names that are confirmed.

### State 4: Help Me
Visual:
Reduce photography and make the interface itself the hero.

Headline direction:
**Let’s get you sorted.**

Primary tasks:
- Top Up / Recharge
- Self Care
- Internet Support
- Mobile Support
- Contact Telikom

This state proves that support is a first-class homepage use case, not a footer afterthought.

## Interaction rules
This is not a carousel.

- No automatic state change.
- No timer.
- No pagination dots.
- No content disappearing before the visitor chooses.
- The default state can be Mobile or an approved campaign state.
- State changes occur only through explicit selection.
- Browser back behaviour does not need to record hero state unless production UX testing supports it.

Transitions should take roughly 250 to 450ms.

## Desktop composition
Use an asymmetric split:
- left 42 to 48 percent: copy + path selector + actions;
- right 52 to 58 percent: image / art direction.

The selected path can also tint a small accent area, but Telikom blue remains the master brand.

A slim bottom bar inside the viewport can show:
- Important Updates
- Latest Offer
- Business Enquiries

Keep the text concise.

## Mobile first viewport
The mobile design is arguably stronger than desktop if executed correctly.

Recommended order:
1. logo / menu;
2. "What brings you to Telikom?";
3. horizontally scrollable four-path selector, with all labels visible enough to understand choices;
4. selected hero headline;
5. selected image;
6. 2 to 3 selected quick actions.

The user should not need to scroll through all four audiences. Only the chosen state displays.

At least one primary CTA and two utility actions must appear before or very near the first scroll boundary.

## Why Gen Z should respond well
The concept behaves more like a modern app than a static brochure:
- immediate choice;
- quick feedback;
- short copy;
- stateful interaction;
- direct task paths;
- mobile-native behaviour;
- no forced linear reading.

The visual style should still be disciplined. Do not decorate the selector with emojis or gamer UI.

## Page architecture after hero
After the visitor scrolls, the page returns to a stable shared content structure. Do not duplicate four different homepages.

1. Interactive Pick Your Path hero.
2. Featured offers / products.
3. "Telikom at a glance" service family overview.
4. PNG connectivity / national role story.
5. Business & Government section.
6. Self Care and support hub.
7. Service Updates / Important Notices.
8. Latest News.
9. Careers / tenders / corporate gateway if required.
10. Footer.

## Featured offers
Use a visual card rail with 2 to 4 offers.

Important:
- no endless carousel;
- desktop should show multiple offers at once;
- mobile can swipe horizontally;
- cards need a clear text alternative and keyboard navigation;
- pricing / product facts must be approved.

Cards may use varied layouts based on product category rather than identical templates.

## Telikom at a glance
Create a simple service map after offers.

Four horizontal rows:
- Mobile
- Internet
- Business
- Support

Each row contains concise sub-links. This provides SEO-friendly, crawlable service discovery even though the hero is interactive.

## PNG identity
Each hero state can show a different aspect of Papua New Guinea:
- Mobile: young everyday connectivity.
- Internet: household.
- Business: professional / enterprise.
- Help: interface-led with small human-support image.

Use approved local photography whenever possible.

Do not use a single generic PNG landscape in every state.

## Government / SOE components
This concept includes official / public-service information without cluttering the hero.

### Important Updates module
A compact list with:
- category;
- date;
- headline;
- status if relevant;
- "View all updates".

### Corporate gateway
Links can include:
- News & Media
- Careers
- Tenders / Procurement
- Corporate Information
- Contact

Only show what Telikom actually maintains.

## Business & Government section
This section should feel especially premium.

Use a wide, dark-ink panel with a strong enterprise image and concise service list.

Headline direction:
**For businesses, government and organisations that cannot afford to disconnect.**

Do not use absolute reliability claims unless approved.

CTA:
Talk to Business

Secondary:
Explore Solutions

## Support hub
Inspired by the usefulness of government / utility service websites, but executed with modern telecom polish.

Possible actions:
- Self Care
- Top Up
- Mobile Help
- Internet Help
- Contact
- Store / location finder if available

Use large rows with icons and plain-language labels.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Ink `#102D3C`
- Mist `#EDF5F8`
- White `#FFFFFF`
- Neutral `#F7F9FA`
- Border `#D4E1E7`

Optional state accents can be subtle derivatives of blue, not unrelated rainbow colours.

### Typography
Gibson preferred.

Key characteristic:
The four path labels should have enough scale to become part of the hero's visual identity.

Use large, short headings and compact supporting copy.

### Geometry
The path selector can use:
- underlined blocks;
- segmented full-width tabs;
- rectangular destination tiles.

Do not use tiny rounded pills.

Image frames can use one bold radius or no radius. Avoid a page full of floating glass cards.

## Motion system
This design needs motion, but motion must communicate state.

Recommended:
- selected path indicator slides into position;
- headline fades / shifts 8 to 16px;
- image transitions with a clean mask or crossfade;
- quick actions update after headline, not all at once;
- hover state provides immediate response.

Do not:
- animate the hero automatically;
- use WebGL just for novelty;
- create long cinematic transitions;
- block input while animation completes.

Respect reduced motion by switching content instantly or with simple opacity.

## Accessibility for stateful hero
Critical requirements:
- path selector uses proper tabs or buttons with accessible state;
- keyboard arrows / tab behaviour is logical;
- selected state is communicated beyond colour;
- content changes are understandable to screen readers;
- focus does not jump unexpectedly;
- every state contains semantic headings and links;
- hero remains useful with JavaScript disabled if feasible, with default content and crawlable links.

## SEO
Because hero states change dynamically, essential service links must also exist in stable HTML outside the interactive state.

- one H1 for the initial page state;
- appropriate headings in static service overview;
- crawlable Mobile / Internet / Business / Support links;
- metadata independent of hero state;
- product / offer schema only with valid current data;
- accessible images and meaningful alt text.

Do not rely on hidden hero-state copy as the only SEO content.

## Performance
Four hero images can become expensive.

Rules:
- preload only the default hero image;
- lazy / deferred load remaining state images;
- responsive AVIF / WebP;
- use low-cost transition effects;
- no video required;
- avoid heavy UI frameworks solely for state management.

## CMS model
Hero paths are structured data.

Each path:
- id
- label
- eyebrow
- headline
- body
- primary CTA
- quick actions
- desktop image
- mobile image
- alt text

The CMS must enforce a maximum copy length to protect first-viewport composition.

## Must avoid
- Looking like four hero slides with tabs added on top.
- Automatic rotation.
- Tiny pill navigation.
- Four completely different art styles.
- Colour-coding paths with unrelated rainbow colours.
- Hiding the Telikom brand beneath the interaction.
- Too much text in each state.
- Fake personalisation based on tracking / inferred user data.
- Support being treated as less important than sales.

## Definition of success
A reviewer should interact with the banner before they even think about scrolling.

The design succeeds when the hero feels like a useful Telikom product interface, not a slideshow, and when each major audience can reach a meaningful path with one intentional click.