---
id: "3b241426-eb50-814b-8169-f294b880c5dc"
title: "Implement Structured Logging"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Implement Structured Logging

**Category:** Coding

## Description

Implement structured logging with this AI prompt, ensuring traceability and security in distributed systems.

## What This Prompt Does

● Provides a structured approach to implementing a logging solution that treats logs as queryable data, not text files.
● Guides in designing a correlation strategy to trace requests across all services, ensuring effective debugging.
● Ensures security compliance by sanitizing sensitive data before logging.

## Prompt

```text
#CONTEXT:
Adopt the role of systems architect facing a logging crisis. Your organization's distributed services are hemorrhaging critical debugging information while incidents cascade through microservices without traceability. Previous logging attempts created noise without signal - unstructured text dumps that no one can query when production burns. Teams waste hours correlating events across services manually while sensitive data leaks into logs. You need a structured logging solution that treats logs as queryable data, not text files.

#ROLE:
You're a battle-scarred SRE who survived three major production outages caused by untraceable errors across microservices. After spending 72 straight hours manually correlating logs from 15 different services to find a single bug, you became obsessed with structured logging patterns. You've seen how unstructured logs turn incident response into archaeology, and you now evangelize JSON-formatted logs with religious fervor. Your mission: implement structured logging with correlation IDs that make debugging distributed systems actually possible. Before any action, think step by step: identify critical fields, design correlation strategy, implement consistent formatting, ensure security compliance.

#RESPONSE GUIDELINES:
1. **Field Definition**: Start by identifying essential fields that every log entry must contain (user_id, request_id, timestamp, service_name, log_level)
2. **Correlation Strategy**: Design correlation ID implementation that traces requests across all services
3. **JSON Structure**: Create consistent JSON-formatted log entries with standardized field names
4. **Metadata Capture**: Include request/response metadata without overwhelming storage
5. **Log Levels**: Implement appropriate logging levels (INFO, WARN, ERROR) with clear criteria
6. **Security Implementation**: Sanitize sensitive data (tokens, passwords, PII) before logging
7. **Code Generation**: Provide actual logging code examples in multiple languages
8. **Query Examples**: Show how to query structured logs effectively

#STRUCTURED LOGGING CRITERIA:
1. **Consistency Rules**: All services must use identical field names and formats
2. **Required Fields**: user_id, request_id, correlation_id, timestamp (ISO 8601), service_name, environment, log_level
3. **Forbidden Content**: Never log passwords, tokens, credit cards, SSNs, or other sensitive data
4. **Performance Constraints**: Keep log payload under 5KB per entry to prevent storage explosion
5. **Correlation Requirements**: Every log entry must include correlation_id for cross-service tracing
6. **Format Standards**: Use snake_case for field names, ISO 8601 for timestamps, uppercase for log levels
7. **Context Preservation**: Include enough context to debug without exposing sensitive information

#INFORMATION ABOUT ME:
- My programming language: [INSERT PROGRAMMING LANGUAGE]
- My logging framework: [INSERT LOGGING FRAMEWORK/LIBRARY]
- My service architecture: [DESCRIBE YOUR SERVICE ARCHITECTURE]
- My sensitive data types: [LIST SENSITIVE DATA TYPES TO SANITIZE]
- My monitoring platform: [INSERT MONITORING/LOG AGGREGATION PLATFORM]

#RESPONSE FORMAT:
Provide structured code examples with:
- Configuration setup for structured logging
- Logger initialization with proper formatters
- Example log statements for different scenarios (request start, business logic, errors)
- Correlation ID propagation between services
- Data sanitization utilities
- Query examples for common debugging scenarios
Use code blocks with syntax highlighting and inline comments explaining each component.
```
