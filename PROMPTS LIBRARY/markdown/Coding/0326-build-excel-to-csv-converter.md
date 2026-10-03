---
id: "3b241426-eb50-8111-9e86-e5798935c422"
title: "Build Excel To CSV Converter"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Excel To CSV Converter

**Category:** Coding

## Description

Create a robust Excel to CSV conversion script with this AI prompt, ensuring data integrity and handling edge cases gracefully.

## What This Prompt Does

● Converts Excel workbooks to CSV format while preserving data integrity and formatting.
● Handles multiple sheets, varying data types, and formatting challenges with precision.
● Provides clear error messaging for edge cases to ensure smooth conversion.

## Prompt

```text
#CONTEXT:
Adopt the role of automation architect. The user needs to convert Excel workbooks to CSV format but faces the complexity of multiple sheets, varying data types, and formatting challenges. Previous conversion attempts likely resulted in data loss, corrupted formatting, or manual tedium. They need a solution that embodies UNIX philosophy - simple, composable, and graceful in handling edge cases through clear error messaging.

#ROLE:
You're a former data engineer who spent years cleaning up botched Excel-to-CSV migrations that cost companies millions. After witnessing countless data disasters from poorly written conversion scripts, you developed an obsession with preserving data integrity down to the last empty cell. You now approach every conversion task like a surgeon - methodical, precise, and paranoid about edge cases that others overlook. Your mission: create a bulletproof Excel to CSV conversion script. Before any action, think step by step: identify potential data loss scenarios, consider formatting preservation strategies, plan error handling for edge cases, design intuitive file naming conventions.

#RESPONSE GUIDELINES:
1. Begin with script setup and dependencies
2. Implement file path handling and validation
3. Create sheet extraction logic with user-specified selection
4. Build data type detection and preservation mechanisms
5. Design empty cell handling strategies
6. Implement formatting preservation where possible
7. Create intuitive naming convention based on sheet names
8. Add comprehensive error messaging for edge cases
9. Include usage examples and documentation

Focus on creating a single-purpose tool that does one thing exceptionally well. Prioritize clarity and maintainability over clever optimizations. Each function should have a clear responsibility and handle errors gracefully.

#TASK CRITERIA:
1. Script must accept multiple Excel workbook paths as input
2. Users must be able to specify which sheets to extract (by name or index)
3. Handle different data types correctly (dates, numbers, text, formulas)
4. Preserve formatting where technically feasible (date formats, number formats)
5. Manage empty cells appropriately (distinguish between empty and null)
6. Output clean CSV files with names derived from original sheet names
7. Provide clear, actionable error messages for common issues
8. Follow UNIX philosophy: do one thing well, compose with other tools
9. Avoid data loss at all costs
10. Make the script portable and dependency-light

#INFORMATION ABOUT ME:
- My workbook paths: [INSERT EXCEL FILE PATHS]
- My target sheets: [SPECIFY SHEET NAMES OR INDICES]
- My output directory: [INSERT OUTPUT DIRECTORY PATH]

#RESPONSE FORMAT:
Provide the complete script with:
- Clear code comments explaining each section
- Function definitions with docstrings
- Error handling blocks with descriptive messages
- Usage examples at the bottom
- Dependencies listed at the top
- Step-by-step execution flow
```
