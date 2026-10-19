---
id: "3b241426-eb50-81cd-bb8d-d23d1a05841c"
title: "Develop Error Handling System"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Error Handling System

**Category:** Coding

## Description

Create a resilient error handling system with this AI prompt, transforming cryptic API responses into actionable intelligence while adhering to RFC 7807 standards.

## What This Prompt Does

● Transforms inconsistent API error responses into a standardized format, making them easier to understand and debug.
● Maps diverse error formats to RFC 7807 standards, ensuring compliance and clarity.
● Implements a robust error handling system that maintains compatibility with API updates.

## Prompt

```text
#CONTEXT:
Adopt the role of API integration architect. The user's development team is drowning in inconsistent error responses from multiple third-party APIs, each with its own cryptic error format. Production incidents escalate because developers can't quickly identify root causes. Customer support receives vague error messages that provide no actionable information. Previous attempts at error standardization created brittle wrappers that broke with every API update. The team needs a resilient error handling system that transforms chaos into clarity while maintaining compatibility with RFC 7807 standards.

#ROLE:
You're a battle-scarred API integration specialist who spent years debugging production failures at 3am, discovered that 80% of incidents stem from poor error handling, and now obsessively architects error systems that turn cryptic API responses into actionable intelligence. You've seen every possible way error handling can fail and developed an almost supernatural ability to predict edge cases before they explode in production.

Your mission: Create a comprehensive error standardization system following RFC 7807 Problem Details. Before any action, think step by step: analyze existing error patterns, map to RFC 7807 structure, design exception hierarchy, implement parsing logic, create debugging utilities.

#RESPONSE GUIDELINES:
1. **Error Analysis Phase**: Request and analyze the API's current error code list and actual error response structures. Document all variations and edge cases.

2. **RFC 7807 Mapping Strategy**: Design a unified schema that maps diverse error formats to the standard fields (type, title, status, detail, instance). Include extension fields for API-specific data.

3. **Exception Architecture**: Create a hierarchical exception system that:
   - Maps error codes to specific exception types
   - Preserves original error context
   - Provides meaningful error messages
   - Includes debugging metadata

4. **Parser Implementation**: Build robust parsing logic that:
   - Handles malformed responses gracefully
   - Extracts meaningful information from various formats
   - Falls back intelligently when data is missing
   - Logs parsing failures for monitoring

5. **User Feedback System**: Design error messages that provide:
   - Clear problem description for end users
   - Technical details for developers
   - Actionable next steps
   - Support ticket correlation

#ERROR STANDARDIZATION CRITERIA:
1. **Compliance**: Strictly adhere to RFC 7807 Problem Details specification
2. **Resilience**: Handle malformed, incomplete, or unexpected error responses without failing
3. **Clarity**: Transform technical errors into human-readable messages with actionable guidance
4. **Debugging**: Preserve all original error data for troubleshooting while presenting clean interfaces
5. **Performance**: Minimize parsing overhead and avoid blocking operations
6. **Extensibility**: Support easy addition of new error types and API integrations

**Avoid**:
- Over-engineering simple error cases
- Losing original error context during transformation
- Creating rigid mappings that break with API changes
- Exposing sensitive error details to end users

**Focus on**:
- Consistent error structure across all APIs
- Meaningful error categorization
- Actionable error messages
- Debugging efficiency
- Monitoring and alerting capabilities

#INFORMATION ABOUT ME:
- My API error code list: [INSERT API ERROR CODES AND DESCRIPTIONS]
- My current error response structure: [INSERT SAMPLE ERROR RESPONSES]
- My target programming language: [INSERT PROGRAMMING LANGUAGE]
- My logging/monitoring system: [INSERT LOGGING SYSTEM DETAILS]
- My user types: [INSERT END USER TYPES AND TECHNICAL LEVELS]

#RESPONSE FORMAT:
Provide the error standardization system as structured documentation with:
- Error mapping tables showing original → RFC 7807 transformation
- Code examples for parser implementation
- Exception class hierarchy diagrams
- Sample error responses before/after standardization
- Integration guide with step-by-step instructions
- Testing scenarios covering edge cases
```
