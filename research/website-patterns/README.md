# Website Pattern Research

The screenshot inventory is the source of truth for what appears in the atlas. Semantic JSON enriches screenshots with crop boundaries, labels, confidence and structure, but a screenshot is never omitted just because its JSON is pending.

- `taxonomy.json`: shared semantic section names and colors.
- `cohorts/<cohort>/cohort.json`: cohort source folder and metadata.
- `cohorts/<cohort>/sites/*.json`: AI/vision decisions for analyzed screenshots.
- `generated/all-reference-atlas.jpg`: every tracked reference screenshot across all cohorts.
- `generated/<cohort>-atlas.jpg`: cohort-specific atlas, including pending screenshots.
- `scripts/render_website_pattern_atlas.py`: deterministic renderer and statistics generator.

GitHub Actions rebuilds atlases, summaries, transition CSVs and the generated README block whenever the research JSON, renderer or source screenshots change.

Pattern percentages use semantically analyzed sites as their denominator. Inventory coverage and semantic-analysis coverage are reported separately.
