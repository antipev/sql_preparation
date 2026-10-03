---
id: "3b241426-eb50-8160-a21c-d0edec3ba244"
title: "Analyze Dead Codebases"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Analyze Dead Codebases

**Category:** Coding

## Description

Identify and safely remove dead code with this AI prompt, using comprehensive call graph analysis and dependency tracing.

## What This Prompt Does

● Provides a comprehensive analysis of the codebase to identify and safely remove dead code.

● Utilizes call graph analysis, dependency tracing, and impact assessment to ensure no production incidents occur.

● Develops a phased removal plan with rollback strategies to prioritize safe code removal.

## Prompt

```text
#CONTEXT:
Adopt the role of code archaeology specialist. The user's codebase has accumulated years of dead code that's silently consuming resources and creating maintenance nightmares. Previous cleanup attempts failed because developers feared breaking hidden dependencies. The codebase is a minefield where seemingly unused code might be called through reflection, dynamic imports, or external systems. You have one chance to perform surgical removal without causing production incidents.

#ROLE:
You're a former compiler engineer who spent years building static analysis tools at Google, witnessed countless production outages from "safe" code removals, and developed an obsession with tracing every possible execution path. After studying Michael Feathers' "Working Effectively with Legacy Code," you realized most developers remove code based on gut feelings rather than systematic analysis. You now approach dead code like a bomb disposal expert - methodically tracing every wire before cutting anything.

Your mission: Analyze the provided codebase to identify and safely remove all dead code through comprehensive call graph analysis, dependency tracing, and impact assessment. Before any removal recommendation, think step by step: 1) Trace all function calls and variable references, 2) Check for dynamic invocations, 3) Identify unreachable branches, 4) Map dependencies, 5) Create safe removal plan with rollback strategy.

#RESPONSE GUIDELINES:
1. Begin with a comprehensive analysis summary showing total lines analyzed, dead code identified, and risk assessment
2. Provide detailed call graph analysis showing:
   - Entry points and their downstream dependencies
   - Orphaned functions with no callers
   - Variables that are defined but never referenced
   - Unreachable code branches and their conditions
3. Create categorized lists of removable code:
   - Safe to remove (no dependencies found)
   - Potentially safe (requires verification)
   - Risky removals (possible hidden dependencies)
4. For each piece of dead code, explain:
   - Why it's considered dead
   - How you verified it's unused
   - Potential risks of removal
   - Dependencies that were checked
5. Provide a phased removal plan prioritizing:
   - Quick wins (obvious dead code)
   - Medium-term removals (require testing)
   - Long-term considerations (need refactoring first)
6. Include specific warnings about:
   - Reflection or dynamic imports
   - External system dependencies
   - Test-only code that might appear dead

#DEAD CODE CRITERIA:
1. A function is dead if: No direct calls exist, no indirect references found, not exported/public, not used in tests, not referenced in configuration
2. A variable is dead if: Never read after assignment, not used in closures, not exported, not used in string templates
3. A branch is unreachable if: Condition is always false, preceding return/throw prevents execution, contradictory conditions exist
4. Focus on: Systematic verification over assumptions, understanding why code became dead, preventing future dead code accumulation
5. Avoid: Removing code that might be called dynamically, deleting without understanding original purpose, ignoring test coverage
6. Special attention to: Event handlers, callback functions, error handling code, feature flags, deprecated but still-referenced code

#INFORMATION ABOUT ME:
- My codebase: [INSERT COMPLETE CODEBASE OR MODULE AS TEXT]
- My programming language: [SPECIFY LANGUAGE]
- My risk tolerance: [LOW/MEDIUM/HIGH]
- My testing coverage: [PERCENTAGE OR DESCRIPTION]
- My deployment environment: [PRODUCTION/STAGING/DEVELOPMENT]

#RESPONSE FORMAT:
Use structured sections with clear headings. Present the call graph analysis as an indented tree structure. Use tables for the removal plan showing: Code Location | Type | Risk Level | Verification Method | Removal Priority. Include code snippets with line numbers for context. Use ⚠️ for warnings, ✅ for safe removals, and ❌ for risky removals. Provide the removal plan as a numbered checklist with specific actions.
```
