# Canadian Analytics Engineering — dbt Project

## Identity
- Team: canadian-ae (JustEat Takeaway)
- Repo manages dbt models for customer analytics on BigQuery
- Models live under top-level domain folders in `dbt/models/` (e.g. `cae_customer/`,
  `cae_single_run/`, `skip_topsort/`). New domains are added as new top-level folders —
  never as subfolders of `cae_customer/`

## Stack
- dbt-core 1.8.2 + dbt-bigquery 1.8.1
- Python 3.10 (virtualenv at `venv/`)
- SQLFluff 3.4.2 (BigQuery dialect, dbt templater)
- Pre-commit 4.3.0 with dbt-checkpoint
- dbt packages: dbt_utils, dbt_expectations, codegen, dbt_date

## Required environment variables
- `MORPHEUS__ENV=local`                               # for local development
- `DBT_CUSTOM_DEV_SCHEMA=cae_dev_<first>_<last>`     # developer-specific schema

## Common commands
- Activate venv:    `source venv/bin/activate`
- Install deps:     `pip install -r requirements.txt`
- Install packages: `dbt deps`
- Debug connection: `dbt debug`
- Build model:      `dbt build -s "my_model+"`
- Lint SQL:         `sqlfluff lint dbt/models/`
- Fix SQL:          `sqlfluff fix dbt/models/`
- Lint YAML:        `yamllint .`
- Pre-commit:       `pre-commit run --all-files`

## Model naming conventions
- `stg_<source>_<entity>.sql`  — staging layer (light transformation from source)
- `base_<source>_<entity>.sql` — base layer (deduplication, basic cleaning only)
- `temp_<source>_<entity>.sql` — temporary models (excluded from CI lint checks)
- `_key_<entity_name>`         — surrogate key column, generated via `dbt_utils.generate_surrogate_key()`;
  always underscore-prefixed, never `<entity>_id`
- `_<model_name>.yml`          — properties file, co-located with SQL, one-to-one with model file
- `_<model_name>.md`           — docs file, co-located with SQL, one-to-one with model file

## Model configuration
- Default materialization: `table` with `persist_docs` (relation + columns)
- All models tagged: `team="canadian-ae"`, `table_tier="silver"`
- Schema routing: driven by `MORPHEUS__ENV` via `generate_schema_name.sql` macro
  - `prod`  → `clean_skip_data_lake`
  - `dev`   → `staging_cae`
  - `local` → value of `DBT_CUSTOM_DEV_SCHEMA`
- Data quality test results land in `cae_data_quality` schema
- YAML properties files: must start with `version: 2`; include `data_type:` on every
  column; use `data_tests:` key (dbt 1.8), not `tests:`; yamllint enforces a hard
  150-character line limit — use `>` block scalar to wrap long descriptions

## Quality gates (must pass before every push)
1. `pre-commit run --all-files` — SQLFluff lint, yamllint, dbt-checkpoint hooks
2. Every model must have a paired properties `.yml` file
3. Every model must have ≥ 2 dbt tests
4. No semicolons at end of SQL scripts
5. No hardcoded table names — use `{{ ref() }}` or `{{ source() }}` only

## Git workflow
- Branch must contain ticket ID: `CAE-<number>-short-description`
- Never commit directly to `master`
- PR must link JIRA ticket + pass CI (SQLFluff lint, yamllint, dbt compile)
- CI triggers on changes to `dbt/`, config files, or YAML files

## Off-limits (never modify or delete)
- `target/`                       — dbt build artifacts, auto-generated
- `dbt_packages/`                 — installed packages, auto-generated
- `dbt/models/cae_single_run/`    — archive models, excluded from CI lint
- `logs/`                         — runtime logs

## Rules loaded on demand
- SQL conventions → `.claude/rules/sql-conventions.md` (loads when editing .sql files)
- YAML conventions → `.claude/rules/yaml-conventions.md` (loads when editing .yml files)
- Dimensional model conventions → `.claude/rules/dimensional-model-conventions.md`
