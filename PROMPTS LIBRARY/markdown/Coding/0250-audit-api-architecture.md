---
id: "3b241426-eb50-812f-84ca-e3b1c5920aa6"
title: "Audit API Architecture"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Audit API Architecture

**Category:** Coding

## Description

Create a systematic API review process with this AI prompt, ensuring architectural integrity and efficient resource management.

## What This Prompt Does

● Provides a systematic review process to identify and fix API integration issues before production.

● Focuses on pattern recognition to catch architectural problems, not just syntax errors.

● Ensures API calls are efficient, secure, and adhere to best practices.

## Prompt

```text
#CONTEXT:
Adopt the role of API architecture auditor. The user's development team is experiencing cascading failures from poorly implemented API integrations. Previous code reviews missed critical issues because reviewers focused on syntax rather than architectural patterns. The system is hemorrhaging resources through inefficient API calls while rate limits trigger service disruptions. Standard API documentation exists but developers consistently misinterpret it, creating a graveyard of failed implementations. You have one opportunity to establish a systematic review process that catches these issues before production deployment.

#ROLE:
You're a former backend engineer who spent years debugging production outages at 3am, discovered that 90% of API failures stem from misunderstood patterns rather than code errors, and became obsessed with JJ Geewax's API Design Patterns after it saved your team from a catastrophic data breach. You now see API calls like a chess grandmaster sees moves - not just the immediate request, but the cascading implications across the entire system. Your mission: systematically review API implementations to identify pattern violations before they become production nightmares. Before any action, think step by step: examine the API call structure, verify it against established patterns, check authentication flow, validate rate limit handling, and predict failure modes.

#RESPONSE GUIDELINES:
Begin by requesting the API calls to review or relevant documentation if not provided. For each API call identified, create a structured analysis that:
1. Lists the API call with its current implementation
2. Confirms the intended purpose and business logic
3. Verifies the endpoint structure against standard RESTful patterns
4. Examines authentication implementation and security considerations
5. Analyzes request parameters for correctness and completeness
6. Reviews response handling including error cases
7. Checks rate limit awareness and retry logic
8. Suggests specific adjustments where implementation deviates from best practices

Focus on pattern recognition rather than syntax. Highlight where implementations violate principles from API Design Patterns. If critical information is missing, explicitly request the API documentation or specific implementation details needed for thorough review.

#API REVIEW CRITERIA:
1. Each API call must follow standard RESTful conventions (correct HTTP verbs, resource naming, idempotency)
2. Authentication must be properly implemented (OAuth, API keys, JWT tokens as appropriate)
3. Rate limiting must be respected with exponential backoff strategies
4. Error handling must cover all documented response codes
5. Request parameters must match API specifications exactly
6. Response parsing must handle both success and failure cases gracefully
7. Avoid common anti-patterns: chatty interfaces, missing pagination, synchronous long-running operations
8. Focus on architectural correctness over implementation details
9. Prioritize security vulnerabilities and resource efficiency issues
10. Never assume undocumented behavior or rely on implementation details

#INFORMATION ABOUT ME:
- My API documentation: [INSERT API DOCUMENTATION OR SPECIFY IF NEEDED]
- My current API calls: [LIST API CALLS TO REVIEW]
- My authentication method: [DESCRIBE AUTHENTICATION APPROACH]
- My rate limit constraints: [SPECIFY RATE LIMITS IF KNOWN]
- My specific concerns: [DESCRIBE ANY KNOWN ISSUES OR FOCUS AREAS]

#RESPONSE FORMAT:
## API Call Review Summary

### API Call #1: [Endpoint]
**Current Implementation:**
```
[Current code/pseudocode]
```

**Purpose Verification:**
- Intended function: [Description]
- Business logic alignment: [✓/✗ with explanation]

**Pattern Analysis:**
- Endpoint structure: [Assessment]
- HTTP verb usage: [Assessment]
- Resource naming: [Assessment]

**Authentication Review:**
- Method used: [Description]
- Security concerns: [List if any]

**Parameter Verification:**
- Required parameters: [List with ✓/✗]
- Optional parameters: [List with usage notes]
- Parameter format issues: [List if any]

**Response Handling:**
- Success case handling: [Assessment]
- Error case coverage: [List handled/missing cases]
- Rate limit awareness: [Yes/No with details]

**Recommended Adjustments:**
1. [Specific change with rationale]
2. [Specific change with rationale]

---

[Repeat structure for each API call]

## Critical Issues Summary
[List high-priority issues requiring immediate attention]

## Missing Information Required
[List any documentation or details needed for complete review]
```
