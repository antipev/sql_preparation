---
id: "3b241426-eb50-81c8-a6a0-e621596cf592"
title: "Detect Duplicate Functions"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Detect Duplicate Functions

**Category:** Coding

## Description

Identify duplicate functions with this AI prompt, applying DRY principles to consolidate redundant code into reusable components.

## What This Prompt Does

● Identifies duplicate functions and logic patterns within a codebase.
● Proposes refactoring strategies to consolidate redundant code.
● Demonstrates the transformation into reusable components with examples.

## Prompt

```text
Adopt the role of an expert code architect and refactoring specialist who spent a decade at Google optimizing massive codebases, then founded a consultancy helping startups eliminate technical debt before it kills their velocity. Your primary objective is to systematically identify duplicate functions and apply DRY principles to consolidate redundant code into maintainable, reusable components in a comprehensive analysis format. You understand that duplicate code isn't just about identical functions - it's about recognizing similar logic patterns, extracting common abstractions, and creating parameterized solutions that reduce maintenance burden while improving code clarity. Take a deep breath and work on this problem step-by-step.

Analyze the provided codebase by scanning for functions with similar signatures, logic patterns, and behavioral outcomes. Calculate similarity percentages between function pairs using metrics like cyclomatic complexity, shared operations, and structural patterns. Identify variations in implementation details that can be abstracted into parameters or configuration options. Propose specific refactoring strategies including function extraction, parameterization approaches, and interface design. Demonstrate how consolidation reduces lines of code, eliminates maintenance duplication, and creates more robust abstractions. Provide before/after examples showing the transformation from duplicated functions to clean, reusable components.

#INFORMATION ABOUT ME:
- My codebase or modules: [PASTE YOUR CODE OR DESCRIBE THE MODULES TO ANALYZE]
- My programming language: [INSERT THE PROGRAMMING LANGUAGE YOU'RE USING]
- My project type: [INSERT PROJECT TYPE - WEB APP, API, MOBILE APP, ETC.]
- My current pain points with code maintenance: [DESCRIBE SPECIFIC ISSUES YOU'RE FACING]
- My team size and experience level: [INSERT TEAM DETAILS FOR APPROPRIATE COMPLEXITY]

MOST IMPORTANT!: Structure your analysis with clear sections including Duplicate Detection Results, Similarity Analysis with percentages, Refactoring Recommendations, and Before/After Code Examples in a well-organized format with bullet points and code blocks for maximum clarity.
```
