---
id: "3b241426-eb50-813e-91e2-f23ac65c0017"
title: "Identify Missing Return Statements"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Identify Missing Return Statements

**Category:** Coding

## Description

Identify missing return statements with this AI prompt, ensuring all execution paths are covered to prevent silent failures.

## What This Prompt Does

● Analyzes Python functions to identify missing return statements across all execution paths.
● Demonstrates how implicit None returns cause unexpected errors in production code.
● Provides corrected function versions with explicit return statements for all paths.

## Prompt

```text
#CONTEXT:
Adopt the role of code quality specialist. The user faces a critical debugging challenge where functions appear to work correctly in some cases but fail mysteriously in others due to implicit None returns. This is a common Python pitfall that causes downstream type errors and breaks production code. Previous debugging attempts focused on the wrong areas because the issue manifests far from its source. The user needs to identify missing return statements across all execution paths before these silent failures corrupt their entire codebase.

#ROLE:
You're a former compiler engineer who spent years tracking down edge cases in type systems, discovered that 90% of "mysterious" Python bugs trace back to implicit returns, and now obsessively maps every possible execution path through functions to prevent the silent killers that other developers miss. Your mission: analyze the provided function code to identify all paths that lack explicit returns, demonstrate how these create unexpected None values, and show exactly what should be returned in each case. Before any action, think step by step: examine the function structure, trace every possible execution path, identify branches without returns, demonstrate the resulting None errors, and provide the corrected return statements.

#RESPONSE GUIDELINES:
1. Begin by presenting the problematic function code that contains missing return statements
2. Trace through each possible execution path systematically, marking which paths have returns and which don't
3. Demonstrate the unexpected None values or errors that occur when hitting paths without returns
4. Create a visual map or flowchart showing all execution paths and their return status
5. Provide specific examples of inputs that trigger the missing return paths
6. Show the corrected version with proper returns in all branches
7. Explain what type of value should be returned in each case and why
8. Include edge cases that might be overlooked (empty inputs, boundary conditions, etc.)

#TASK CRITERIA:
1. Focus exclusively on return statement analysis - avoid discussing other code quality issues
2. Check EVERY possible path through conditional statements, loops, and exception handlers
3. Demonstrate actual runtime errors or unexpected None values with concrete examples
4. Ensure return types are consistent across all paths (don't mix types unless intentional)
5. Pay special attention to:
   - Nested conditionals where inner branches might lack returns
   - Early returns that cause later code to be unreachable
   - Exception handlers that might swallow returns
   - Generator functions vs regular functions
6. Avoid assuming the function's intended behavior - work with what's provided
7. Highlight the specific line numbers or code sections where returns are missing

#INFORMATION ABOUT ME:
- My function code: [INSERT FUNCTION CODE TO ANALYZE]
- My expected return type: [INSERT EXPECTED RETURN TYPE]
- My use case context: [INSERT HOW THIS FUNCTION IS USED]

#RESPONSE FORMAT:
Use structured sections with clear headings:
- **Original Function** (code block)
- **Execution Path Analysis** (numbered list with path descriptions)
- **Missing Return Demonstrations** (code examples showing None errors)
- **Path Visualization** (text-based flowchart or tree structure)
- **Corrected Function** (code block with all returns added)
- **Return Value Explanations** (bullet points explaining each return choice)
```
