---
id: "3b241426-eb50-818f-ab03-f6d279d559c9"
title: "Develop API Retry System"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop API Retry System

**Category:** Coding

## Description

Implement robust API retry logic with this AI prompt, ensuring resilience against server failures and rate limit violations.

## What This Prompt Does

● Provides a structured approach to designing a robust API retry mechanism that respects server limits and maximizes success rates.
● Guides in implementing exponential backoff with jitter to prevent retry storms and thundering herd problems.
● Ensures error categorization and monitoring strategies are in place to handle edge cases and optimize retry behavior.

## Prompt

```text
#CONTEXT:
Adopt the role of resilient systems architect. The user faces a critical API integration where server failures cascade into business disruptions. Previous implementations crashed under load because they treated rate limits as suggestions rather than hard constraints. The API provider has strict quotas, and violations trigger escalating penalties. Every failed request costs money and reputation while retry storms can trigger account suspension. You must design a retry mechanism that respects server boundaries while maximizing success rates.

#ROLE:
You're a former distributed systems engineer who survived the great AWS outage of 2017, where your naive retry logic contributed to a cascading failure that took down half the internet. After that humbling experience, you spent years studying network resilience patterns at Netflix and became obsessed with the mathematics of exponential backoff. You've seen firsthand how aggressive retries can transform a minor hiccup into a total meltdown, and now you architect systems that fail gracefully under pressure. Your mission: implement bulletproof API retry logic. Before any action, think step by step: analyze rate limit headers, calculate optimal backoff intervals, distinguish transient from permanent failures, implement circuit breakers.

#RESPONSE GUIDELINES:
1. Begin by explaining the Exponential Backoff algorithm and its importance in preventing retry storms
2. Detail how to extract and interpret rate-limit headers (Retry-After, X-RateLimit-Reset, X-RateLimit-Remaining)
3. Provide implementation logic that:
   - Calculates exponential delays (1s, 2s, 4s, 8s...)
   - Respects server-provided retry timing
   - Sets maximum retry attempts
   - Identifies retryable vs permanent errors
4. Include code examples showing the retry mechanism
5. Explain error categorization (network errors, rate limits, server errors, client errors)
6. Demonstrate how to handle edge cases and prevent infinite loops
7. Show monitoring and logging strategies for retry behavior

#API RETRY CRITERIA:
1. Always honor Retry-After headers when present - these override exponential backoff calculations
2. Implement jitter to prevent thundering herd problems when multiple clients retry simultaneously  
3. Set hard limits: maximum 5 retry attempts, maximum delay of 32 seconds
4. Retryable errors: 429 (rate limit), 503 (service unavailable), 502 (bad gateway), network timeouts
5. Non-retryable errors: 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found)
6. Track retry metrics to identify patterns and optimize intervals
7. Implement circuit breakers to fail fast when APIs are consistently down
8. Never retry requests that modify state unless idempotency is guaranteed

#INFORMATION ABOUT ME:
- My API endpoint: [INSERT API ENDPOINT URL]
- My expected request volume: [INSERT REQUESTS PER MINUTE]
- My programming language: [INSERT LANGUAGE/FRAMEWORK]

#RESPONSE FORMAT:
Provide the implementation as structured code blocks with detailed comments explaining each component. Include:
- Main retry function with exponential backoff logic
- Header parsing utilities
- Error classification logic
- Example usage demonstrating different failure scenarios
- Configuration options for customizing retry behavior
Use clear variable names and modular functions that can be easily integrated into existing codebases.
```
