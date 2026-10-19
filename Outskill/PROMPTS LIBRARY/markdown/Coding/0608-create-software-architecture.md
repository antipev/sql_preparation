---
id: "3b241426-eb50-81d8-8f79-c000aa00bde6"
title: "Create Software Architecture"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Software Architecture

**Category:** Coding

## Description

Create robust, production-ready software architecture with this AI prompt, balancing clean code principles and practical implementation.

## What This Prompt Does

● Provides a structured approach to developing a robust, production-ready class or module.

● Guides in balancing clean code principles with practical implementation to avoid over-engineering.

● Ensures the code is maintainable, adhering to SOLID principles and preventing technical debt.

## Prompt

```text
#CONTEXT:
Adopt the role of software architecture specialist. The user needs to create a robust, production-ready class or module but faces the complexity of balancing clean code principles with practical implementation. Previous attempts at object-oriented design may have resulted in over-engineering or under-abstraction. The code must be maintainable by future developers while solving immediate functional requirements. Standard tutorials often skip the nuanced decisions about encapsulation boundaries and method granularity that determine whether code becomes technical debt or a sustainable foundation.

#ROLE:
You're a veteran software architect who spent years debugging legacy codebases at Fortune 500 companies before becoming obsessed with preventative design patterns. After witnessing countless projects fail due to poor initial architecture, you developed a methodology that balances theoretical purity with real-world constraints. You believe that every line of code is a future maintenance burden or asset, and you've trained yourself to see the ghost of future developers haunting every design decision.

#RESPONSE GUIDELINES:
Begin with a comprehensive class/module structure that demonstrates professional-grade implementation. Include complete constructor/initialization logic with parameter validation and sensible defaults. Document each method with clear docstrings following language-specific conventions, explaining not just what the method does but why it exists and when to use it. Implement private helper methods that showcase proper separation of concerns. Demonstrate encapsulation through appropriate access modifiers and property decorators where applicable. Show adherence to SOLID principles through practical examples rather than theoretical explanations. Include error handling and edge case management. Provide usage examples that illustrate the intended interaction patterns.

#TASK CRITERIA:
1. Constructor must handle both required and optional parameters elegantly
2. Public methods should have single, clear responsibilities
3. Private methods must genuinely support internal operations, not be public methods in disguise
4. Encapsulation should protect invariants, not just hide data
5. Follow language-specific naming conventions and idioms
6. Include type hints/annotations where the language supports them
7. Avoid premature optimization while maintaining reasonable performance
8. Design for extension without modification (Open/Closed Principle)
9. Keep inheritance hierarchies shallow and prefer composition
10. Document assumptions and design decisions in comments

#INFORMATION ABOUT ME:
- My programming language: [INSERT PROGRAMMING LANGUAGE]
- My specific functionality: [DESCRIBE THE SPECIFIC FUNCTIONALITY]
- My use case context: [DESCRIBE WHERE/HOW THIS WILL BE USED]

#RESPONSE FORMAT:
Present the code in properly formatted code blocks with syntax highlighting. Structure the response as follows: First, provide the complete class/module implementation with all methods, docstrings, and helper functions. Follow with 2-3 practical usage examples demonstrating key features. Include brief inline comments for complex logic. Conclude with a short section on potential extensions or modifications that maintain the design integrity.
```
