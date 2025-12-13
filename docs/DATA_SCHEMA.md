
---

# Dataset Metadata Specification

**Hollow House Institute — Datasets Core**

## Purpose

This document defines the **canonical metadata fields, schema conventions, and validation requirements** for all datasets published in the `Datasets_Core` repository.

Adherence to this specification improves:

* discoverability
* interoperability
* governance clarity
* ethical reuse and auditability

All datasets in this repository are subject to **Hollow House Institute dataset governance and licensing**.

---

## Core Metadata Fields

Each dataset **must** include a metadata file (`dataset-metadata.yaml` or `.json`) containing the following fields:

### Required Fields

* **title** (`string`)
  Human-readable dataset title.

* **slug** (`string`)
  Machine-friendly identifier (lowercase, hyphens only).

* **description** (`string`)
  One to two sentence summary describing what the dataset contains and its intended research use.

* **keywords** (`array[string]`)
  Search and categorization keywords
  *Example:* `["relational-data", "behavioral-signals", "time-series"]`

* **license** (`string`)
  License identifier.
  **Must reference Hollow House Institute dataset licensing.**
  *Example:* `"HHI-DATA"`
  (See `DATASET_LICENSE.md`)

* **version** (`string`)
  Semantic version (`v1.0.0`) or ISO date (`YYYY-MM-DD`).

* **authors** (`array[object]`)
  Each object may include:

  * `name`
  * `affiliation`
  * `orcid` (optional)
  * `github` (optional)

* **source** (`string`)
  Provenance reference (e.g., internal generation, archive reference, or DOI if applicable).

* **schema** (`object` or file reference)
  Column-level schema defining field names, data types, units, and descriptions.

* **temporal_coverage** (`object`)

  ```json
  {
    "start": "YYYY-MM-DD",
    "end": "YYYY-MM-DD"
  }
  ```

* **spatial_coverage** (`string`)
  Scope of coverage (e.g., `"global"`, `"regional"`, or GeoJSON bounding box).

* **citation** (`string`)
  Canonical citation text for this dataset.

---

## Column Schema Example (YAML)

```yaml
- name: observation_date
  type: date
  format: ISO-8601
  description: Date of observation in UTC

- name: value
  type: number
  unit: "USD"
  description: Monetary value expressed in U.S. dollars
```

---

## Supported File Formats

### Metadata

* YAML (`.yaml`, `.yml`)
* JSON (`.json`)

### Data

* CSV
* Parquet
* GeoParquet (for geospatial datasets)

### Schemas

* JSON Schema
* Frictionless Data Table Schema

---

## Validation Requirements

All datasets **must pass validation** prior to release.

Validation checks include:

* Required metadata fields present
* License field matches Hollow House Institute dataset licensing
* Schema matches actual data columns
* No prohibited fields or disallowed data types

Validation may be performed using:

* `scripts/validate_metadata.py`
* Integrated validation hooks in dataset tooling

---

## Best Practices for Discoverability

To improve clarity and responsible reuse:

* Keep titles concise (50–70 characters)
* Lead descriptions with primary subject keywords
* Clearly state:

  * what the dataset contains
  * the context in which it was generated
  * appropriate research use
* Always include a citation and license reference

---

## Examples

Reference implementations can be found in:

```
datasets/<dataset-name>/dataset-metadata.yaml
```

Example datasets illustrate:

* correct metadata structure
* schema definitions
* versioning patterns
* license references

---

## Governance Notice

This specification supports **ethical, non-exploitative dataset publication**.

All datasets are governed by:

* `DATASET_LICENSE.md`
* `LICENSE_INDEX.md`

Use of datasets beyond permitted scope requires explicit authorization from
**Hollow House Institute**.

📧 [contact@hollowhouseinstitute.proton.me](mailto:contact: hollowhouseinstitute@proton.me)

---

