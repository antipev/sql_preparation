# Advanced SQL Notes 
`Advanced SQL Implementing Modern Data Solutions and ML Applications`

## Indexing and Efficient Data Access
Indexes are one of the most fundamental tools for improving SQL query performance
in `traditional databases`. 
An **index is a data structure that allows the database to quickly locate specific rows without scanning the entire table**. 

By indexing columns that are used in JOIN conditions, WHERE filters, or ORDER BY clauses, the query planner can check the index instead of performing a full table scan, often making lookups or filtered queries exponentially faster.

`non traditional datbases` If you work primarily with systems like Snowflake or BigQuery, you won’t be creating traditional indexes at all: these platforms manage data organization automatically. 

Instead, you’ll rely on table partitioning and clustering to achieve similar effects. 

**indexes are still relevant in traditional RDBMSs, whereas cloud native warehouses shift the responsibility to automatic storage management and elastic compute.**

`Redshift` is a columnar cloud data warehouse and avoids traditional indexes just like Snowflake and BigQuery, but it relies heavily on `sort` and `distribution keys`(traditionally required more manual tuning from database administrators) to achieve performance optimization.

## Optimization

BigQuery and Snowflake use cost-based optimizers as well, but their behavior differs
due to their distributed cloud architectures. 

BigQuery does not contain user-facing indexes, so the optimizer focuses on `minimizing data movement by choosing efficient distributed join strategies`. Logical operations such as joins are often implemented using physical techniques like broadcasting a small table to all compute nodes or `repartitioning (shuffling)` data across nodes by join key. Because **shuffles involve network and disk I/O (`Disk Input/Output. It refers to the process of a computer system or database reading data from a storage drive (like an SSD or HDD) or writing data to it`) and can dominate query cost, performance tuning in BigQuery is less about manual hints and more about shaping queries well: **filtering early, keeping one side of joins small when possible, and taking advantage of partitioning and clustering**.

Snowflake works similarly but in the context of virtual warehouses: clusters of compute with local memory and disk. Its optimizer also chooses between broadcast
and repartition joins, while additionally leveraging metadata from micropartitions to
skip unnecessary data automatically. 

In both systems, traditional principles still apply: reading less data is faster than reading more, and smart schema design makes it easier for the engine to do the right thing.

## Antipatterns

### Selecting all columns (SELECT *) unnecessarily

- Always select only the columns you truly need. This reduces I/O, memory usage, and network transfer. It also protects you from bugs if new columns are added (since your query won’t inadvertently start pulling them in).

### Not filtering data early
Failing to include a restrictive WHERE clause or joining overly broad datasets can
lead to huge intermediate results. Always try to filter out irrelevant data as early
as possible in the query. Early filtering means the database processes fewer rows
downstream (joins, aggregations, etc., will have less data to handle).

### Ignoring indexes (or not having the right index)
Another anti-pattern is writing a query in a form that can’t use an index. For example, wrapping a column in a function in the WHERE clause (WHERE DATE(order_date) = '2025-01-01') will usually bypass an index on order_date, forcing a full table scan. 

Similarly, using an OR across different columns (WHERE region = 'EUROPE' OR customer_id = 123) might prevent index use because the condition is not simple. 

Solution: ensure that relevant indexes exist, and write filters that allow those indexes to be used (e.g., use range conditions or equality on raw columns rather than transforming the column). In cloud warehouses, the analog is: use your partition key in filters. 

### Misusing DISTINCT or UNION
Remember that UNION by default eliminates duplicates, which means an implicit sort
operation to compare results. If you know the result sets are disjointed or you don’t
care about deduplication, use UNION ALL (which just appends results). 

The same goes for using DISTINCT as a temporary measure. Sometimes people add DISTINCT to remove duplicates caused by joins without realizing they might be masking an underlying issue (like a missing join condition) and adding a costly sort operation.

### Wildcard searches without full-text indexing
If a certain search such as WHERE name LIKE '%Smith%' is frequent, it shouldn’t be used as an index on name in traditional B-tree indexing, since it is not recommended to rely on a SQL LIKE statement alone.


### RBAR (row-by-agonizing-row) processing
This is a term for doing iterative row-by-row processing in SQL or in the application, which fails to leverage SQL’s set-based power. Aim to let SQL do
work in bulk.


### Not using prepared statements (when executing many similar queries)
If your application is executing the same type of query repeatedly (just with different values), not using prepared statements or parameterized queries is a performance anti-pattern.


## Concurrency and workload isolation

Achieving high performance isn’t just about making individual queries fast; it’s also
about handling many queries concurrently without them competing destructively for resources.

`BigQuery` operates on a serverless architecture that manages compute resources
dynamically through virtual compute units called `slots`.

 - In general, access to more slots lets you run more concurrent queries, and your complex queries can run faster. You cannot manually change the number of slots used by BigQuery to execute queries

In contrast, `Snowflake` uses dedicated virtual warehouses for compute, offering builtin workload isolation. Each warehouse runs independently, so resource contention is eliminated between workloads. 

For example, an ETL job can run on a warehouse size configured to large while reporting queries use a medium warehouse size, ensuring mutual performance stability. If a warehouse receives more queries than it can handle concurrently (based on its size and available CPU), Snowflake can automatically scale out using multi-cluster warehouses, launching additional clusters temporarily to handle the load and shutting them down once demand subsides.

While `BigQuery` focuses on dynamic sharing of compute slots with reservation-based isolation, `Snowflake` provides physical isolation by default and scales through user-defined compute clusters, each model offering different advantages depending on workload patterns and operational goals.


## Architecting SQL-Driven Solutions

A `data pipeline` is a structured sequence of processes that ingests (batch and/or
streaming), transforms, and delivers data from raw sources to its final destination,often a curated dataset consumed by analysts, applications, or ML systems. These
pipelines may include ingestion mechanisms (like file drops, APIs, or message
queues), transformation engines (like SQL, Python, or Spark), and delivery or serving
layers. SQL-driven pipelines follow the same shape but rely primarily on SQL for
transformation and modeling, and often for serving outputs as tables and views.


`Foundational design principles` are what separate ad-hoc SQL scripts from production-grade pipelines. These principles provide the discipline and structure needed to move from “getting it to work” to building pipelines that continue to
deliver value over time. 

These principles include 
- modularity, 
- clear lineage, 
- maintainability,
- idempotency ("retry-safe"), 
- automation, and 
- alignment with business SLAs. 
- `data contracts—formal agreements` between producers and consumers of data that define what the data will look like, how often it will arrive, and what quality standards it must meet. 

Together, these principles shape SQL pipelines that are not only technically correct but that are also resilient to change, transparent to stakeholders, and trustworthy across teams.


`Layering means` splitting your pipeline into clear stages, like these:
- Raw or staging tables
  These mirror the source systems, with little or no transformation.

- Intermediate views or tables
  These apply most of the business logic: cleaning, standardizing, joining, and early aggregations.

- Final tables or data marts
  These are polished, ready-to-use datasets built for reporting, dashboards, or machine learning.

This layered structure makes it much easier to follow what’s happening at each step.
If someone new joins the team, they can quickly understand how the data flows and
where specific logic lives. 


Not every data pipeline needs real-time data, so trying to build for maximum speed
can quickly lead to unnecessary cost and complexity. That’s why it’s important to
work with your stakeholders to define clear `service-level agreements (SLAs)`. These
agreements help you understand exactly how fresh the data needs to be and how reliable it must be, so you can design the pipeline accordingly.

Start by asking the right questions:
• Does the data need to update every hour, or is once per day enough?
• Are there specific times when the data must be available?
• What level of delay or quality issue is acceptable before it becomes a problem?
• What is the data availability SLA from upstream systems?


As data pipelines mature and multiple teams begin producing and consuming data,
it becomes essential to establish clear agreements about the data itself. This is where data contracts come in. A `data contract` is a formal agreement that
explicitly defines the 
- schema, 
- format, and 
- expectations of data exchanged between producers (the team or system providing the data) and consumers (the team or system using the data). **It treats data as a product** with a defined interface, much like an API contract in software engineering


```yaml
data_contract:
  name: customer_orders_contract_v1
  description: >
    Defines the schema, quality, and delivery expectations for customer
    orders data produced by the transactional system and consumed by the
    analytics platform.
  version: 1.0
  producer: "ecommerce_app.orders_service"
  consumer: "analytics_team.orders_pipeline"
  schema:
    table: orders
    primary_key: order_id
    fields:
      - name: order_id
        type: STRING
        constraints: ["NOT NULL", "UNIQUE"]
      - name: customer_id
        type: STRING
        constraints: ["NOT NULL"]
      - name: order_date
        type: TIMESTAMP
        constraints: ["NOT NULL"]
      - name: status
        type: STRING
        allowed_values: ["pending", "paid", "shipped", "canceled"]
      - name: total_amount
        type: DECIMAL(12,2)
        constraints: ["NOT NULL", ">=0"]
  data_quality:
    expectations:
      - no_nulls: [order_id, customer_id, order_date, total_amount]
      - valid_enum: {status: ["pending", "paid", "shipped", "canceled"]}
      - currency: "total_amount must be >= 0"
  monitoring:
    freshness_sla: "Data available by 06:00 UTC daily"
    completeness: "At least 99.5% of transactions per day must be present"
  delivery:
    cadence: "daily batch, delivered by 06:00 UTC"
    storage_format: "Parquet"
    location: "s3://analytics-raw/orders/"
    partitioning: "by order_date (daily)"
  security_and_governance:
    pii_fields: [customer_id]
    handling:
      customer_id: "must be hashed in downstream gold models"
    access_control:
      roles:
        - name: analytics_read
          permissions: ["SELECT"]
        - name: finance_reporting
          permissions: ["SELECT", "EXPORT"]
  lifecycle:
    contract_valid_from: "2025-07-25"
    versioning_policy: >
      Minor changes (e.g. adding nullable columns) allowed with notification.
      Breaking changes require new contract version.
    deprecation_policy: "Deprecated versions supported for 90 days."

```


`Data contracts` shift the data quality paradigm from reactive to proactive. 

**By specifying up front what the data will look like (schema, types, and so on), how often it will be updated, and what quality standards it must meet**, you prevent breaking changes and unexpected surprises downstream. 

As a result, **consumers can build with confidence that the data will conform to the contract**. And if the producer needs to change something, they must version the contract or negotiate updates, rather than simply pushing a change that could break dashboards or models without warning.

`Data contracts` fundamentally move data quality processes to `shift-left`, meaning issues are caught at the source or early in the pipeline rather than by downstream consumers. 

Instead of data engineering teams or analysts discovering that a source system changed a field and now dashboards are broken (a reactive scenario), the contract approach means the producer validates and communicates changes up front. 

This proactive behavior significantly reduces the firefighting mode that many teams find themselves in due to unforeseen data issues.


Exposure configuration in dbt (conceptual example)

```yaml
exposures:
- name: weekly_orders_report
label: Executive Orders and Revenue Dashboard
type: dashboard
url: https://app.powerbi.com/groups/.../reports/...
depends_on:
- ref('mart_sales')
owner:
name: Data Analysts Team
email: analyst-team@yourcompany.com
description: >
Executive dashboard showing weekly order volumes and revenue.
```

This declaration would appear in the docs, showing that the mart_sales model is
used by weekly_orders_report. It means any change to that model can be traced to a
business outcome (governance through impact analysis), and owners can be notified
of changes. Even if this exact YAML isn’t present in the repository, the practice is
clear: we treat reports and data products as code, just like data models.




## Architectural Patterns for Data Pipelines

In `batch processing`, data is collected over a set period, such as hourly, daily, or weekly, and then processed in large chunks. The main trade-off of batch processing is data latency. 

`Streaming pipelines`, on the other hand, process data continuously, often as soon as
it arrives. Instead of waiting to collect data over a period, as in batch processing,
streaming systems handle each new record or small group of records right away. This
immediate processing capability makes it possible to gain near real-time insights,
which is particularly ideal for use cases like live dashboards, fraud detection, or
continuous system monitoring where timely information is critical.

In the SQL world, streaming usually relies on tools that support SQL queries on realtime data. This includes technologies like ksqlDB, Flink SQL, and Spark Structured Streaming.

The biggest advantage of streaming is low latency, as data becomes available to
users almost immediately. But this power comes with more complexity in the
overall solution. Streaming systems need to handle late-arriving data, out-of-order
events, and continuously running queries. Ensuring idempotency (no duplicates) and
exactly-once processing is much harder in streaming than in batch jobs.

`Real-time systems` typically produce outputs almost immediately after events occur. For example, a fraud detection system might evaluate a transaction within seconds of its submission. `Near real-time systems` operate with short but defined delays, such as generating updated metrics every few minutes or recalculating the last hour of activity at regular intervals.



`ETL` - data is transformed before it’s loaded into your system (ETL), 

- In traditional extract, transform, load (ETL), data is extracted from source systems,
transformed using external tools or code, often in Java, Python, or even Spark, and
then loaded in its final form into a database. This approach was common when databases were limited in compute power, and when transformation logic lived mostly
outside the warehouse. 

ETL is still used today, particularly in batch-oriented pipelines and within the batch layer of a Lambda architecture, where transformations are applied before data enters the data platform.
For SQL practitioners, this often meant less direct involvement in the transformation
layer, since most of the heavy lifting happened outside the database. SQL tended to be used only at the very end for loading or reporting, which limited visibility and made logic harder to maintain collaboratively.

- One major drawback is that the raw source data is never fully replicated to the warehouse—if you later need a piece of information that was dropped or changed during the ETL process, you might have to re-extract from the source

`ELT` - data is transformedb after it’s already stored in the warehouse (ELT)? 

- In ELT, raw data is loaded into staging tables or schemas with minimal modification. All transformation logic, such as joins, data cleaning and enrichment, or even aggregations, is then expressed in SQL and executed inside the warehouse. This approach is not only more performant on modern platforms, but it also keeps transformation logic close to the data, making it easier to test, debug, version, and collaborate on.

- By loading data first, you also retain the raw data (Bronze layer)
and can always revisit or reprocess it with new logic. ELT simplifies pipelines by
using the warehouse as the single transformation engine—no need for an external
ETL server for most use cases.

- Streaming transformations can be seen as a real-time extension of ELT/ETL. In
streaming, data is continuously extracted from sources and immediately transformed
on the fly as it’s loaded into a system or as it flows through. There are two flavors: one is stream-first pipelines (such as Kafka → Flink jobs → database) where transformation happens in a streaming processor before final storage—akin to continuous ETL.

- The other is in-database streaming features (such as materialized views that update in near real-time or streaming ingestion with SQL triggers), which blur into ELT, just on a micro-batch scale.

`zero-ETL` and `data sharing` represents a shift in data architecture by minimizing or eliminating data movement between systems. **It enables operational data to become available in an analytical platform, such as a data warehouse or lakehouse, with minimal manual pipeline code.**

- Instead of building and maintaining traditional extraction and load jobs, developers configure a connection (sometimes called an integrated sync or zero-ETL bridge) and focus on writing SQL transformations directly in the destination system.

- A concrete example is **the concept of lakehouse systems** that combine features of
data lakes and warehouses, or products like Azure Cosmos DB and Synapse Link, or
Snowflake’s external table integrations, where data from one system is queryable in
another with minimal setup. 


Similarly, `data sharing` is a pattern where data is directly and securely shared across accounts or organizations, often within the same cloud data warehouse ecosystem, without copying or duplicating the data. 

- An example is Snowflake’s data sharing feature or Databricks’ Delta Sharing protocol. In these setups, consumers query the shared data directly from the provider’s platform using SQL, as if it were native to
their own environment.
This model allows for fine-grained access control and eliminates the need for pipeline development or file-based transfers. A single dataset can be shared with multiple external users, systems, or teams, each receiving access only to what they’re authorized to see.

- Data sharing is relevant for ensuring consistency (everyone sees the same “single
source of truth” data, rather than multiple copies that could diverge) and for efficiency (avoiding large data transfers and storage duplication).

- Both zero-ETL and data sharing shift **the emphasis from building pipelines and toward declarative, SQL-driven access**. In practice, this means **SQL becomes the primary interface: with zero-ETL, transformations happen directly in the warehouse**;
with data sharing, external datasets can be queried in SQL without ever moving or
duplicating them.

```
-- BigQuery federated query from MySQL
SELECT *
FROM EXTERNAL_QUERY(
'my-mysql-connection',
'SELECT id, created_at FROM orders WHERE created_at >= NOW() - INTERVAL 1 DAY'
);
```

## Data Mesh and Data Products

`Data mesh` the approach to organizing data architecture (and data
teams) that treats data as a product, emphasizes domain ownership of data, provides
a self-service data infrastructure, and implements federated governance across the
organization. 
In a data mesh, responsibility for data is decentralized: each domain or business
unit (for example, Sales, Marketing, Finance) owns its data pipelines and datasets
as products, delivering them to others in the company who need them. 

`Data as a product` means those teams treat their datasets with the same care and quality as a software team treats a customer-facing product, with clear documentation, quality assurances (tests, contracts), and an interface for users, most commonly through SQL queries but also via APIs or data shares when needed. **Consumers of a data product are like customers: they should have a good experience using the data, and their needs drive the product features.**


- The need for strong governance and standardized infrastructure becomes
greater as you decentralize. The ultimate goal is to enable faster innovation (teams
can move quickly with their own data) without sacrificing consistency and quality
across the company.


## Architectures for Scalability

A traditional relational database is a monolithic system. Storage, compute, and query
execution all live within the same engine, sharing the same physical resources. When workloads grow, the primary scaling strategy is vertical scaling by adding more CPU cores, more RAM, or faster storage to a single machine.
This system can work well for moderate growth, but eventually it hits limits in both
hardware and budget.

From a SQL practitioner’s perspective, much of the optimization work focuses on
squeezing maximum performance out of this single engine, which often involves
indexing to speed up table lookups, partitioning and carefully
managing query plans.

```
Example 3-2. Indexing a frequently filtered column to speed up table lookups
-- Indexing a frequently filtered column to speed up lookups
CREATE INDEX idx_orders_order_date ON orders(order_date);
-- Range partitioning a large table to improve pruning in queries
CREATE TABLE orders_2024 PARTITION OF orders
FOR VALUES FROM ('2024-01-01') TO ('2024-12-31');
```


`Cloud native data platforms` - Storage, compute, and query execution are decoupled so each can scale independently.
This shifts the scaling model from constrained to elastic: keep all historical data
in low-cost storage, spin up compute clusters only when needed, and run multiple
workloads without them competing for the same resources.


Cloud native systems approach this differently, allowing you to isolate workloads by
allocating dedicated compute resources:
- • In Snowflake, spin up a separate warehouse for BI dashboards so reporting
queries never slow ingestion jobs.
- • In BigQuery, assign workloads to a dedicated slot reservation, guaranteeing
throughput without contention.


## Layered Architecture: Separating Storage, Transformation, and Orchestration

A layered architecture separates the concerns of 
- data ingestion, 
- storage, 
- transformation, 
- orchestration, and 
- consumption, 
serving as a clear example of how to design a modular and maintainable data pipeline. 

A layered architecture allows teams to develop, maintain, and troubleshoot each part of the pipeline independently, while still contributing to a cohesive, end-to-end system.

### Data Ingestion

No matter how the data is ingested, the goals are always the same:
• All data should be delivered completely, with no loss or duplication.
• Important metadata like timestamps and primary keys should be kept intact.
• The process should handle errors, schema changes, or temporary source outages.
• The result should be cleanly structured and ready for the next stage of processing,
supporting, for example, downstream SQL transformations.

The ingestion layer is not responsible for applying business rules or cleaning the
data. It should avoid implementing complex transformation logic, such as filtering,
enrichment, joins, or aggregations. The goal is to make raw data accessible and
queryable (structured tables or partitioned files) so SQL-driven logic can take over
cleanly in downstream layers.

### Storage and processing
This layer is where data is persisted and your SQL queries are executed. It supports
everything from lightweight filtering to complex joins, aggregations, and modeling
steps, but with a focus on infrastructure-level execution. This is where performance
matters: materialization strategies, partitioning, and clustering directly impact how
efficiently queries run and scale.

Storage systems typically evolve through different levels of maturity—raw, refined,
and curated—based on how the data is processed and organized. While terminology
varies, a common and intuitive model to describe this evolution is the `medallion architecture`.

`Bronze (raw)`
- Unchanged data as it was ingested, ... typically schema-aligned but unfiltered, and they are often kept in an immutable state to serve as a reliable source of truth. 

`Silver (refined)`
- Data that has been cleaned, conformed, and made consistent. This stage may
handle nulls, correct types, and introduce joins across systems. Silver datasets
serve as trusted, standardized foundations for analytical work, preserving enough
detail for exploratory and ad hoc analysis before business-facing aggregation
occurs in the Gold layer.

`Gold (curated)`
- Highly refined, aggregated, and business-facing datasets, such as KPI tables
or metrics ready to feed dashboards and machine learning models. Gold data
reflects key business definitions and is often governed more tightly. It represents
curated, business-defined narratives designed for consumption across reporting
tools, executive dashboards, and operational decision-making.


Treat this layer as both storage and compute, especially in cloud platforms where
these concerns are separated internally. Even if the transformation logic lives in the next layer, it’s worth noting that `the storage and processing layer` is what makes that logic possible. This is where your models are materialized, your indexes (if applicable) are leveraged, and your queries are optimized for performance. 

A poorly organized storage layer can quickly turn a clean pipeline into a bottleneck. Conversely, a well-managed warehouse or lakehouse enables clean modular transformations and consistent delivery of data products downstream.

### Transformation and modeling

Once data is ingested and stored in a queryable format, the next step is to transform
it into structures that are **usable, interpretable, and aligned with business needs.** It’s not just where SQL is executed, but where logic is written, versioned, and maintained. **The transformation layer is about logic and structure, not infrastructure.**

Transformations are broken down into stages, which makes pipelines easier to test,
debug, and extend.

- In the `staging layer (stg_)`, raw inputs are cleaned and standardized. `Intermediate models (int_)` apply business logic, for example, combining orders with customer or payment data, and prepare enriched records for downstream use. The `final layer` includes curated outputs, such as fct_revenue_per_customer, which aggregates revenue by customer, or rpt_product_sales_summary, which provides product-level sales reporting.

#### Transformation patterns

The principles in mind:
1. Clear separation of concerns
Isolate business rules into dedicated models.

2. Modularity
Build small, composable steps rather than one large SQL file.

3. Reusability
Abstract common logic (like currency conversions or user segmentation) into
shared models.

4. Testability
Write tests for assumptions like uniqueness, null constraints, or value ranges.

5. Traceability
Use comments, documentation, and naming conventions to make logic easier to
audit

#### SQL as a modeling language.
Best practices include the following:
• Using CTEs to structure logic
• Avoiding overly nested subqueries when unnecessary
• Applying consistent naming conventions
• Annotating logic with comments for clarity
• Breaking long queries into logical components
• Materializing intermediate datasets when appropriate to optimize performance,
manage resource usage, or reuse results across multiple downstream steps

#### Orchestration and scheduling
The role of orchestration:
coordinating the moving parts of a SQL-based system so that everything flows in a
controlled and predictable manner.

**Orchestration transforms a pipeline from a collection of queries into a functioning system. It defines how each piece fits together: which models depend on which, when they should run, how they’re triggered, and what to do if something goes wrong. It turns static SQL into an operational flow that the business can rely on.**


`Time-based schedules` trigger jobs at fixed intervals, such as every hour, every
night at midnight, or every Monday at 8 a.m. This approach works especially well
for batch pipelines or business reporting cycles that follow a predictable cadence.


`Event-driven schedules` are more dynamic. Instead of relying on the clock, they
respond to specific signals, such as a new file appearing in cloud storage, a webhook
from an upstream system, or the successful completion of a previous step.
These schedules are particularly useful in streaming or near-real-time scenarios,
where fresh data may arrive at irregular intervals and **speed matters more than predictability**.

Orchestrators track the outcome of each task, maintain logs of what ran and when, and provide context when things go wrong. If a job fails or runs longer than expected, the orchestrator gives you the tools to diagnose and respond.

#### Consumption layer
The consumption layer is the last mile of your data pipeline, the point where all previous layers, from ingestion to transformation, are finally put to work. This is where data moves from systems to people, from structured models to strategic decisions. If the upstream pipeline is the factory, the consumption layer is the storefront: the place where value is realized and trust is either reinforced or lost.

In modern SQL-driven platforms, **this layer connects directly to the outputs of your transformation layer, most often the curated Gold models described in the medallion architecture**.

- While business-facing dashboards and reports should rely only on curated models, other users, like data scientists and analytics engineers, may work directly
with intermediate models, especially when those models contain enriched or denormalized data useful for exploration or machine learning. What matters most is that access is intentional, documented, and aligned with how stable each model is expected to be.

**Best practices for the consumption layer**

1. Expose only curated models
    Limit access to Gold-layer outputs. This reduces the risk of stakeholders building reports on incomplete or inconsistent data.

2. Enforce semantic alignment
    Use semantic layers or standardized naming conventions to help nontechnical users query data consistently.

3. Treat reporting as a product
    Every dashboard is an interface to your models. Version it, test it, and monitor usage.

4. Avoid tight coupling
  Decouple dashboards and apps from volatile upstream logic. If a transformation changes, you shouldn’t have to fix 10 dashboards.

5. Document with intent
  Make it easy to understand what each model or table is for, and what it isn’t.Clear ownership and documentation are key.






#### Continuous integration and continuous delivery for SQL pipelines

`Continuous integration (CI)`
Automatically validates changes when they’re committed, running tests to catch issues early

`Continuous delivery (CD)`
Ensures that, once changes pass validation, they’re deployed quickly and consistently
to staging and production environments


CI/CD workflow steps for SQL/dbt pipelines

| Step | Purpose | SQL/dbt-specific actions |
|---|---|---|
| Version control commit | Track all changes in code and logic | Commit SQL models, macros, and tests with clear, descriptive messages |
| Automated linting and style checks | Enforce consistency and readability | Run SQLFluff or dbt-style checks |
| Automated unit and integration tests | Catch issues early | Use `dbt test` or custom SQL queries |
| Build and compile models | Ensure models compile and dependencies resolve | Run `dbt compile` to detect syntax or reference errors |
| Deploy to staging | Validate in a safe environment | Trigger orchestrated runs against staging datasets |
| End-to-end and regression tests | Confirm stability before production | Compare staging outputs to production baselines |
| Approval and promotion | Controlled release process | Require peer review and stakeholder sign-off |
| Deploy to production | Apply changes to live datasets | Orchestrator triggers production jobs after approval |
| Post-deployment monitoring | Detect issues quickly | Use observability tools for anomalies and performance checks |


#### Infrastructure as Code (IaC) in scaling and for data platforms
One enabling technology for managing scalable architectures is Infrastructure as Code
(IaC). IaC is the practice of defining your infrastructure (servers, databases, network configs, and so on) in machine-readable configuration files or scripts, rather than via manual setup or clicking through consoles. In a data platform context, this means database instances, warehouses, pipelines, and related resources are defined in code and can be deployed or updated automatically.

IaC tools, like Terraform, AWS CloudFormation, Azure ARM templates

```
# Terraform configuration for BigQuery defining a dataset and access roles in a single block
# Provider omitted for brevity
resource "google_bigquery_dataset" "sales_ds" {
dataset_id = "sales"
friendly_name = "Sales Analytics Dataset"
description = "Dataset for sales reporting and analytics"
location = var.gcp_region
delete_contents_on_destroy = true
access {
role = "READER"
user_by_email = "analyst-team@mycompany.com"
}
access {
role = "WRITER"
user_by_email = "analytics-ci@my-gcp-project.iam.gserviceaccount.com"
}
}
```


## Common Architectural Anti-Patterns

### Tight Coupling Between Pipeline Components
Tight coupling happens when downstream processes rely on upstream tables that
were never intended for direct consumption, such as dashboards querying staging
or intermediate models. When internal structures change, these dependencies break
silently, slowing development and reducing trust.

### Monolithic “All-in-One” SQL Scripts

Putting the entire pipeline—ingestion, transformation, and output—into a single
SQL script may seem simpler at first, but it quickly becomes fragile.
Debugging is harder, intermediate results are invisible, and one failure forces a full rerun. Parallel execution becomes impossible.

A better approach: break transformations into modular SQL models with explicit
dependencies and materialized checkpoints. Tools like dbt enable partial reruns,
parallelism, and targeted optimizations, making the pipeline more maintainable and
faster to evolve.

### Missing Lineage and Monitoring
Without lineage, you don’t know who depends on what. Without monitoring, you
may not even know something broke until a user complains.

### Over-Coupling to Specific Technologies
Relying heavily on vendor-specific SQL extensions or proprietary features can lock
you into a single platform, making migration or integration costly.

### Not Designing for Evolution
Architectures that assume fixed inputs, logic, or scale will eventually break as requirements evolve. Pipelines that can’t reprocess historical data or easily add new sources are the first examples that something wasn’t correctly designed.

A better approach: parameterize pipelines for backfills, keep sources configurable,
and design transformations to accommodate change. Flexibility today is resilience
tomorrow.

### Skipping Tests for SQL Models
Without automated tests, errors in joins, aggregations, or data assumptions often slip into production unnoticed, eroding trust in the platform.

A better approach: implement tests directly in SQL or via frameworks like dbt.
Validate uniqueness, null constraints, and business rules at every stage, not just the final outputs. Testing protects the integrity of your SQL pipelines and catches issues before they reach consumers.

### Ignoring Governance and Security
Granting broad, uncontrolled access may be convenient in the short term, but it risks
compliance breaches and inconsistent data handling as the platform grows.

A better approach: apply role-based access controls, column-level security, and masking for sensitive fields. Separate sensitive datasets into dedicated schemas and automate retention policies. A secure architecture protects the business and builds trust.

## Traditional SQL Data Modeling Techniques

Three cornerstone techniques that have dominated the industry in the past few decades: 
- 3NF normalization, 
- the star schema (and its variant, the snowflake schema), 
- and the recent, popular approach of one big table (OBT) denormalization.

1. `3NF normalization`
In practical terms, each fact is stored once in one place, rather than duplicated across multiple records.

The core 3NF principle: **all data about a given subject, such as departments,is kept in a single location**. The result is a model with minimal duplication,
reduced data redundancy, and higher information density, ensuring the same information is never stored in multiple places.

A schema designed in 3NF provides a very strong foundation for data integrity.
Each piece of information is stored in exactly one place, which dramatically reduces
redundancy and ambiguity.

That cost becomes visible as soon as you start querying across entities. The primary
drawback of 3NF is that related data is spread across multiple tables, which means
queries frequently require joins. These joins are not just harder to write and reason about; they also introduce performance overhead, particularly when tables are large or poorly indexed.

Highly normalized schemas can also become `cognitively expensive`. An analyst or
data scientist must understand the full relational structure to answer even basic
analytical questions. 
In reporting or exploratory analysis, this friction adds up quickly.

Queries become longer, harder to maintain, and more prone to subtle errors.
While modern databases are quite good at optimizing joins, **the fundamental reality remains: normalization optimizes for write correctness, not read convenience**.

As a result, normalized schemas often struggle to meet the performance and usability
expectations of analytics workloads.

Normalized models are ideal for transactional systems (OLTP), where data is frequently inserted, updated, and deleted, and where consistency is not negotiable.

----
However, when the goal shifts from operating on data to analyzing it. At that
point, **the normalized model is typically transformed into a more analysis-friendly shape, such as a star schema or a wide denormalized table**. These derived models
trade some redundancy for faster queries and simpler mental models, while the
original 3NF schema continues to serve as the authoritative source of truth.

**In practice, successful data platforms rarely choose between normalization and denormalization. Instead, they use 3NF as a stable core and build analytical models on top of it**.
----

2. `Dimensional Modeling: Star Schema for Analytics`

A star schema organizes data around two core concepts: facts and dimensions.
At the center lies a fact table that stores measurable, quantitative values, such as
amounts, counts, or durations. 

Surrounding the fact table are dimension tables that provide descriptive context for the measures.

Visually, the structure resembles a star: a central fact table connected to several dimension tables via foreign keys, each representing a different analytical perspective.

Each dimension is typically stored in a single, denormalized table. In practice, a star schema requires only one level of joins between the fact table and each dimension, significantly reducing query complexity and improving performance for BI workloads.

Analytical queries become shorter, more readable, and easier to reason about. Analysts do not need deep knowledge of the underlying operational schema. Fewer joins typically result in faster execution, especially in column-oriented analytical databases.

Another major advantage is consistency through shared dimensions. The same dimension (conformed dimensions) table can be reused across multiple fact tables.

A snowflake schema is a variation of the star schema that introduces additional
normalization within the dimensions. Rather than storing all dimension attributes in
a single table, some attributes are extracted into related subdimension tables, creating chains of joins that branch outward from the fact table. Visually, this structure resembles a snowflake rather than a star.

3. `One Big Table: The Wide Denormalized Table Approach`

This approach places all relevant analytical data into a single, wide table, denormalized to the extreme. OBT enables rapid insights by having all necessary data in one place, instantly accessible: for example, quickly determining margin by channel during a promotion period. 

Conceptually, an OBT fully flattens a star schema, joining the fact table with all of its dimensions in advance so that measures and descriptive attributes coexist as columns.

**the core idea is to shift complexity from query time to data preparation time**.

Analytical queries require only scanning and filtering a single table, with no joins required. All necessary attributes are present as columns. This makes queries shorter, easier to write, and simpler to understand.

This design aligns extremely well with the execution model of modern columnar analytical databases. Systems such as BigQuery, Snowflake, and Redshift are optimized
to efficiently scan large tables, reading only the columns required by a query. In this environment, avoiding joins can significantly reduce query latency. 

In practice, performance benchmarks have shown that a single denormalized table can outperform an equivalent star schema by a substantial margin, precisely because it avoids runtime join costs. 

This reality has led some platforms to offer pragmatic advice: **simply denormalize aggressively when performance matters most**.

OBT cons:
- `Redundancy`: The same descriptive values are repeated across many rows, complicating
updates and change management. 
  For example, if a department name changes,that update must be propagated everywhere it appears. 
  
- `Managing historical correctness` is especially challenging. Storing point-in-time (as-was) versus current-state (as-is) values is a key decision. 

- OBTs also tend to grow very wide, often containing dozens or even hundreds of columns.
  This can make them difficult to understand, document, and evolve. 
  
- Adding a new attribute sourced from a different system may require recomputing or backfilling large portions of the table. While incremental processing and partitioned backfills can mitigate this cost, the underlying reality remains: OBTs are less flexible in the face of schema change.

- There are also governance and compliance considerations. Regulations such as GDPR
require that personal data be correctable and, in some cases, removable. In a heavily
denormalized table, identifying and updating all instances of an individual’s data
can be cumbersome.

- It limits reuse and semantic consistency across an organization. 
For example, a conformed Customer dimension ensures “VIP” has a consistent meaning.
In contrast, **independently built OBTs may encode business rules differently, leading to fragmentation**. Dimensional models with conformed dimensions provide a shared foundation that OBTs alone cannot guarantee.

In practice, OBTs are best treated as delivery artifacts rather than foundational models. They are often used as **downstream marts** tailored for specific tools, dashboards, or performance-critical workloads.This makes OBTs especially useful. They
also serve as quick wins, helping teams meet immediate analytical needs while more
structured models are developed.

A normalized or dimensional warehouse serves as the system of record, while one or more OBTs are materialized on top for convenience and speed. Analysts benefit from querying the OBT for simplicity, while engineers maintain the underlying models for flexibility and governance.



## Knowledge Graphs and Semantic Modeling

Traditional models struggle with metadata sprawl, schema drift, and complex cross-domain joins. By resolving these pain points, semantic models and knowledge graphs offer more flexibility and clarity, making them increasingly compelling for modern databases.

Unlike **a relational model, which organizes information in tables, or a star schema, which still relies on predefined tables and relationships**, **a knowledge graph represents data as a network of entities and relationships**. 

In this network, 
- entities are the nodes (thing: box, circle) and 
- relationships are the edges (connection: raod, cable).

`a knowledge graph is a collection of interlinked facts.`
It organizes information as a graph, consisting of nodes and edges. 

The nodes represent entities, such as real-world objects or abstract concepts. 
The edges show the relationships between these entities. 

In this context, `a fact is an atomic assertion about entities or their relationships`. **This differs from the fact table in data warehousing, which typically contains quantitative data**. 
Instead, **a knowledge graph is a semantic data model that connects entities and relationships within a unified network**.

```
# A knowledge graph query (Cypher)
MATCH (alice:Person {name: 'Alice'})-[:memberOf]->(dept:`Department`)
RETURN dept;
```

important implications:
1. Relationships are treated as first-class data, not as secondary artifacts.

2. Query structures naturally reflect real-world connections.

For many data modelers, a common frustration is dealing with endless join
rewrites in traditional relational databases, since trying to accurately reflect
complex relationships often leads to cumbersome, convoluted SQL queries. Recognizing
these headaches, graph databases offer a welcome relief. 

By enabling more intuitive data modeling, they save time and reduce complexity in query development, making the design process less stressful and more efficient.

3. Complex, join-heavy questions become simpler and more intuitive, which enables more efficient data retrieval and faster decision-making.

For instance, what traditionally required a cumbersome 12-table join operation
in a relational database can often be reduced to a simple two-hop traversal in a
graph database. This dramatic simplification not only saves time but also makes
complex queries more accessible and easier to manage.

4. Performance depends on the depth of relationships traversed, not on table size.

Think of it like a subway ride: the more stations you stop at, the longer your
trip takes. Similarly, in a graph database, the deeper the relationship, the more
computational effort required. This approach results in optimized operations
and can reduce computational costs, making it efficient for queries focusing on
deeply interconnected data.


However, it is important to remember that graph queries do not always outperform
SQL in every scenario.

---
To transition smoothly from current graph models to future
Web Ontology Language (OWL) work, it is essential to focus on data mapping
and vocabulary alignment, bridging today’s practices with tomorrow’s ontology. This
initial step ensures that the shift from tables to graphs is manageable, not mysterious.
---

## Semantic Models and Ontologies
A semantic model goes beyond capturing just the structure of data; it encodes the
meaning behind it. Instead of focusing solely on storing values, a semantic model
explicitly defines what entities represent, how they are connected, and the rules that govern their relationships.


**In knowledge graphs, semantic modeling is most often realized through an ontology**.
An `ontology` serves as a schema for the graph, **defining the types of entities within a domain**, the relationships among them, and, at times, logical constraints or hierarchical structures.

**A semantic knowledge model captures and represents the meaning of data by explicitly defining domain-relevant objects, concepts, and the relationships between them**.
This approach produces a model that humans can understand and machines can
interpret.

```
A SPARQL query
PREFIX ex: <http://example.com/hr#>
SELECT ?empName ?deptName
WHERE {
    ?emp a ex:`Employee` ;
    ex:worksIn ?dept ;
    ex:hasName ?empName .
    ?dept ex:hasName ?deptName .
}
```
The latter two define ontology rules, stating that
worksIn links an Employee to a Department. These schema-level statements allow
systems to infer types and validate relationships.


```A simple Cypher query
MATCH (e:`Employee`)-[:WORKS_IN]->(d:`Department` {name: "Sales"})
RETURN e.name;
```

This query directly mirrors the mental model of the graph: find employees connected
to the Sales department via a WORKS_IN relationship. For comparison, the equivalent
SQL query requires a join as shown below.

```An equivalent SQL query
SELECT e.emp_name
FROM `Employee` e
JOIN `Department` d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'Sales';
```

---
What’s important is not the syntax but the workflow: SQL prepares the data, and
the graph navigates the relationships. You stay in the PostgreSQL ecosystem, reuse
existing tables and pipelines, and introduce graph queries only when they add clarity
or performance. For SQL users, this makes graph databases feel less like a radical
departure and more like a natural extension of relational modeling when relationships
become the primary question.
---

## Spark, Apache Flink, CloudRun
Spark is one of the most
widely adopted distributed processing engines in the industry, and its Structured
APIs are fundamentally built around relational abstractions. DataFrames and Datasets
represent logical tables, transformations compile into query plans, and Spark
SQL provides a fully capable SQL interface on top of the same execution engine. In
practice, many DataFrame operations are simply a programmatic way of expressing
relational transformations that could also be written in SQL.

Spark was one of the earliest engines to support Iceberg’s table format and catalog abstractions, including snapshot isolation, schema evolution, partition evolution, and transactional writes.


Apache Flink with SQL for the streaming ingestion. Flink is another distributed stream processing engine that has excellent SQL support. With Flink SQL, you can declare source tables (e.g., a Pub/Sub subscription or Kafka topic) and sink tables (e.g., an Iceberg table), and then issue SQL INSERT
statements that continuously apply.

Cloud Run. to pull data from the API we create one Cloud Run Job per
entity, namely customers, products, and orders. Each job is a small Python script
that executes a well-defined sequence of steps to retrieve data and persist it into the landing zone.

Using Cloud Run jobs for batch ingestion keeps the process on-demand and serverless.
Jobs can be triggered manually or orchestrated through schedulers such as
Workflows or Airflow.

## The Data Lakehouse
A `data lakehouse` is an architectural pattern that merges the best of data lakes and data warehouses. 
In our case, we store data in open formats on cheap, scalable cloud storage, but with a warehouse-like management layer on top (Iceberg) that enables transactions, schema enforcement, and indexing. 

This hybrid design lets us decouple storage and compute: data is persisted in GCS, and multiple engines (e.g., Spark for ingestion, BigQuery for analytics) can operate on the same data without duplication.

The lakehouse ensures that raw data is preserved and auditable, while providing the
governance, ACID consistency, and performance features of a warehouse.

Several key advantages to our storage layer:

1. Single source of truth
  Data is ingested once into the Bronze layer on GCS and never manually copied; both batch and streaming sources end up in the same unified tables. BigQueryreferences this data in place (via BigLake), ensuring analysts query the latest truthdirectly from storage without redundant ETL processes

2. ACID (Atomic,Consistent,Isolated,Durable) transactions and reliability
  Apache Iceberg manages our dataset’s writes so they are atomic, consistent, isolated, and durable. An ingestion job either succeeds completely or fails entirely, preventing partial or corrupt data from ever being visible to downstream users.

3. Schema management and evolution
  As source schemas change over time, the lakehouse can adapt without breaking downstream queries. Iceberg allows adding or removing columns and evolving partition strategies without expensive reprocessing. This means our Bronze tables can gracefully absorb changes (such as a new field in customers data) in a controlled way.

4. Performance via pruning and indexing
  Unlike raw cloud storage, the table format maintains metadata (e.g., min/max statistics and partition indexes) that query engines use to skip irrelevant data. BigQuery, when querying these Iceberg tables, reads only the necessary Parquet files thanks to Iceberg’s manifest-based pruning, which accelerates scans on large partitions.

5. Seamless integration of batch and stream data
  The lakehouse Bronze layer captures both streaming events and batch snapshots into the same tables, naturally supporting Lambda architecture. For example, new incremental orders from Pub/Sub and full daily snapshots of orders can coexist in the bronze.orders table, with each commit adding a snapshot. The Iceberg metadata keeps these writes isolated yet consistent, so analysts don’t have to worry about merge conflicts. They just see a complete table update after each load. Note that, to better demonstrate the differences between real-time and bulk ingestion, this book maintains two separate tracks for order data: incremental events from Pub/Sub into bronze.live_orders and full snapshots from the REST API into bronze.orders.


### Open table formats
One foundational technology enables all the advantages of a lakehouse: `open table formats`. These types of tables are an emerging class of data storage technology (e.g.,Apache Iceberg, Delta Lake, Apache Hudi) designed for transactional data lakes.

**Open table formats introduce a metadata layer on top of flat files, turning a collection of Parquet/Optimized Row Columnar (ORC) files in cloud storage into a queryable table with ACID properties and snapshots**. They are open because they are vendorneutral and widely supported, preventing lock-in while ensuring interoperability across engines and clouds.

This kind of pushdown happens behind the scenes and is one reason we
can store large volumes of raw data without choking BigQuery: the overhead of the
external table is low because BigQuery reads only what Iceberg tells it is necessary. In effect this creates a separation of concerns: **Iceberg handles data layout, metadata, and consistency; BigQuery handles heavy SQL lifting and leaves storage management to the Iceberg layer.**

```
--Time travel with BigQuery and Iceberg
SELECT *
FROM bronze.customers
FOR SYSTEM_TIME AS OF
TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY);
```

## DBT

Example deduplication in Staging orders code

the model stg_orders is a lightweight SQL view that selects all columns from the raw Bronze orders table and filters it to the latest snapshot of data. It uses a common macro to ensure only the newest records (by ingestion timestamp) are included (latest_snapshot_where(..)), preventing duplication of outdated records


```
with src as (
select *
from {{ source('bronze', 'orders') }}
{{ latest_snapshot_where(source('bronze', 'orders')) }}
)
select
cast(id as int64) as order_id,
cast(customer_id as int64) as customer_id,
cast(product_id as int64) as product_id,
cast(ingest_ts as timestamp) as ingest_time
from src
```

```
{% macro latest_snapshot_where(source_relation, ingest_ts_col='ingest_ts') %}
where ({{ ingest_ts_col }}) = (
  select max({{ ingest_ts_col }})
  from {{ source_relation }}
)
{% endmacro %}
```

Here, the {{ source('bronze', 'orders') }} reference tells dbt to read from the raw Bronze orders table, and **the custom latest_snapshot_where macro appends a WHERE clause to pick the maximum ingest timestamp from that table**. 

This effectively implements a deduplication by snapshot: **if the Bronze table contains multiple snapshots or versions of the same entity, the Silver view will show only the most recent version**.


As with the other ingestion jobs, transformations are also executed using a Cloud Run job called ch05-dbt-job. When triggered, the job runs dbt build to materialize Silver and Gold models and execute all tests, followed by dbt docs generate to produce up-to-date documentation. The job runs under a dedicated service account with just enough permissions to create BigQuery jobs and write to the appropriate datasets.

This setup deliberately avoids long-lived virtual machines or heavyweight CI pipelines.
Cloud Run provides a clean execution model in which the job starts, runs
dbt, and exits. It can be triggered manually, scheduled, or orchestrated alongside
ingestion jobs.


Because this project uses dbt Core rather than dbt Cloud, the documentation generated
by dbt docs generate exists as local artifacts instead of a hosted service.

To make these insights accessible, we publish the generated documentation to a dedicated, public-access GCS bucket as part of the job execution. This bucket is
intentionally isolated from the primary data storage to preserve security while still
providing an easy way for readers and stakeholders to inspect lineage, model definitions, and dependencies.

### Orchestration

In our solution, we have multiple moving pieces: Cloud Run jobs (for ingestion into the landing zone), Dataproc Spark jobs (to build the Iceberg table within the Bronze
layer), and dbt transformation runs.

Google Cloud Workflows, a lightweight, serverless orchestration service within Google Cloud, to coordinate the pieces, is chosen. Cloud Workflows allows us to define a directed acyclic graph (DAG) of tasks in YAML,calling various GCP services and waiting for their completion. It’s similar in spirit to tools like Apache Airflow (Cloud Composer on GCP) or Prefect, but it requires no infrastructure setup and is tightly integrated with GCP APIs, aligning with our principles of low maintenance and managed services to reduce operational burden

### Atmoic vs Mart (Debatable)

The main point is that a single source of truth is not achieved by collapsing all
logic into one table. It is achieved by clearly separating responsibilities. Facts own atomic truth. Marts own analytical interpretation. When that boundary is respected, consistency naturally follows.

Instead of letting every dashboard reinvent “revenue,” marts establish shared, governed outputs that downstream tools can trust.


By treating consumption as a first-class layer (much like an API for our warehouse),
we formalize how data is used. In practice, the Consume layer often corresponds
to a dedicated dataset or schema (for example, consume in our scenario) containing
views and stable queries. These views encapsulate business logic and hide underlying
complexity. As long as the view definitions remain consistent, consumers get the
same results and fields, even if the underlying implementation changes.

When are raw Gold tables safe to use directly? In some cases, a Gold model is simple
and stable enough to be used as is.

When is an abstraction required? Whenever the physical schema is subject to change
or the usage logic is complex. For instance, if computing a metric correctly requires
joining multiple tables or applying filters (for instance, revenue might need to join
orders to products for category information, and exclude canceled orders), it’s better to expose a prepared metric view rather than expect each user to get the join and filters right.


`Semantic models consist of the defined entities, metrics, and relationships that give that data meaning`. The semantic model lives on top of the physical tables. It encodes things like Order has a relationship to Customer and Product or Total Revenue is defined as the sum of total_amount after excluding certain statuses and so on.