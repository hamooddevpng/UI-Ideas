# Design 20 — Telikom Command

## Portfolio position
- Gen-Z: **7/10**
- Enterprise / premium: **8/10**
- UX clarity: **10/10**
- PNG identity: **5/10**
- Motion: **5/10**
- Complexity: **6/10**
- Similarity target: **0/10**

## Core idea
Make search/command the homepage. The first question is not “What promotion should Telikom advertise?” but “What did the visitor come here to do?”

A large command field sits at the centre of the page: **“What are you looking for?”** It understands a controlled set of tasks and service keywords: top up, mobile data, home internet, business internet, pay bill, coverage, store, support, careers, news, devices, VSAT.

This can work entirely without AI.

## First viewport
- Telikom logo + slogan prominent.
- Huge command/search field with keyboard shortcut hint on desktop.
- 6–8 common intents below it as text, not cards.
- A quiet PNG photo or network graphic used as supporting context.
- Persistent Self Care / Top Up controls.
- No classic promotional hero.

## Command behavior
Typing filters a curated index and shows results grouped by:
- Do something
- Find a service
- Get support
- Learn about Telikom

Examples:
“data” → Gutpela Mobile Data, Home Data, Business Data.
“pay” → Pay Bill, Self Care.
“remote” → VSAT / satellite / enterprise remote connectivity.

The command system must gracefully fall back to normal navigation if JS is unavailable.

## Page architecture
1. Command/search opening.
2. Top tasks as clean rows.
3. Service directory with audience filters.
4. Featured promotion/news area.
5. PNG connectivity/infrastructure story.
6. Business/enterprise gateway.
7. Self Care and support tools.
8. News / corporate content / footer.

## Visual system
### Palette
- Telikom Blue `#0875C9`
- Deep Blue `#075E9F`
- Light Blue `#E5F4FC`
- Background `#F8FBFD`
- Ink `#132F42`
- White `#FFFFFF`
- Line `#CBDDE7`

### Style
Search-engine / command-palette clarity blended with polished corporate editorial layout. Use whitespace, crisp lines and strong typography. Avoid dashboard density.

## Typography
Gibson preferred. Search field text large (24–36px desktop), but result rows remain compact and scannable.

## Interaction
- Keyboard shortcut `/` or Cmd/Ctrl+K may focus the command input, but never override browser shortcuts improperly.
- Arrow keys move through results.
- Enter follows the selected result.
- Escape closes suggestions.
- Result transitions subtle only.

## Search scope
Prototype uses a local deterministic data index. Production can later connect to CMS/site search. Do not represent it as an AI assistant. The search should tolerate synonyms and misspellings where practical.

## PNG identity
Because the first screen is utility-heavy, add strong PNG identity lower down through one major people/network story and real photography. Avoid making the site look like a generic software search portal.

## Chatbot
Chatbot and command search serve different jobs. Search finds pages/tasks; chatbot provides support. Keep chatbot fixed bottom-right with a conventional interface and avoid duplicating the full command index.

## Mobile
Command field remains the hero. Results become a full-width list. Common tasks render in a 2-column or stacked list. No keyboard-shortcut hint. Keep Top Up and Help reachable without scrolling.

## Accessibility
Treat suggestions as an accessible combobox/listbox pattern if implemented as such. Label the input clearly. Do not rely solely on placeholder text. Search results must be links with descriptive labels. Ensure focus is not trapped.

## SEO
The command interface is not a replacement for crawlable navigation. Render service directory and key links in the DOM. One H1, descriptive headings, canonical/meta/schema work as normal.

## Performance
Lightweight. No 3D. Local index should remain small. Delay noncritical imagery. Search must feel instantaneous on lower-powered phones.

## CMS
Index entries should be generated from CMS/service metadata: title, synonyms, category, URL, description. Editors update content once; search reflects it.

## Do not do
- Turn it into an AI chat experience; that is Design 16.
- Add a giant background image hero behind the search box.
- Hide normal nav.
- Return fake results to non-existent services.
- Overcomplicate filters.

## Success
A customer should reach the right Telikom task in one interaction, while the site looks deliberately unlike the existing marketing-led homepage.