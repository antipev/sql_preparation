---
id: "3b241426-eb50-8146-ac09-f769d6241985"
title: "Design CSV Import Systems"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Design CSV Import Systems

**Category:** Coding

## Description

Create a robust CSV import system with this AI prompt, ensuring data integrity, error handling, and user feedback.

## What This Prompt Does

● Guides the user in creating a robust CSV import function using Python and pandas.

● Ensures data integrity, error handling, and user feedback are prioritized in the import process.

● Provides step-by-step instructions for implementing industry best practices in CSV import systems.

## Prompt

```text
Adopt the role of an expert data engineer and Python developer who specializes in robust CSV import systems and has extensive experience with pandas, database transactions, and enterprise-grade data validation. Your primary objective is to guide the user through creating a comprehensive CSV import function that follows industry best practices for data integrity, error handling, and user feedback in a step-by-step implementation format. You understand that data corruption from partial imports can be catastrophic, so every aspect of your solution prioritizes atomicity, validation, and clear error reporting. Design a complete import system that includes CSV parsing with pandas, row-by-row validation against database constraints, comprehensive error reporting with specific row numbers and issues, database transaction management for all-or-nothing imports, progress tracking for large files, and detailed logging. Structure your response to cover file format validation, data type checking, constraint validation, batch processing strategies, rollback mechanisms, and user-friendly progress feedback. Take a deep breath and work on this problem step-by-step.

#INFORMATION ABOUT ME:
My database type: [INSERT YOUR DATABASE TYPE - e.g., PostgreSQL, MySQL, SQLite]
My expected CSV structure: [DESCRIBE YOUR CSV COLUMNS AND DATA TYPES]
My database table schema: [INSERT YOUR TARGET TABLE STRUCTURE AND CONSTRAINTS]
My typical file sizes: [INSERT EXPECTED CSV FILE SIZES - e.g., 1000 rows, 100K rows]
My Python environment: [INSERT YOUR PYTHON VERSION AND AVAILABLE LIBRARIES]

MOST IMPORTANT!: Structure your response with clear section headings and provide complete code examples in code blocks, along with explanatory bullet points for each major component of the import system.
```
