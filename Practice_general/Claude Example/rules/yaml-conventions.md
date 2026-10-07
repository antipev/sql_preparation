---
paths:
  - "**/*.yml"
  - "**/*.yaml"
---

# YAML Conventions (yamllint + dbt-checkpoint)

## dbt model properties (required structure for every model)

```yaml
version: 2

models:
  - name: stg_source_entity
    description: >
      Staging model for <source> <entity> data.
      One row per <entity>.
    columns:
      - name: _key_entity
        description: Surrogate primary key derived from <grain_columns>.
        tests:
          - not_null
          - unique

      - name: other_column
        description: What this column represents.
        tests:
          - not_null

      - name: day_utc
        description: partition_by column.
        tests:
          - not_null

      - name: ingested_at
        description: Timestamp when data was ingested by the pipeline.
```

## Required fields on every column entry
- `description:` — non-empty; style rules below
- `data_type:` — optional; used in some older models (`data_type: string`, `data_type: date`,
  etc.) but not required in new staging models

## Test syntax
Use `tests:` (project convention). The dbt 1.8 key `data_tests:` is equivalent and used
in some older models — both are accepted; new models use `tests:`.

## File header
Every properties file must start with `version: 2` followed by a blank line.

## Description style
- **Short** (the full line stays ≤ 150 chars): plain unquoted text
  ```yaml
  description: Name of the vendor
  ```
- **Long or multi-line** (would exceed 150 chars): `>` folded block scalar — YAML joins
  continuation lines with a space
  ```yaml
  description: >
    Charged clicks represent a fraction of total clicks to avoid counting
    duplicate or fraudulent interactions.
  ```
- **Preserving newlines**: `|` literal block scalar (rare; use only when line breaks matter)
- **Doc block reference**: `'{{ doc("block_name") }}'` — single-quoted Jinja

## Line length
yamllint enforces a hard **150-character limit** (configured in `.yamllint`).
Any description or value that would exceed 150 chars on a single line must be
wrapped with `>` block scalar. Lines exceeding this limit will fail CI.

## Spacing between columns
Always leave a blank line between every `- name:` block — whether or not it has tests.

```yaml
      - name: vendor_id
        data_type: string
        description: Topsort internal vendor identifier.
        data_tests:
          - not_null

      - name: vendor_name
        data_type: string
        description: Display name of the vendor.
```

## dbt source properties
- Every source table used must be declared in a `sources:` block
- Include `loaded_at_field` on sources where freshness monitoring applies

## dbt-checkpoint requirements (enforced by pre-commit)
- `check-model-has-properties-file` — every `.sql` model needs a matching `.yml`
- `check-model-has-tests` — minimum 2 tests per model (enforced)
- `check-script-semicolon` — no semicolons allowed in SQL files
- `check-script-has-no-table-name` — use `ref()`/`source()` only

## Formatting rules (yamllint)
- 2-space indentation
- No trailing spaces
- Quoted strings only when value contains special characters (`:`, `#`, `{`) or Jinja
- Files excluded from lint: `temp_*` models and `dbt/models/cae_single_run/`
