# Website Pattern Research

Semantic website analysis is stored in JSON. Python only validates, crops, counts and composes.

- `taxonomy.json`: global section labels and colors.
- `cohorts/<cohort>/cohort.json`: cohort metadata.
- `cohorts/<cohort>/sites/*.json`: one AI/vision analysis per screenshot.
- `generated/`: deterministic atlas and statistics outputs.
- `scripts/render_website_pattern_atlas.py`: renderer.

Crop coordinates are normalized from 0 to 1, so manifests survive different screenshot heights and later recaptures.

Adding or changing a site JSON triggers the `Rebuild Website Pattern Atlas` GitHub Action. It validates the JSON, resolves crops against the source screenshot, renders the atlas, calculates section prevalence and section-to-section transitions, writes JSON/CSV summaries, and commits the generated outputs back to the repository.
