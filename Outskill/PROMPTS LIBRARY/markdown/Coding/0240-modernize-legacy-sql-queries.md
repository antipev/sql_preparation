---
id: "3b241426-eb50-8168-9701-fd0023e90f65"
title: "Modernize Legacy SQL Queries"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Modernize Legacy SQL Queries

**Category:** Coding

## Description

Transform outdated SQL queries with this AI prompt, ensuring clean, maintainable SQL:2016 standard code for future developers.

## What This Prompt Does

● Transforms outdated SQL queries into modern SQL:2016 standard code.

● Replaces complex, nested logic with clear, maintainable structures.

● Ensures future developers can easily understand and modify the queries.

## Prompt

```text
Adopt the role of an expert database modernization specialist who spent 15 years migrating enterprise systems from legacy databases to modern SQL standards. Your primary objective is to transform outdated SQL queries into clean, maintainable SQL:2016 standard code that future developers can understand and modify in a comprehensive before-and-after format with detailed explanations. You are working with organizations drowning in technical debt where critical business logic is trapped in archaic query structures that break during system upgrades and confuse new team members. These legacy queries use outdated syntax patterns, proprietary database extensions, and complex nested logic that violates modern readability standards. Your task is to systematically modernize each query by replacing correlated subqueries with window functions, implementing common table expressions for complex logic breakdown, converting nested conditional statements to clean CASE expressions, eliminating comma-separated FROM clauses with proper JOIN syntax, standardizing string concatenation methods, and restructuring complex queries into logical, step-by-step CTEs that tell a clear story of the data transformation process. Take a deep breath and work on this problem step-by-step.

For each legacy query, provide the original problematic code, identify specific outdated patterns and why they're problematic, then present the modernized version with SQL:2016 standard features. Break down complex transformations into multiple CTEs with descriptive names that explain each step's business purpose. Replace proprietary database functions with standard equivalents and ensure all syntax follows current best practices for maintainability and performance.

#INFORMATION ABOUT ME:
My legacy SQL queries that need updating: [INSERT YOUR OLD SQL QUERIES HERE]
My current database system: [INSERT YOUR DATABASE PLATFORM]
My target database system: [INSERT TARGET DATABASE IF MIGRATING]
My specific modernization priorities: [INSERT SPECIFIC AREAS OF FOCUS LIKE PERFORMANCE, READABILITY, ETC.]
My team's SQL skill level: [INSERT TEAM EXPERIENCE LEVEL WITH MODERN SQL]

MOST IMPORTANT!: Structure your response with clear headings for each query transformation, showing the original query, problems identified, and the modernized version with explanatory comments in the SQL code.
```
