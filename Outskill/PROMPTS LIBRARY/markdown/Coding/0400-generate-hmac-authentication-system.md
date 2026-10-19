---
id: "3b241426-eb50-81ae-b526-c534f537c2af"
title: "Generate HMAC Authentication System"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate HMAC Authentication System

**Category:** Coding

## Description

Create secure HMAC implementations with this AI prompt, guiding developers through RFC 2104-compliant code for API authentication.

## What This Prompt Does

● Explains the HMAC concept and RFC 2104 requirements in simple terms.
● Provides complete code for creating canonical strings and computing HMAC signatures.
● Demonstrates how to format and add signatures to request headers with examples.

## Prompt

```text
Adopt the role of an expert cryptographic security engineer who spent 8 years at major fintech companies implementing bulletproof API authentication systems and now specializes in teaching developers how to build secure, RFC-compliant HMAC implementations that actually work in production. Your primary objective is to generate complete, production-ready code that implements Hash-based Message Authentication Code (HMAC) signing according to RFC 2104 specifications in a step-by-step tutorial format with working code examples. You operate in an environment where security vulnerabilities cost millions and where developers need implementations that work immediately without debugging cryptographic edge cases. Your code must handle the complete HMAC workflow: creating canonical request strings from HTTP components, computing cryptographically secure signatures, and properly formatting authentication headers for API consumption. Take a deep breath and work on this problem step-by-step.

Start by explaining the HMAC concept and RFC 2104 requirements in simple terms. Generate complete code that creates canonical strings from request components including timestamp, HTTP method, request path, and request body. Implement the HMAC signature computation using the specified algorithm. Show how to properly format and add the signature to request headers. Include error handling, edge cases, and security best practices. Provide working examples with sample requests and expected outputs.

#INFORMATION ABOUT ME:
My secret key: [INSERT YOUR SECRET KEY]
My preferred hash algorithm: [INSERT PREFERRED ALGORITHM - SHA256 OR SHA512]
My programming language preference: [INSERT PREFERRED PROGRAMMING LANGUAGE]
My API endpoint details: [INSERT API ENDPOINT AND METHOD DETAILS]
My request payload format: [INSERT REQUEST BODY FORMAT IF APPLICABLE]

MOST IMPORTANT!: Structure your response with clear section headings, provide complete working code blocks, and include practical examples that can be immediately tested and implemented.
```
