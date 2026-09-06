# Design 24 — Guided Connection

## Portfolio position
- Gen-Z: **6/10**
- Enterprise / premium: **8/10**
- UX clarity: **10/10**
- PNG identity: **7/10**
- Motion: **5/10**
- Complexity: **7/10**
- Similarity target: **0/10**

## Core premise
Make the homepage a guided service-selection journey. Many telecom customers do not know Telikom’s internal product names; they know their situation. The design asks a short sequence of human questions and routes them to relevant services.

This is more structured than Design 16 (chat-first) and more guided than Design 20 (command/search). It should feel like a premium adviser or configurator.

## Opening question
First viewport:
**“What do you need to connect?”**
Large choices:
- My phone
- My home
- My business
- A remote location
- I need support

The Telikom logo/slogan and direct utilities remain visible. A “Browse everything” link bypasses the guide.

## Journey steps
Typical flow:
1. Audience / context.
2. Need: data, voice, internet, systems, support.
3. Optional location/usage question only if useful and non-sensitive.
4. Recommended service categories.
5. CTA to plan/service page or contact Telikom.

Do not ask unnecessary personal information. The prototype does not collect or submit data.

## Page architecture
1. Guided selector hero.
2. Recommendation stage.
3. “Or browse by service” fallback index.
4. PNG people/use-case stories.
5. Featured plans/offers.
6. Business/enterprise solutions.
7. Remote connectivity.
8. Self Care/support.
9. News/footer.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Deep Blue `#0665A8`
- Soft Blue `#D8EDF8`
- Background `#F4FAFD`
- Ink `#143349`
- White `#FFFFFF`
- Divider `#C9DDE8`

### Style
Calm, spacious, confident. Large option surfaces may use photography/illustrations but must not become generic cards. Consider a horizontal step line, split panels or large text choices with image previews.

## Typography
Gibson preferred. Questions should be large and conversational. Explanatory copy concise.

## Interaction
- Selection animates the chosen answer forward and brings next question into focus.
- Back button always available.
- Step indicator shows progress.
- Recommendation summary remains visible after completion.
- Browser back should not become confusing; for prototype, internal Back is sufficient without manipulating history.

## Recommendations
Do not pretend to calculate technical eligibility. Recommendations are category-based only unless actual product rules/coverage APIs are later provided. Label examples clearly.

## PNG identity
Each audience option can reveal authentic PNG imagery. Remote and community contexts should be particularly local. Avoid generic global lifestyle imagery.

## Self Care
Users selecting support/task intents should skip the marketing journey and go directly to Top Up, Pay Bill, Buy Data, Coverage, Store Locator, FAQs or 1555.

## Business
Business pathway can branch by need: Internet/Data, Voice, Systems/Hosting, Remote Connectivity, Talk to Sales. Avoid overpromising features not validated by Telikom.

## Chatbot
Fixed bottom-right. The chatbot should not duplicate the wizard. It can offer “Need help choosing?” and link back into the guide or support.

## Mobile
Mobile is naturally suited to the guided model. Use one question per screen/section with large thumb-friendly choices. Keep “Skip / browse all” visible. Recommendation results stack cleanly.

## Accessibility
- Choices are semantic radio-style buttons only if one selection is expected; otherwise normal buttons/links.
- Focus moves predictably after step change.
- Step state announced accessibly.
- One H1.
- No content only available through animated transitions.
- Minimum 44px targets.

## SEO
Because the guide is interactive, all important service categories need a crawlable fallback directory on the same page. Do not let search engines see only questions and JS states.

## Performance
Light/medium. No WebGL. Use a small state machine. Preload only images for the current/next step. Keep interactions instantaneous.

## CMS
CMS manages questions, choices, mappings and recommendation copy through structured content. The design should allow Telikom to refine service mapping without code changes. Product claims/prices live in separately validated records.

## Must avoid
- A long survey.
- Collecting phone numbers/emails in the prototype.
- Claiming exact service availability without integration.
- Making the guide mandatory.
- Turning recommendation results into ordinary repeated product cards.

## Success
A visitor who knows their need but not Telikom product names should reach the correct service pathway with minimal cognitive effort, and management should see a fundamentally different homepage architecture.