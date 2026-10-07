---
paths:
  - "**/*.sql"
---

# SQL Conventions (SQLFluff — BigQuery dialect)

## Formatting
- 4-space indentation
- Keywords and functions: UPPERCASE (SELECT, FROM, WHERE, JOIN, CAST, COALESCE, etc.)
- Identifiers: lowercase
- Trailing commas in SELECT lists
- UNION on its own new line
- JOINs: indented one level; ON clause indented below JOIN line

## CTE style (`indented_ctes = true` in .sqlfluff)
`WITH` goes on its own line. CTE names are indented 4 spaces under it. CTE body content
is indented a further 4 spaces (8 total). Blank line between each CTE.

```sql
WITH
    source AS (
        SELECT *
        FROM {{ source('...', '...') }}
    ),

    renamed AS (
        SELECT
            col_one,
            col_two
        FROM source
    )

SELECT *
FROM renamed
```

## Aliases
- **Table aliases**: always explicit (`AS` keyword required) — `FROM {{ this }} AS source_sub`
- **Column aliases**: `AS` required **only when renaming or computing** a column.
  Pass-through columns (same name, no transformation) must have **no** `AS` alias.
  ```sql
  -- correct
  col_one,
  CAST(col_two AS STRING)    AS col_two_str,

  -- wrong — redundant alias on pass-through column
  col_one                    AS col_one,
  ```
- **Expression aliases**: always explicit — `SUM(amount) AS total_amount`

## Structure rules
- Prefer CTEs over subqueries for readability
- Subqueries inside JOIN clauses are forbidden
- Reference other models with `{{ ref('model_name') }}`
- Reference source tables with `{{ source('source_name', 'table_name') }}`
- No hardcoded dataset or table names
- No semicolons at end of scripts

## Suppressed rules (do not re-enable without team discussion)
- L016 — line length
- L028 — table reference qualification
- L031 — avoid aliases in FROM/JOIN
- L034 — wildcard column ordering

## BigQuery keyword identifiers
When a column alias clashes with a BigQuery reserved word (e.g. `date`, `week`, `year`,
`time`, `timestamp`), wrap it in backticks:
```sql
day    AS `date`,   -- `date` is a reserved word in BigQuery
col    AS `week`,
```
SQLFluff RF04 fires when a keyword is used as an unquoted identifier — backtick-quoting
is the correct BigQuery fix. Do **not** rename the alias to work around RF04; use backticks.

## Inline suppression syntax
- Suppress one rule: `-- noqa: L042`
- Suppress all rules on a line: `-- noqa`
