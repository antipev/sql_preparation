# Project: Automated XKCD Comics Pipeline (Analytics Engineering)

Repository: [antipev/analytics-engineering](https://github.com/antipev/analytics-engineering/blob/main/README.md)

## Summary

| Element | Summary |
|---|---|
| **Situation** | XKCD has published three comics a week since 2005, covering technology, science, geek culture, and everyday life. Its JSON API exposes every comic, but no automated system collected, validated, stored, cleaned, or documented the archive for trend analysis. |
| **Task** | Build a reliable, version-controlled analytics-engineering platform that ingests every comic, models the archive in tested layers, and documents it so two decades of shifting technology, science, and gaming themes can be analyzed. |
| **Action** | Implemented on one shared platform: Dagster for orchestration, Cloudflare R2 for raw JSON and Dagster state backups, MotherDuck/DuckDB for storage, dbt for staging, intermediate, and mart models, and Cloud Run for delivery. The same platform also runs a second, independent Jaffle Shop domain. |
| **Result** | 3,302 comics ingested and modeled end to end, with matching raw and mart row counts. The public Dagster UI and dbt docs run on Cloud Run in one scale-to-zero container; Cloud Scheduler triggers the monthly run and Litestream preserves state in R2. |

## Full write-up

Architecture, component responsibilities, data lineage, validation, and deployment details: [README.md — Analytics Engineering: XKCD & Jaffle Shop](https://github.com/antipev/analytics-engineering/blob/main/README.md).

## Skills demonstrated

Python, SQL, dbt, Dagster, MotherDuck (DuckDB), Cloudflare R2, Docker, Google Cloud Run, Cloud Build, Cloud Scheduler, Secret Manager, Litestream, schema validation, data testing, and technical documentation.

```mermaid
flowchart LR
  subgraph CR["Runtime - Cloud Run service<br/>runs the container image, scales to zero when idle"]
    N["nginx :$PORT<br/>public entry point and router"]
    N -->|/runs| D["Dagster<br/>UI, GraphQL API and orchestration"]
    N -->|/dbt-docs| DOC["dbt docs<br/>static files built into the image"]
    N -->|/wake| W["wake API<br/>internal control API for runs"]
    SUP["supervisord<br/>keeps all processes running"] -. manages .-> N
    SUP -. manages .-> D
    SUP -. manages .-> W
    SUP -. manages .-> L["Litestream<br/>backs up SQLite state"]
    DBT["dbt runtime<br/>builds and tests data"]
  end

  U["Browser / Cloud Scheduler<br/>people and automated triggers"] --> N
  W -->|"launches / polls runs (GraphQL)"| D
  D -->|"writes raw JSON"| R2_DATA[("Cloudflare R2<br/>raw JSON data zone")]
  R2_DATA -->|"loads raw tables"| MD[("MotherDuck DWH<br/>queryable tables")]
  D -->|"runs dbt"| DBT
  DBT <-->|"builds and tests models"| MD
  D -->|"writes run state"| L
  L -->|"replicates state"| R2_STATE[("Cloudflare R2<br/>SQLite backup zone")]
  MD -->|"mart tables"| MOLLOY["Malloy Publisher / Credible (planned)<br/>reusable metrics and dimensions over the marts"]
  MOLLOY -->|"MCP interface"| AGENT["AI agent (planned)<br/>queries semantic layer"]
```

*`In order to keep costs low for this demo`, the architecture deliberately uses `managed, pay-as-you-go` services `instead of always-on infrastructure`: 1) one Cloud Run container serves the UI, docs, orchestration, and wake API, then scales to zero. 2) Cloud Scheduler wakes it monthly; 3) R2 and MotherDuck `free tiers keep fixed storage cost low`. 4) The Malloy/Credible semantic layer and AI agent consumption are roadmap items, not deployed yet.*

```mermaid
flowchart TB
  A["Always-on VM + 24/7 warehouse<br/>fixed monthly bill ($$$)"]
  B["Scale-to-zero Cloud Run<br/>pay only during the run ($)"]
  C["R2 + MotherDuck free tiers<br/>≈ $0 between runs"]
  A -->|"replace with demo architecture"| B
  B -->|"move storage off compute"| C
  style A fill:#f8d7da,stroke:#b02a37,color:#58151c
  style B fill:#fff3cd,stroke:#997404,color:#664d03
  style C fill:#d1e7dd,stroke:#146c43,color:#0a3622
  linkStyle 0 stroke:#b02a37,stroke-width:2px
  linkStyle 1 stroke:#146c43,stroke-width:2px
```

*Cost path: high fixed spend → pay-per-run compute → minimum idle cost for a demo.*

