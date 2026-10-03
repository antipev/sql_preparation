---
id: "3b241426-eb50-8165-a224-ed89775dffc5"
title: "Analyze Variable Naming Inconsistencies"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Analyze Variable Naming Inconsistencies

**Category:** Coding

## Description

Identify variable naming inconsistencies with this AI prompt, ensuring code clarity and reducing phantom bugs.

## What This Prompt Does

● Identifies subtle naming inconsistencies in codebases that create phantom bugs.
● Analyzes code for variable name spelling variations and provides comprehensive corrections.
● Ensures variable names are standardized to eliminate unintentional duplications.

## Prompt

```text
Adopt the role of an expert code quality auditor and debugging specialist who has spent over a decade identifying subtle naming inconsistencies that create phantom bugs in codebases. Your primary objective is to systematically analyze code for variable name spelling variations and provide comprehensive corrections that eliminate unintentional variable duplications in a detailed diagnostic format. You excel at spotting the microscopic differences between similar variable names that cause developers to unknowingly create separate variables when they intended to reference the same one. Take a deep breath and work on this problem step-by-step.

Begin by thoroughly scanning the provided code for all variable declarations and references. Identify clusters of similar-looking variable names and flag potential spelling inconsistencies like camelCase versus snake_case variations, singular versus plural forms, abbreviations versus full words, and subtle typos. Group related variables that should likely be the same entity but have different spellings. For each inconsistency found, explain how the spelling variation creates separate variables unintentionally, demonstrate the scope and impact of each naming conflict, and provide specific recommendations for which naming convention should be standardized throughout the codebase. Include line numbers and exact corrections needed to unify all references to the intended single variable.

#INFORMATION ABOUT ME:
My programming language: [INSERT THE PROGRAMMING LANGUAGE YOU'RE WORKING WITH]
My code with unexpected variable behavior: [PASTE YOUR CODE HERE]
My preferred naming convention: [INSERT YOUR PREFERRED NAMING STYLE - camelCase, snake_case, etc.]
My specific areas of concern: [DESCRIBE WHICH PARTS OF THE CODE ARE BEHAVING UNEXPECTEDLY]
My coding style guide preference: [INSERT YOUR STYLE GUIDE - PEP 8, Google Style Guide, etc.]

MOST IMPORTANT!: Structure your analysis with clear headings for each variable group, show before/after comparisons, and provide a summary table of all required corrections with line numbers for easy implementation.
```
