# Dimensional Model Conventions

Applies to reference/dimension tables (non-event, non-transactional sources).

## Materialization
- Use `materialized='table'` — never `incremental` for dimension/reference tables
- No `partition_by`, no `incremental_predicates`, no `insert_overwrite`
- No `{% if is_incremental() %}` block in the SQL

## Dedup layer
- Dedup SQL is a bare `SELECT * FROM {{ source(...) }}` — no CTE wrapper, no QUALIFY
- dbt_project.yml `+materialized: view` handles the BigQuery view creation
- Include in `_stg_<domain>_dedup.yml` with `unique_combination_of_columns` test on the natural grain

## Clean layer
- `cluster_by` leading with the highest-cardinality group filter (e.g. marketplace before vendor key)
- No `CAST` on `DATETIME` source columns unless explicit UTC conversion is required downstream
- Surrogate key column order in `generate_surrogate_key` must match `cluster_by` column order

## Primary key post_hook
BigQuery does NOT support named primary key constraints — omit CONSTRAINT name entirely.

- `table` models: single unnamed ADD PRIMARY KEY (table is recreated each run — no DROP needed):
  ```sql
  post_hook=[
      "ALTER TABLE {{ this }} ADD PRIMARY KEY (col) NOT ENFORCED"
  ]
  ```
- `incremental` models: DROP PRIMARY KEY then ADD to handle idempotency across runs:
  ```sql
  post_hook=[
      "ALTER TABLE {{ this }} DROP PRIMARY KEY IF EXISTS",
      "ALTER TABLE {{ this }} ADD PRIMARY KEY (col) NOT ENFORCED"
  ]
  ```

## Foreign keys
- Only add when the FK columns directly and completely match the referenced table's PRIMARY KEY
- Composite PKs (e.g. string_marketplace_id + external_vendor_id) require all columns to be
  present in the referencing model — do not add partial FKs
