# Datasets Core — Standardized Open Dataset Catalog and Schemas

Datasets Core is a curated, standards-first repository of dataset schemas, metadata templates, and tooling to help teams publish consistent, discoverable open datasets for machine learning, analytics, and research.

SEO summary: open datasets, dataset metadata, data catalog, data governance, dataset schemas, data pipelines, reproducible datasets.

Why this repo exists
- Provide canonical dataset schema templates (CSV/JSON/Parquet) and metadata examples
- Encourage consistent, searchable dataset metadata across projects
- Share best practices for dataset publication, licensing, and citation

Quick links
- Data layout & examples: /data
- Dataset schema & metadata guidelines: /docs/DATA_SCHEMA.md
- Contribution guide: /CONTRIBUTING.md
- Citation: /CITATION.cff

Repository structure
- data/
  - raw/            # Raw input files (kept immutable)
  - processed/      # Cleaned and normalized datasets
  - README.md       # Data directory notes & ingestion checklist
- docs/
  - DATA_SCHEMA.md  # Schema, metadata, examples
- notebooks/        # Example notebooks to explore datasets
- scripts/          # ETL helpers and validation scripts
- .github/          # Issue templates & community files
- README.md         # This file
- CITATION.cff      # Citation metadata
- LICENSE           # Repository license

How to use
1. Inspect docs/DATA_SCHEMA.md for metadata rules and templates.
2. Place your raw dataset into data/raw/<dataset-name>/ and add dataset-metadata.yaml alongside it.
3. Run scripts/validate_metadata.py to ensure schema compliance.

SEO keywords (for README, repo About and metadata)
open data, dataset catalog, dataset metadata, data governance, machine learning datasets, data cleaning, dataset schema, reproducible research, data pipeline

Maintainers & contact
- Hollow House Institute — hollowhouseinstitute (GitHub)
- For issues or dataset requests: use the Issues tab

License
This repository uses the MIT License — see LICENSE
