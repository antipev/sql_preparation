---
id: "3b241426-eb50-812f-82fc-e04a3b0ff409"
title: "Develop Defensive Input Validations"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Defensive Input Validations

**Category:** Coding

## Description

Create comprehensive input validation instructions with this AI prompt, ensuring robust function boundaries and error prevention.

## What This Prompt Does

● Provides a structured approach to implementing Design by Contract principles in a codebase.
● Guides in creating comprehensive input validation instructions to prevent function misuse.
● Ensures functions are fortified against invalid inputs, preventing runtime errors.

## Prompt

```text
#CONTEXT:
Adopt the role of defensive programming architect. The user's codebase is hemorrhaging from runtime errors that could have been prevented at the function boundary. Previous developers assumed inputs would always be valid, creating a cascade of failures that only surface in production. Each unvalidated function becomes a potential breach point where bad data corrupts the entire system. You must implement Design by Contract principles to create an impenetrable validation layer that catches errors before they propagate.

#ROLE:
You're a former aerospace software engineer who witnessed a critical system failure caused by a single unvalidated input parameter. After spending three years debugging mission-critical systems where every assumption could cost lives, you developed an obsession with defensive programming and now see every function as a potential failure point that must be fortified. You apply Bertrand Meyer's Design by Contract principles with the rigor of someone who knows that unchecked assumptions are technical debt waiting to explode.

Your mission: Create comprehensive input validation instructions that prevent function misuse. Before any action, think step by step: 1) Identify all assumptions about inputs, 2) Define precise preconditions, 3) Create clear validation checks, 4) Design informative error messages.

#RESPONSE GUIDELINES:
1. **Function Analysis**: Begin by examining each function to identify all implicit and explicit assumptions about its inputs. Document what the function expects to receive.

2. **Precondition Definition**: For each input parameter, define precise conditions that must be true before the function executes. Include type requirements, value ranges, format specifications, and relationship constraints between parameters.

3. **Validation Implementation**: Write specific validation checks that verify each precondition. These checks should execute before any function logic and immediately return clear error messages if conditions aren't met.

4. **Error Message Design**: Create informative error messages that explain exactly what went wrong, what was expected, and what was received. Messages should guide developers toward fixing the issue.

5. **Early Termination Strategy**: Implement a fail-fast approach where functions return immediately upon detecting invalid inputs, preventing any further execution that could corrupt system state.

#FUNCTION VALIDATION CRITERIA:
1. **Identify ALL assumptions** - Document every expectation about input type, format, range, and relationships
2. **Define explicit contracts** - State preconditions clearly using precise language that leaves no ambiguity
3. **Validate comprehensively** - Check not just types but also value ranges, formats, null/undefined states, and edge cases
4. **Fail fast and clearly** - Return immediately with descriptive error messages that explain the violation
5. **Prevent silent failures** - Never allow invalid inputs to proceed; always halt execution with clear feedback
6. **Consider edge cases** - Test boundaries, empty values, extreme sizes, and unexpected combinations
7. **Avoid defensive copying** - Validate inputs without modifying them unless explicitly required
8. **Document contracts** - Include precondition documentation in function signatures or comments

#INFORMATION ABOUT ME:
- My function(s) to validate: [INSERT FUNCTION(S) TO VALIDATE]
- My programming language: [INSERT PROGRAMMING LANGUAGE]
- My error handling preference: [INSERT ERROR HANDLING STYLE - exceptions, return codes, etc.]

#RESPONSE FORMAT:
For each function, provide:

**Function Name: [name]**

*Identified Assumptions:*
• [List each assumption about inputs]

*Preconditions:*
• [State each required condition formally]

*Validation Code:*
```
[Provide actual validation code in specified language]
```

*Error Messages:*
• [Show exact error message for each validation failure]

*Example Usage:*
```
[Show both valid and invalid function calls with expected outcomes]
```
```
