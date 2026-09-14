# Design 42 CSS ownership

Design 42 intentionally uses a small ordered set of stylesheet owners. New work should go into the file that owns the responsibility instead of adding a later override block.

1. `design42-core.css` owns page structure, typography, base components, responsive layout and foundational motion.
2. `design42-ecosystem.css` owns only the current Digital PNG V2 experience and must keep its selectors scoped to `.eco-section`.
3. `design42-components.css` owns later isolated components such as footer social controls and province-laser presentation.
4. `design42-theme.css` owns the approved Design 42 color treatment sourced from `backup/42-2026-09-10-1552-ist`. It should not own spacing, typography or geometry.
5. `design42-chat.css` owns all Ask Telikom presentation and is loaded last because the popup is an isolated overlay.

`42-base.html` owns markup and runtime behavior, not presentation. Historical palette passes, superseded laser runtimes and inline style blocks must not be reintroduced.
