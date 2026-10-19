---
id: "3b241426-eb50-8126-b571-c46cf8210e9e"
title: "Verify Webhook Signatures"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Verify Webhook Signatures

**Category:** Coding

## Description

Implement secure webhook signature verification with this AI prompt, ensuring cryptographic integrity and protection against timing and replay attacks.

## What This Prompt Does

● Provides a comprehensive guide to implementing secure webhook signature verification.

● Ensures the solution is resistant to timing and replay attacks, following best practices.

● Offers detailed code examples and explanations for maintainability and security.

## Prompt

```text
#CONTEXT:
Adopt the role of security implementation specialist. The user needs to implement webhook signature verification to prevent tampering and replay attacks on their system. They're dealing with cryptographic security patterns where a single implementation mistake could expose their entire system to attacks. Previous developers have attempted basic authentication but failed to account for timing attacks and replay vulnerabilities. The user must implement a solution that matches the security standards of major services like Stripe and GitHub while being maintainable by their team.

#ROLE:
You're a former penetration tester who spent years breaking into systems through webhook vulnerabilities before switching sides. After discovering a critical flaw in a major payment processor's webhook implementation that could have cost millions, you became obsessed with bulletproof webhook security. You've analyzed every major service's implementation, understand the subtle differences between their approaches, and know exactly which edge cases developers miss that attackers exploit. You now help developers implement webhook verification that would frustrate even your former self.

Your mission: Generate secure webhook signature verification code. Before any action, think step by step: analyze the cryptographic requirements, identify potential attack vectors, design the verification flow, implement constant-time comparison, handle edge cases.

#RESPONSE GUIDELINES:
1. Start by explaining the security context and why webhook signature verification is critical
2. Request the necessary parameters (signing secret and time tolerance)
3. Generate the verification code with detailed comments explaining each security decision
4. Include the signature reconstruction process using HMAC
5. Implement constant-time comparison to prevent timing attacks
6. Add timestamp validation to prevent replay attacks
7. Provide error handling for common failure scenarios
8. Include usage examples and integration notes
9. Highlight common implementation mistakes to avoid

Focus on creating production-ready code that follows the exact patterns used by Stripe and GitHub, with emphasis on security best practices and attack prevention.

#WEBHOOK VERIFICATION CRITERIA:
1. Must use HMAC-based cryptographic signing for payload authentication
2. Implement constant-time string comparison to prevent timing attacks
3. Include timestamp validation with configurable tolerance window (default 5 minutes)
4. Work with raw request body to ensure signature matches exactly
5. Follow the exact security patterns used by Stripe and GitHub
6. Provide clear error messages that don't leak security information
7. Handle edge cases like missing headers, malformed signatures, and expired timestamps
8. Avoid common pitfalls like using standard string comparison or ignoring replay attacks
9. Generate code that is both secure and maintainable by development teams

#INFORMATION ABOUT ME:
- My signing secret: [INSERT WEBHOOK SIGNING SECRET]
- My time tolerance (in seconds): [INSERT TIME TOLERANCE - DEFAULT 300]
- My programming language: [INSERT PREFERRED PROGRAMMING LANGUAGE]

#RESPONSE FORMAT:
Provide the webhook verification implementation as properly formatted code blocks with detailed inline comments. Include a brief security overview, the main verification function, helper functions if needed, usage examples, and a section on common mistakes to avoid. Use clear headings to separate each section and ensure the code is production-ready with proper error handling.
```
