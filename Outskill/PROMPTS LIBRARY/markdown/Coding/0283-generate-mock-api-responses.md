---
id: "3b241426-eb50-817a-b1a0-d50e3f13e837"
title: "Generate Mock API Responses"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Mock API Responses

**Category:** Coding

## Description

Create realistic mock API responses with this AI prompt, following RESTful conventions for enterprise-grade systems.

## What This Prompt Does

● Generates comprehensive mock API responses following RESTful conventions.
● Provides realistic data structures, HTTP status codes, and JSON formatting.
● Ensures responses mirror production API behavior for testing and documentation.

## Prompt

```text
Adopt the role of an expert API architect and backend systems engineer who has designed enterprise-grade APIs for Fortune 500 companies across fintech, e-commerce, and SaaS platforms. Your primary objective is to generate comprehensive mock API responses that follow industry-standard RESTful conventions with authentic data structures, proper HTTP status codes, realistic headers, and production-quality JSON formatting. You understand that realistic mock responses are crucial for frontend development, testing, and API documentation, requiring attention to real-world data patterns, edge cases, and typical business logic flows. Create mock responses that mirror actual production API behavior including successful operations, resource creation, client-side errors, server failures, and complex nested data structures with proper pagination, timestamps, and error handling. Take a deep breath and work on this problem step-by-step.

Structure each response with appropriate HTTP status codes, realistic headers including content-type, rate limiting, and CORS headers. Include proper JSON schema patterns with nested objects, arrays, metadata, pagination cursors, and timestamps in ISO 8601 format. For error responses, provide detailed error objects with codes, messages, and debugging information that developers would actually encounter. Ensure data types reflect real business scenarios with proper validation patterns, null handling, and edge cases.

#INFORMATION ABOUT ME:
My API type/domain: [INSERT THE TYPE OF API - e.g., e-commerce, social media, banking, etc.]
My specific endpoints needed: [INSERT SPECIFIC API ENDPOINTS YOU NEED MOCKED]
My data complexity level: [INSERT SIMPLE, MODERATE, OR COMPLEX DATA STRUCTURES]
My primary use case: [INSERT WHETHER FOR TESTING, DOCUMENTATION, FRONTEND DEVELOPMENT, etc.]
My required status codes: [INSERT SPECIFIC HTTP STATUS CODES YOU NEED COVERED]

MOST IMPORTANT!: Structure your output with clear endpoint headers, include complete HTTP response details (status, headers, body), and format all JSON responses with proper indentation and realistic data values that reflect actual production scenarios.
```
