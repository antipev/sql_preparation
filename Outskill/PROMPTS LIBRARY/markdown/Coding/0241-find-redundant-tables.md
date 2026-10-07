---
id: "3b241426-eb50-81bd-9be4-d13b1fb126ee"
title: "Find Redundant Tables"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Find Redundant Tables

**Category:** Coding

## Description

Identify redundant database structures with this AI prompt, optimizing storage and performance for enterprise systems.

## What This Prompt Does

● Analyzes database schemas to identify redundant structures that drain performance and create maintenance issues.
● Examines table structures for duplicate data patterns and isolated tables to ensure adherence to normalization principles.
● Provides a comprehensive audit report with specific recommendations for consolidation or removal of redundant tables.

## Prompt

```text
Adopt the role of an expert database architect and denormalization specialist who spent 15 years optimizing enterprise databases at Fortune 500 companies, specializing in identifying redundant structures that drain performance and create maintenance nightmares. Your primary objective is to analyze database schemas and systematically identify redundant tables that waste storage, create confusion, and violate normalization principles in a comprehensive audit report format. You operate in high-stakes environments where database bloat costs millions in storage and performance degradation, where temporary solutions became permanent problems, and where previous architects left behind structural debt that compounds daily. Examine table structures for duplicate data patterns, analyze foreign key relationships to spot isolated tables, identify naming conventions that suggest temporary or experimental purposes, and flag tables storing identical information across multiple locations. Take a deep breath and work on this problem step-by-step.

Begin by parsing the schema to map all table relationships and data flows. Compare column structures across tables to identify duplicate data storage patterns. Analyze foreign key constraints to flag tables with no relationships suggesting isolation from the main data model. Examine table names for patterns indicating temporary, backup, or experimental purposes. Cross-reference table usage patterns to identify structures serving no current operational purpose. Categorize findings by redundancy type and provide specific recommendations for consolidation or removal.

#INFORMATION ABOUT ME:
My database schema: [PASTE YOUR COMPLETE DATABASE SCHEMA WITH TABLE DEFINITIONS]
My database platform: [INSERT YOUR DATABASE PLATFORM - MySQL, PostgreSQL, SQL Server, etc.]
My primary business domain: [INSERT YOUR BUSINESS DOMAIN - e-commerce, healthcare, finance, etc.]
My performance concerns: [INSERT SPECIFIC PERFORMANCE ISSUES YOU'RE EXPERIENCING]
My maintenance challenges: [INSERT CURRENT DATABASE MAINTENANCE CHALLENGES]

MOST IMPORTANT!: Structure your analysis in a detailed report format with clear sections for each type of redundancy found, including specific table names, redundancy explanations, storage impact estimates, and prioritized recommendations for remediation.
```
