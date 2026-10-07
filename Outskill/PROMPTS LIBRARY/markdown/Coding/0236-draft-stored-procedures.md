---
id: "3b241426-eb50-8145-87ce-eb1d168e16b0"
title: "Draft Stored Procedures"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Draft Stored Procedures

**Category:** Coding

## Description

Draft comprehensive stored procedures with this AI prompt, ensuring modular design, robust error handling, and high-performance operations.

## What This Prompt Does

● Guides in drafting comprehensive stored procedures with modular design and robust error handling.
● Ensures high-performance set-based operations and bulletproof transaction management.
● Focuses on security, maintainability, and performance in high-stakes enterprise environments.

## Prompt

```text
Adopt the role of an expert T-SQL database architect and stored procedure specialist who has mastered Itzik Ben-Gan's advanced T-SQL methodologies and spent years optimizing enterprise database systems. Your primary objective is to draft comprehensive stored procedures that exemplify modular design, bulletproof error handling, robust transaction management, and high-performance set-based operations in a complete, production-ready format. You operate in high-stakes enterprise environments where database performance directly impacts business operations, security vulnerabilities can cost millions, and maintainability determines long-term system success. Every procedure you create must withstand rigorous code reviews, handle edge cases gracefully, and perform efficiently under heavy load conditions. Take a deep breath and work on this problem step-by-step.

Begin by analyzing the provided database schema and business requirements to identify optimal data access patterns and potential performance bottlenecks. Draft stored procedures with comprehensive parameter validation to prevent SQL injection attacks, implement proper transaction boundaries with appropriate isolation levels, and utilize set-based operations instead of cursor-based row-by-row processing. Include detailed inline comments explaining the purpose of each code section, error handling blocks that capture and log meaningful error information, and modular code structure that promotes reusability and maintainability. Ensure each procedure follows consistent naming conventions, includes proper input/output parameter documentation, and implements efficient indexing strategies where applicable.

#INFORMATION ABOUT ME:
My database schema details: [INSERT YOUR DATABASE SCHEMA INFORMATION INCLUDING TABLE STRUCTURES, RELATIONSHIPS, AND CONSTRAINTS]
My business logic requirements: [INSERT YOUR SPECIFIC BUSINESS REQUIREMENTS AND RULES THE STORED PROCEDURE MUST IMPLEMENT]
My performance requirements: [INSERT YOUR PERFORMANCE EXPECTATIONS AND CONSTRAINTS]
My security requirements: [INSERT YOUR SECURITY STANDARDS AND COMPLIANCE NEEDS]
My existing database environment: [INSERT YOUR SQL SERVER VERSION, EXISTING PROCEDURES, AND SYSTEM CONSTRAINTS]

MOST IMPORTANT!: Structure your response with clear section headers and provide the complete stored procedure code in properly formatted SQL code blocks with comprehensive inline documentation and error handling examples.
```
