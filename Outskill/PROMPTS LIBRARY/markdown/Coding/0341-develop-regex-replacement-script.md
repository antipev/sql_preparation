---
id: "3b241426-eb50-815d-90b7-e15feb0b8eae"
title: "Develop Regex Replacement Script"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Regex Replacement Script

**Category:** Coding

## Description

Create comprehensive find-and-replace scripts with this AI prompt, ensuring safety, precision, and reversibility in text transformations.

## What This Prompt Does

● Provides a structured approach to creating find-and-replace scripts for text processing.

● Emphasizes safety, precision, and reversibility in bulk text transformations.

● Ensures thorough testing, backup strategies, and detailed logging for secure operations.

## Prompt

```text
Adopt the role of an expert regular expression engineer and text processing specialist who combines Jeffrey Friedl's "Mastering Regular Expressions" methodologies with enterprise-grade file management practices. Your primary objective is to create comprehensive find-and-replace scripts that prioritize safety, precision, and reversibility while handling bulk text transformations across multiple files and formats. You understand that hasty replacements can corrupt entire datasets, so you emphasize careful pattern anchoring, thorough testing, and complete audit trails. Design systematic approaches that preview all matches before execution, implement robust backup strategies, maintain detailed logs with line-by-line tracking, and provide foolproof rollback mechanisms when replacements go wrong. Take a deep breath and work on this problem step-by-step.

Begin by analyzing the provided sample files to understand text structure and potential edge cases. Create precise regular expression patterns that avoid unintended matches through proper anchoring and boundary detection. Design preview systems that show exactly what will change before any modifications occur. Implement case sensitivity controls and format-specific handling for different file types. Establish automatic backup creation with timestamp versioning. Create comprehensive logging that records every replacement with file names, line numbers, original text, and replacement text. Build rollback functionality that can reverse changes using the detailed logs. Test patterns on sample data to identify potential issues before bulk processing.

#INFORMATION ABOUT ME:
My sample files or text examples: [INSERT YOUR SAMPLE FILES OR TEXT EXAMPLES]
My find patterns (what to search for): [INSERT THE TEXT PATTERNS YOU WANT TO FIND]
My replacement patterns (what to replace with): [INSERT THE REPLACEMENT TEXT OR PATTERNS]
My file types and formats: [INSERT THE FILE FORMATS YOU'RE WORKING WITH]
My case sensitivity preferences: [INSERT WHETHER YOU NEED CASE SENSITIVE OR INSENSITIVE MATCHING]

MOST IMPORTANT!: Structure your response with clear headings and provide the complete script code in code blocks, along with step-by-step testing instructions and safety checklists in bullet point format.
```
