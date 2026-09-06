# Design 16 — Telikom Buddy

## Portfolio position
- Gen-Z: **9/10**
- Premium: **4/10**
- UX clarity: **10/10 target**
- PNG identity: **6/10**
- Motion: **7/10**
- Complexity: **6/10**
- Similarity target: **0/10**

## Core premise
Invert the normal homepage. Instead of asking customers to understand Telikom’s organisation and then browse sections, start with a conversational task chooser:

**“What do you want to do today?”**

The homepage behaves like a helpful assistant interface but does not depend on real AI to be useful. It can be fully implemented as deterministic intent navigation with optional future chatbot integration.

## First screen
The dominant object is a large command/conversation panel, not a hero photo.

Suggested opening:
- Telikom logo + slogan clearly visible.
- Friendly prompt.
- Quick intent chips: Top Up, Buy Data, Pay Bill, Home Internet, Business, Coverage, Support.
- A text field that can filter/navigate known tasks.
- A secondary PNG image strip or small human story, not the main interaction.
- Fixed chatbot may be visually integrated with the assistant interface but should remain available site-wide.

## Conversation model
The page should support guided deterministic flows such as:
- “I need mobile data” → show plan categories + link.
- “Internet for my home” → home services + coverage CTA.
- “I run a business” → business solution pathways.
- “I’m in a remote location” → satellite/VSAT pathway.
- “I need help” → 1555, FAQs, contact, stores.

Do not claim natural-language AI intelligence unless an actual supported backend exists. Prototype should clearly be a navigation assistant.

## Page architecture
1. Task-first assistant hero.
2. “Popular things people do” utility band.
3. Guided service recommendations / intent results.
4. PNG people story — why connectivity matters.
5. Plans as selectable choices tied to intent.
6. Business and Remote pathways.
7. Coverage/location step.
8. News/service updates.
9. Support and footer.

The structure should feel like a service journey, not a marketing landing page.

## Visual palette
- Telikom Blue `#0875C9`
- Utility Blue `#267FC0`
- Soft Blue `#D9EDF8`
- Background `#F4FAFD`
- Ink `#13374D`
- White `#FFFFFF`
- Divider `#CBDDE8`

No unrelated accent colours.

## UI language
Rounded surfaces are acceptable here because the concept is conversational, but avoid generic SaaS dashboards. Use chat bubbles sparingly; important service results should be structured and scannable.

## Imagery
PNG photography should appear as contextual reassurance, e.g. a family/home image beside the Home recommendation, business professionals beside Enterprise, remote landscape beside VSAT. Do not put random images in every answer.

## Motion
- Assistant prompt can gently type/reveal once, but provide instant text for screen readers.
- Result panels animate in with short fades/slides.
- Intent chips may rearrange based on selection.
- No continuous typing animation.
- Reduced-motion removes transitions.

## Chatbot relationship
This concept already looks conversational, so distinguish two layers:
1. Homepage assistant = deterministic navigation.
2. Fixed chatbot = support/help channel.

Do not create two competing bubbles. The floating chatbot can collapse into a small “Help” button while the hero assistant is visible, then expand after scrolling.

## Mobile
This should be excellent on mobile. Treat the homepage as a guided app-like flow:
- full-width prompt;
- large intent buttons;
- bottom sticky utility sheet;
- results stack vertically;
- no sidebars;
- preserve browser back behavior if steps change.

## Accessibility
- Every intent chip is a real button/link with accessible label.
- The text input has label and suggestions accessible via keyboard.
- Do not trap focus in pseudo-chat.
- Results announce politely via `aria-live` only when necessary; avoid noisy announcements.
- One H1.
- 44px touch targets.

## SEO
Critical service content must exist in the page DOM outside the interactive state so crawlers can understand Mobile, Home Internet, Business Solutions and Support. Do not hide all content behind JavaScript-only steps.

## Performance
No WebGL required. Small vanilla JS state machine is enough. Keep task dataset local/static for prototype. Avoid loading a heavy chatbot SDK until real integration requirements are confirmed.

## CMS
CMS should provide service intents, titles, descriptions, CTAs and associated images. Editors can add synonyms for task search without editing code. Keep commercial plan details separately managed/validated.

## Business fit
Although deliberately youth-friendly, this concept is highly practical because it reduces cognitive load and prioritises Self Care. Enterprise users can answer “I’m looking for business connectivity” and immediately enter a dedicated path.

## Do not do
- Fake an AI model or claim “AI-powered” without backend support.
- Hide normal navigation entirely.
- Make assistant responses long and chatty.
- Use cartoon mascots that undermine Telikom credibility.
- Convert later sections back into the same card grid as designs 1–6.

## Success criterion
A first-time customer should be able to complete or reach a high-value task faster than on a conventional homepage, while management sees a structurally new concept rather than another hero/banner treatment.