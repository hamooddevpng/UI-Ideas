# Telikom Page Design Research Standard

This directory is a design-research workspace. It does not implement the Telikom website.

## Evidence threshold

A structural recommendation for a `[Page Design]` task must not be treated as final unless the relevant page study contains at least **15 valid visual references**.

A URL in a manifest is not automatically valid evidence. Captures must be visually checked. Exclude or clearly flag:

- security-verification / bot-wall pages;
- cookie or consent overlays that obscure the page;
- navigation failures / error pages;
- materially incomplete or unloaded layouts;
- captures whose infinite expansion makes section proportions misleading;
- a page that is not actually the intended page type after redirects.

If exclusions reduce a page below 15 usable references, add replacement references and recapture before finalising the recommendation.

## Three evidence layers

### 1. Telecom / direct page-type evidence
Use strong telecom operators and adjacent connectivity providers to study customer flows, product presentation, plan comparison, availability, support, devices, business sales and telecom-specific terminology.

### 2. Papua New Guinea business context
Maintain a broad cohort of major PNG organisations. Use it to study familiar local conventions such as national-purpose storytelling, branch/location discovery, contact expectations, trust proof, careers, corporate information, news and community/CSR content.

Target: at least **15 PNG businesses / major commercial or public-enterprise organisations** in the context pool.

### 3. Papua New Guinea government / public-sector context
Use government, regulators and public institutions to study public notices, document-heavy information architecture, consultations, official contact patterns, service directories, accessibility and institutional trust.

These references are especially relevant to News & Media, About Us, FAQs, Contact and other public-information surfaces.

## Research method

For each page study:

1. Select at least 15 relevant reference pages.
2. Capture full-page desktop screenshots deterministically where possible.
3. Record requested URL, final URL, page title and capture status.
4. Visually inspect every capture.
5. Label semantic sections and interaction patterns.
6. Separate recurring majority patterns from useful minority patterns.
7. Compare global telecom practice with PNG-local business/public-sector expectations.
8. Produce a recommended Telikom section sequence based on evidence, not on a predetermined layout.
9. Preserve Telikom content-parity requirements from the reference implementation.
10. Put the research result, image links and final design handoff into the matching Todoist `[Page Design]` task as comments.

## What to record in each final Todoist research comment

- sample size and exclusions;
- references / cohorts used;
- common section and interaction patterns;
- meaningful PNG-local observations;
- important differences between direct competitors and adjacent local sites;
- recommended section order in arrow format;
- required content / data fields;
- filters, calculators, forms or other interaction states;
- desktop/mobile implications;
- links to the research contact sheets / comparison images;
- unresolved content or asset gaps.

## Scope guardrail

Research work must not be confused with implementation. A `[Page Design]` research task prepares the evidence and design handoff. It does **not** modify the production Telikom frontend unless a separate implementation task explicitly requests that work.
