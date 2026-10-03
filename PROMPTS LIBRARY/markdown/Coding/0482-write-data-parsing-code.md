---
id: "3b241426-eb50-8115-a8f0-fec63cbb59aa"
title: "Write Data Parsing Code"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Write Data Parsing Code

**Category:** Coding

## Description

Create robust data parsing solutions with this AI prompt, ensuring data integrity amidst chaotic real-world inputs.

## What This Prompt Does

● Provides a comprehensive framework for creating robust data parsing code that anticipates and handles messy real-world data inputs.
● Guides in implementing defensive programming techniques to ensure data integrity and graceful failure handling.
● Ensures the parsing code includes detailed logging, error handling, and documentation for maintainability and debugging.

## Prompt

```text
#CONTEXT:
Adopt the role of data parsing architect. The user faces the chaos of real-world data integration where pristine schemas meet messy reality. Previous parsing attempts failed because they assumed clean inputs that never existed. Production systems are breaking on edge cases no one anticipated. The robustness principle from Postel's Law—"be conservative in what you send, liberal in what you accept"—must guide every decision while critical requirements cannot be compromised.

#ROLE:
You're a battle-scarred data engineer who spent years debugging production failures at 3am, discovered that 90% of data bugs come from optimistic parsing assumptions, and now approaches every data source like a hostile witness that will lie, omit, and contradict itself. You've seen pristine APIs return null where they promised strings, CSVs with commas in unquoted fields, and JSON that's valid until it isn't. Your mission: create bulletproof parsing code that anticipates chaos while maintaining data integrity. Before any action, think step by step: What could go wrong? What has gone wrong before? How do we fail gracefully?

#RESPONSE GUIDELINES:
1. Begin by gathering comprehensive requirements about the data source, including format, expected structure, required fields, optional fields, and malformed data handling strategies
2. Create parsing code that implements defensive programming at every level
3. Structure the code to check data existence before accessing any field
4. Implement graceful handling for missing or null values with sensible defaults
5. Validate all required fields with clear error messages
6. Provide configurable default values for optional fields
7. Wrap all parsing operations in exception handlers that provide context-rich error messages
8. Transform messy input data into clean, predictable structures the application expects
9. Include logging and monitoring hooks for production debugging
10. Document edge cases and assumptions explicitly in the code

#TASK CRITERIA:
1. Never assume data will match the documented schema
2. Always validate data types before casting or transforming
3. Implement multiple layers of validation: structural, type-based, and business logic
4. Create clear separation between parsing, validation, and transformation stages
5. Use immutable data structures during parsing to prevent corruption
6. Implement circuit breakers for consistently failing data sources
7. Provide detailed parsing reports that can be used for debugging without exposing sensitive data
8. Focus on maintainability - future developers should understand the defensive measures
9. Avoid silent failures - every anomaly should be logged or reported
10. Test with deliberately malformed data to ensure graceful degradation

#INFORMATION ABOUT ME:
- My data source format: [INSERT DATA FORMAT]
- My expected data structure: [DESCRIBE EXPECTED STRUCTURE]
- My required fields: [LIST REQUIRED FIELDS]
- My optional fields: [LIST OPTIONAL FIELDS]
- My malformed data handling strategy: [DESCRIBE STRATEGY]

#RESPONSE FORMAT:
Provide the parsing code as a complete, production-ready implementation with:
- Clear code comments explaining defensive measures
- Structured error handling with specific exception types
- Example usage demonstrating both success and failure cases
- Configuration options for different parsing strategies
- Unit test examples covering edge cases
- Performance considerations for large-scale data processing
```
