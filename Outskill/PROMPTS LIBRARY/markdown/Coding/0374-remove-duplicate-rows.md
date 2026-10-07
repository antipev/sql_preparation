---
id: "3b241426-eb50-81d7-a715-fadff180e97a"
title: "Remove Duplicate Rows"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Remove Duplicate Rows

**Category:** Coding

## Description

Guide users through comprehensive duplicate removal with this AI prompt, using Python for data cleaning and analysis.

## What This Prompt Does

● Guides users through a comprehensive duplicate removal process in datasets.
● Educates users on what duplicates were removed and why, using step-by-step code.
● Provides detailed duplicate analysis, including counts, locations, and examples.

## Prompt

```text
Adopt the role of an expert data analyst and Python developer who specializes in data cleaning methodologies from "Python for Data Analysis" with deep expertise in identifying and handling duplicate records across diverse datasets. Your primary objective is to guide users through a comprehensive duplicate removal process that not only cleans their data but educates them on what was removed and why in a clear, step-by-step code implementation. You should follow the established data cleaning methodology where duplicates are identified based on all columns or specific subsets depending on the context. Begin by analyzing the provided dataset to understand its structure, then systematically identify duplicates using pandas methods, display detailed information about what duplicates exist and where they appear, remove them while preserving the first occurrence, and provide comprehensive reporting on the cleaning results. Take a deep breath and work on this problem step-by-step.

Create Python code that first examines the dataset structure and identifies potential duplicate patterns. Generate detailed duplicate analysis showing exact counts, locations, and examples of duplicate records. Implement the removal process with clear before-and-after comparisons. Provide sample outputs of eliminated records so users understand exactly what data was cleaned. Include validation steps to confirm the cleaning was successful and offer insights on whether duplicates were based on all columns or specific subsets.

#INFORMATION ABOUT ME:
My dataset description: [INSERT DESCRIPTION OF YOUR DATASET AND ITS PURPOSE]
My dataset format: [INSERT WHETHER IT'S CSV, EXCEL, JSON, OR OTHER FORMAT]
My specific columns of concern: [INSERT SPECIFIC COLUMNS TO CHECK FOR DUPLICATES, OR "ALL COLUMNS"]
My preferred duplicate criteria: [INSERT WHETHER TO CHECK ALL COLUMNS OR SPECIFIC SUBSETS]
My dataset size estimate: [INSERT APPROXIMATE NUMBER OF ROWS IN YOUR DATASET]

MOST IMPORTANT!: Provide your output as executable Python code blocks with detailed comments, followed by explanatory text for each step. Include sample output examples showing what the duplicate analysis and removal results would look like.
```
