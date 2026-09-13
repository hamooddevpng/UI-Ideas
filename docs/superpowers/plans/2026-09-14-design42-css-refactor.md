# Design 42 CSS Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor Design 42 so visual/component ownership is predictable, historical CSS/JS passes no longer fight each other, and the backup color treatment can be restored from one canonical theme layer without changing layout, content, or interaction behavior.

**Architecture:** Keep `42-base.html` as the functional document, but migrate historical versioned style/script passes into explicit canonical ownership. `42.html` becomes a small branch-aware loader. Canonical theme and chatbot presentation move to external CSS files. A static architecture test prevents new palette/version override piles, and Playwright visual QA compares the refactor against the existing Design 42 screenshots before any intentional color change.

**Tech Stack:** HTML, CSS, vanilla JavaScript, Node.js 20, Playwright/Chromium, GitHub Actions.

**Spec:** User-approved refactor request in the Design 42 workstream, with the untouched backup `backup/42-2026-09-10-1552-ist` as the later color source of truth.

## Global Constraints

- Work only on `refactor/design42-css-cleanup` until review.
- Do not merge to `main` without explicit approval.
- Preserve current Design 42 content, DOM structure, interactions, animations, laser behavior, Digital PNG ecosystem, and popup chatbot behavior during the structural refactor.
- Do not intentionally change colors until the structural cleanup is visually verified.
- After structural parity, restore the backup color treatment through one canonical theme file, not through new inline override blocks.
- Avoid new `!important` declarations unless required to neutralize legacy inline styles during migration; every retained use must be documented in the audit.
- Keep the preview URL compatible with htmlpreview and branch refs.

---

### Task 1: Audit current CSS and script ownership

**Files:**
- Create: `scripts/audit-design42.mjs`
- Create: `qa/design42/refactor-audit.md`
- Create: `qa/design42/refactor-audit.json`
- Create: `.github/workflows/design42-refactor-qa.yml`

**Interfaces:**
- Consumes: `42-base.html`, `42.html`.
- Produces: machine-readable and human-readable inventories of `<style>` and `<script>` blocks, version markers, palette passes, duplicate selector ownership, and `!important` counts.

- [ ] **Step 1: Write the failing architecture test**

Create `tests/design42-css-architecture.test.mjs` that initially asserts the future architecture: external theme/chat CSS files exist, `42.html` contains no inline theme/chat CSS payload, and legacy palette markers are absent from the rendered ownership path.

- [ ] **Step 2: Run the test and verify RED**

Run: `node tests/design42-css-architecture.test.mjs`

Expected: FAIL because the external theme/chat files and cleanup markers do not exist yet.

- [ ] **Step 3: Add the audit script**

The script must read `42-base.html` and `42.html`, enumerate every `<style>` and `<script>` block, capture the first `Design 42:` comment when present, count `!important`, identify blocks containing `palette`, `laser`, `chat`, `support`, `business`, or `quick`, and report selectors declared in more than one style block.

- [ ] **Step 4: Add branch QA workflow**

The workflow must run on pushes to `refactor/design42-css-cleanup`, execute architecture tests/audit, start a local server, capture desktop/mobile screenshots, compare against the committed `qa/design42/latest-*.jpg` baseline using ImageMagick, and upload the audit + screenshots + diff images as an artifact. It must never commit screenshots to `main`.

- [ ] **Step 5: Commit audit/guardrail infrastructure**

Commit message: `test: audit Design 42 style ownership`

---

### Task 2: Make the Design 42 loader branch-aware and small

**Files:**
- Modify: `42.html`
- Create: `assets/design42/design42-chat.css`
- Test: `tests/design42-css-architecture.test.mjs`

**Interfaces:**
- Consumes: sibling `42-base.html`, `design42-ecosystem-v2.html`, and external CSS files from the same branch/ref as `42.html` when viewed through htmlpreview.
- Produces: one deterministic rendered document without hard-coding `main` as the source branch.

- [ ] **Step 1: Add failing assertions for branch-aware sibling resolution**

The test must reject hard-coded `raw.githubusercontent.com/hamooddevpng/UI-Ideas/main/42-base.html` and require a source-root resolver that derives the raw branch/commit from htmlpreview's query URL, with a local-server fallback.

- [ ] **Step 2: Verify RED**

Run: `node tests/design42-css-architecture.test.mjs`.

Expected: FAIL on hard-coded `main` source URLs.

- [ ] **Step 3: Replace `42.html` with a minimal loader**

The loader must: resolve the sibling source root, fetch `42-base.html`, replace the Digital PNG section from `design42-ecosystem-v2.html`, load external chatbot CSS, and render once. It must not embed a large CSS template literal.

- [ ] **Step 4: Move popup chatbot presentation into `assets/design42/design42-chat.css`**

Preserve current floating launcher dimensions, popup sizing, mobile behavior, and page-non-shifting behavior exactly.

- [ ] **Step 5: Run architecture tests and visual QA**

Expected: architecture checks pass for loader/chat ownership; visual diff remains within the configured structural-parity threshold.

- [ ] **Step 6: Commit**

Commit message: `refactor: simplify Design 42 loader and chat styles`

---

### Task 3: Consolidate legacy palette ownership

**Files:**
- Modify: `42-base.html`
- Create: `assets/design42/design42-theme.css`
- Create: `scripts/refactor-design42-base.mjs`
- Test: `tests/design42-css-architecture.test.mjs`

**Interfaces:**
- Consumes: audit output identifying historical palette blocks and their cascade order.
- Produces: one canonical theme file and a base document with obsolete palette passes removed.

- [ ] **Step 1: Extend the test to reject historical palette markers**

Reject blocks named `brighter Telikom palette`, `daylight Telikom palette`, `daylight palette polish`, `balanced daylight palette`, and any other palette blocks identified by Task 1's audit.

- [ ] **Step 2: Verify RED**

Run: `node tests/design42-css-architecture.test.mjs`.

Expected: FAIL while historical palette blocks remain.

- [ ] **Step 3: Implement deterministic migration script**

`scripts/refactor-design42-base.mjs` must remove only audited obsolete palette style blocks, preserving all non-palette structural/animation CSS. It must refuse to write if an expected marker is missing or occurs an unexpected number of times.

- [ ] **Step 4: Build canonical `design42-theme.css`**

First reproduce the current pre-refactor computed visual treatment exactly. Define one `:root` token set and one section-level color owner for hero/header, quick actions, offers, services, Business/Government, PNG story, updates, support, chatbot accents, and footer.

- [ ] **Step 5: Load canonical theme after base CSS**

`42.html` must inject/link `design42-theme.css` as the final theme owner. No historical palette CSS may remain in `42-base.html`.

- [ ] **Step 6: Run architecture + visual parity QA**

Expected: tests pass and screenshots remain visually equivalent to the current baseline except anti-aliasing/animation noise.

- [ ] **Step 7: Commit**

Commit message: `refactor: consolidate Design 42 theme ownership`

---

### Task 4: Collapse superseded versioned component passes

**Files:**
- Modify: `42-base.html`
- Modify: `scripts/refactor-design42-base.mjs`
- Test: `tests/design42-css-architecture.test.mjs`

**Interfaces:**
- Consumes: Task 1 audit groups for province lasers and other clearly superseded versioned passes.
- Produces: only the active implementation for each audited component family.

- [ ] **Step 1: Add tests for superseded component versions**

Require one active province-laser implementation and reject obsolete versions when the audit proves a later version fully supersedes them. Do not remove unrelated experiments without evidence.

- [ ] **Step 2: Verify RED**

Run architecture test and confirm it fails on superseded version markers.

- [ ] **Step 3: Remove audited superseded blocks through the migration script**

Preserve the latest active laser implementation and all IDs/classes it depends on. Remove only blocks shown by the audit to be hidden/disabled or superseded by later versions.

- [ ] **Step 4: Run tests + Playwright interactions**

Verify province lasers still appear, chatbot opens/closes, hero scene switching works, quick actions react, Business/Government interactions work, and Digital PNG ecosystem remains present.

- [ ] **Step 5: Commit**

Commit message: `refactor: remove superseded Design 42 component passes`

---

### Task 5: Restore the approved backup color treatment cleanly

**Files:**
- Modify: `assets/design42/design42-theme.css`
- Create: `scripts/capture-design42-reference.mjs`
- Test: `tests/design42-css-architecture.test.mjs`

**Interfaces:**
- Consumes: `backup/42-2026-09-10-1552-ist` as the visual color reference.
- Produces: one canonical theme matching the backup's rendered colors while retaining the current refactored structure and popup chatbot.

- [ ] **Step 1: Capture backup and refactor reference screenshots in QA workflow**

Render the untouched backup and the refactor at desktop/mobile sizes and save side-by-side/diff artifacts.

- [ ] **Step 2: Record computed reference colors**

Use Playwright to write a JSON snapshot of computed colors/backgrounds/borders for header, hero scenes, quick deck/cards, offers, services, Business/Government, PNG story, updates, support, and footer from the backup.

- [ ] **Step 3: Update only `design42-theme.css`**

Match the reference computed colors through canonical tokens/section rules. Do not modify layout or component markup.

- [ ] **Step 4: Verify visual/color parity**

Run architecture tests and Playwright reference comparison. Review desktop fold, full desktop, and mobile artifacts.

- [ ] **Step 5: Commit**

Commit message: `style: restore Design 42 backup color treatment`

---

### Task 6: Final verification and handoff

**Files:**
- Review all changed files.

**Interfaces:**
- Produces: reviewable refactor branch and preview URL. No merge.

- [ ] **Step 1: Run all architecture tests**

Run: `node tests/design42-css-architecture.test.mjs`

Expected: PASS with zero failures.

- [ ] **Step 2: Run final branch visual QA workflow**

Expected: successful workflow and downloadable screenshot/diff artifact.

- [ ] **Step 3: Compare branch against `main`**

Confirm changes are limited to Design 42 refactor/test/QA files and do not alter unrelated designs.

- [ ] **Step 4: Provide preview and verification summary**

Give the htmlpreview branch URL and explicitly state what was structurally refactored, what intentional visual change occurred (backup colors), and any remaining legacy debt.

- [ ] **Step 5: Keep branch unmerged**

Wait for explicit user approval before merging.
