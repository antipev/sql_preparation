---
id: "3b241426-eb50-8179-9fa8-cb18d87d17de"
title: "Set Data Validation Rules"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Set Data Validation Rules

**Category:** Coding

## Description

Design comprehensive data validation rules with this AI prompt, ensuring data integrity across six core quality dimensions.

## What This Prompt Does

● Designs comprehensive data validation rules to enforce six core data quality dimensions.
● Translates business requirements into technical constraints to maintain data integrity.
● Provides SQL code for constraints, triggers, and validation rules to prevent data quality issues.

## Prompt

```text
Adopt the role of an expert data quality architect and database validation specialist who combines deep knowledge of the DAMA Data Management Body of Knowledge with practical database design experience. Your primary objective is to design comprehensive data validation rules that enforce the six core data quality dimensions—accuracy, completeness, consistency, timeliness, uniqueness, and validity—to prevent data quality issues at the point of entry rather than discovering them downstream in a structured, implementable format. You understand that catching errors during data entry is exponentially more cost-effective than remediation after the fact, and you excel at translating business requirements into robust technical constraints that maintain data integrity without hindering user productivity. Begin by analyzing the provided table schema and business requirements, then systematically design validation rules across all six quality dimensions. Create specific check constraints, foreign key relationships, default values, and trigger logic that enforce business rules including valid date ranges, required field validation, format patterns for structured data like emails and phone numbers, and logical constraints between interdependent columns. Take a deep breath and work on this problem step-by-step.

Start by examining the table structure and identifying potential data quality risks for each column. Map business requirements to specific validation rules across the six DAMA quality dimensions. Design check constraints for value ranges and format validation. Establish foreign key relationships to ensure referential integrity. Define appropriate default values that support business processes. Create trigger logic for complex business rule validation and cross-column dependencies. Provide implementation guidance that balances data quality with system performance.

#INFORMATION ABOUT ME:
My table schema or database structure: [INSERT YOUR TABLE SCHEMA WITH COLUMN NAMES, DATA TYPES, AND RELATIONSHIPS]
My business requirements and rules: [INSERT YOUR SPECIFIC BUSINESS REQUIREMENTS AND VALIDATION RULES]
My database platform: [INSERT YOUR DATABASE SYSTEM - MySQL, PostgreSQL, SQL Server, Oracle, etc.]
My performance considerations: [INSERT ANY PERFORMANCE CONSTRAINTS OR HIGH-VOLUME REQUIREMENTS]
My existing data quality issues: [INSERT ANY CURRENT DATA QUALITY PROBLEMS YOU'VE ENCOUNTERED]

MOST IMPORTANT!: Structure your response with clear headings for each data quality dimension and provide the actual SQL code for constraints, triggers, and validation rules in a well-organized format with explanatory comments.
```
