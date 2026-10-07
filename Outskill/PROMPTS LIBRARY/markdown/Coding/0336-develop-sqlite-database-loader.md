---
id: "3b241426-eb50-815d-8715-e0bde62f60cf"
title: "Develop SQLite Database Loader"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop SQLite Database Loader

**Category:** Coding

## Description

Create a robust SQLite database loader system with this AI prompt, converting CSV files into normalized, indexed, and constrained tables.

## What This Prompt Does

● Converts CSV files into normalized, indexed, and constrained SQLite database tables.
● Infers data types, validates constraints, and optimizes schema for production systems.
● Provides detailed reporting on data import success and constraint violations.

## Prompt

```text
Adopt the role of an expert database architect and data engineer who specializes in relational database theory, particularly C.J. Date's principles of database normalization and data integrity. Your primary objective is to create a comprehensive SQLite database loader system that converts CSV files into properly normalized, indexed, and constrained database tables with full documentation and validation reporting. You have extensive experience in data type inference, constraint validation, and schema optimization for production systems. Apply rigorous database normalization principles to ensure data integrity through proper typing, indexing, and constraint definition. Generate Python code that intelligently infers appropriate data types from CSV samples, creates efficiently indexed tables, handles NULL values according to business rules, validates all data during import process, and provides detailed reporting on any rows that fail constraint validation. Take a deep breath and work on this problem step-by-step.

Begin by analyzing the provided CSV structure and relationships between datasets. Create a data type inference engine that samples CSV data to determine optimal SQLite column types. Design proper indexing strategies based on anticipated query patterns. Implement comprehensive constraint validation including primary keys, foreign keys, check constraints, and NOT NULL requirements. Generate detailed import logs showing successful imports and constraint violations. Create complete schema documentation explaining table structures, relationships, and business rules.

#INFORMATION ABOUT ME:
My CSV files to convert: [INSERT YOUR CSV FILE NAMES AND BRIEF DESCRIPTIONS]
My relationships between datasets: [DESCRIBE HOW YOUR TABLES RELATE TO EACH OTHER]
My specific data validation requirements: [INSERT ANY SPECIAL VALIDATION RULES OR CONSTRAINTS]
My expected query patterns: [DESCRIBE HOW YOU PLAN TO USE THE DATABASE]
My NULL value handling preferences: [INSERT HOW YOU WANT NULL VALUES TREATED]

MOST IMPORTANT!: Provide your output as complete Python code with detailed comments, followed by a markdown table showing the proposed schema structure with columns for Table Name, Column Name, Data Type, Constraints, and Index Strategy.
```
