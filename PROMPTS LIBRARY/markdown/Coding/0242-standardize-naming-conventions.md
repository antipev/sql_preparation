---
id: "3b241426-eb50-81fd-8134-d2526578fb47"
title: "Standardize Naming Conventions"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Standardize Naming Conventions

**Category:** Coding

## Description

Create a comprehensive database naming standardization plan with this AI prompt, ensuring ISO 11179 compliance and zero disruption to applications.

## What This Prompt Does

● Analyzes existing database naming conventions to identify inconsistencies and anti-patterns.
● Develops a standardized naming convention framework following ISO 11179 guidelines.
● Creates a detailed implementation roadmap with rename scripts, rollback procedures, and dependency mapping.

## Prompt

```text
Adopt the role of an expert database architect and ISO 11179 standards specialist who has spent over a decade standardizing enterprise database schemas across Fortune 500 companies. Your primary objective is to analyze existing database naming conventions and create a comprehensive standardization plan that follows ISO 11179 guidelines while ensuring zero disruption to existing applications in a detailed implementation roadmap format. You understand that inconsistent naming conventions create technical debt, reduce developer productivity, and increase maintenance costs. Begin by conducting a thorough analysis of current naming patterns, identifying all inconsistencies including mixed case styles, plural/singular variations, abbreviation misuse, and missing semantic clarity. Develop a unified naming convention framework with specific rules for tables, columns, indexes, constraints, and other database objects. Create detailed rename scripts with rollback procedures and dependency mapping to ensure application compatibility. Take a deep breath and work on this problem step-by-step.

Start by requesting and analyzing the current database schema to identify naming inconsistencies and anti-patterns. Establish clear ISO 11179 compliant naming rules including case conventions, pluralization standards, abbreviation guidelines, and semantic clarity requirements. Create a prioritized implementation plan that groups related objects and minimizes application impact. Generate comprehensive rename scripts with proper dependency handling, backup procedures, and rollback mechanisms. Provide validation queries to verify naming compliance and establish ongoing governance procedures.

#INFORMATION ABOUT ME:
My database platform: [INSERT YOUR DATABASE PLATFORM - e.g., PostgreSQL, MySQL, SQL Server, Oracle]
My current schema or object list: [INSERT YOUR DATABASE SCHEMA EXPORT OR LIST OF TABLES/OBJECTS]
My application dependencies: [INSERT CRITICAL APPLICATIONS OR SYSTEMS THAT USE THIS DATABASE]
My deployment constraints: [INSERT ANY MAINTENANCE WINDOWS OR DEPLOYMENT RESTRICTIONS]
My team's technical expertise level: [INSERT YOUR TEAM'S DATABASE ADMINISTRATION EXPERIENCE LEVEL]

MOST IMPORTANT!: Structure your response with clear sections including Current State Analysis, Proposed Naming Standards, Implementation Roadmap, and SQL Scripts in a well-organized format with proper headings and code blocks for maximum clarity and implementation success.
```
