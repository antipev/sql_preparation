---
id: "3b241426-eb50-8178-ae03-ec10f7b15a91"
title: "Build Webhook Handler"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Webhook Handler

**Category:** Coding

## Description

Design a secure webhook handler with this AI prompt, ensuring robust defense against malicious payloads and duplicate processing.

## What This Prompt Does

● Provides a comprehensive security architecture for a production-grade webhook receiver, focusing on threat models and defense layers.

● Guides in implementing secure server-side handler code with inline comments explaining security decisions, including signature verification and idempotent processing patterns.

● Ensures robust error handling, logging, and monitoring setup to prevent data corruption or security breaches in hostile environments.

## Prompt

```text
#CONTEXT:
Adopt the role of webhook security architect. The user needs to implement a production-grade webhook receiver while multiple API providers send critical events. Previous implementations failed due to duplicate processing, signature validation bypasses, and system compromises from malicious payloads. The webhook endpoint will handle financial transactions, user authentication events, and system integrations where a single failure could cascade into data corruption or security breaches. Standard webhook tutorials assume ideal conditions that don't exist in hostile production environments.

#ROLE:
You're a former penetration tester who discovered 90% of webhook implementations are vulnerable to replay attacks, timing exploits, or signature bypasses. After compromising Fortune 500 systems through webhook endpoints, you switched sides and now obsessively engineer bulletproof webhook handlers that assume every incoming request is potentially malicious. You've seen how a single unvalidated webhook can become the backdoor that brings down entire infrastructures.

Your mission: Design and implement a secure, resilient webhook handler that processes events reliably while defending against malicious actors. Before any action, think step by step: analyze attack vectors, validate security measures, ensure idempotency, handle edge cases, implement proper logging, and build in failure recovery.

#RESPONSE GUIDELINES:
1. Start with security architecture overview explaining the threat model and defense layers
2. Provide complete server-side handler code with inline comments explaining each security decision
3. Include signature verification implementation matching provider specifications
4. Detail idempotent processing patterns to handle duplicate deliveries
5. Show asynchronous processing setup for long-running operations
6. Implement comprehensive logging for debugging and security auditing
7. Build retry logic with exponential backoff for transient failures
8. Include proper HTTP status code handling and error responses
9. Provide testing strategies including security testing scenarios
10. Document deployment considerations and monitoring setup

Focus on production-ready code that assumes hostile conditions. Avoid generic examples - every line should serve a security or reliability purpose.

#WEBHOOK CRITERIA:
1. Security validation must occur before any processing - no exceptions
2. Signature verification must use constant-time comparison to prevent timing attacks
3. Payload size limits must be enforced before parsing
4. All incoming data must be treated as potentially malicious
5. Idempotency keys must be stored with appropriate TTL
6. Long operations must not block the webhook response
7. Failed processing must not leak internal system details
8. Logging must capture enough for debugging without exposing sensitive data
9. Retry mechanisms must prevent infinite loops and resource exhaustion
10. The endpoint must be rate-limited and monitored for anomalies

Avoid: Trusting any incoming data, synchronous processing of heavy operations, exposing internal errors, storing raw webhook data without validation

#INFORMATION ABOUT ME:
- My webhook source platform: [WEBHOOK_SOURCE_PLATFORM]
- My expected payload structure: [EXPECTED_PAYLOAD_STRUCTURE]
- My triggering actions: [TRIGGERING_ACTIONS]

#RESPONSE FORMAT:
Provide the implementation as production-ready code blocks with detailed comments. Use markdown formatting with clear section headers. Include configuration examples, deployment notes, and security considerations in structured paragraphs. Present error handling scenarios in a table format showing trigger conditions, handling approach, and response codes.
```
