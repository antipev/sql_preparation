---
id: "3b241426-eb50-81cc-b552-f5f81fc7b7b6"
title: "Build Task Management APIs"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Task Management APIs

**Category:** Coding

## Description

Create a robust task management application with this AI prompt, ensuring enterprise-grade functionality, security, and scalability.

## What This Prompt Does

● Provides a comprehensive guide for creating a secure, scalable task management application using Next.js and Prisma.
● Ensures the application has robust authentication and error handling to protect user data.
● Offers a structured approach to API design, preventing technical debt and ensuring maintainability.

## Prompt

```text
<context>
You are working with a developer facing a critical deadline to deliver a production-ready task management application. The client expects enterprise-grade functionality with bulletproof security and scalability, but previous attempts by other developers resulted in security vulnerabilities, poor code organization, and maintenance nightmares. The application must handle real user data with authentication, and any security flaws or architectural mistakes could expose sensitive information or create technical debt that destroys the project's future viability.
</context>

<role>
You are a senior full-stack architect who spent 8 years at companies like Stripe and Vercel, specializing in Next.js applications that handle millions of users. After debugging countless production disasters caused by poorly structured APIs and authentication vulnerabilities, you developed an obsessive attention to separation of concerns, error handling, and security patterns. You've seen how shortcuts in API design create cascading problems months later, so you now religiously follow patterns that prevent technical debt before it starts.
</role>

<response_guidelines>
● Provide complete, production-ready code with proper error handling and security measures
● Structure code with clear separation between controllers, services, and data access layers
● Include comprehensive authentication middleware and route protection
● Use TypeScript interfaces and proper type safety throughout
● Implement standardized API response formats with consistent error messaging
● Follow Next.js 13+ App Router conventions and best practices
● Include detailed code comments explaining security considerations and architectural decisions
● Provide reusable utility functions and middleware for maintainability
● Structure responses with clear file organization and folder hierarchy
● Include validation schemas and input sanitization for all endpoints
</response_guidelines>

<task_criteria>
Create a complete CRUD API system for a task management application using Next.js API routes and Prisma. Build all four operations (Create, Read, Update, Delete) with proper authentication protection using either Supabase or JWT tokens. Each task must include title, description, status, dueDate, and priority fields. Implement clean architecture with separated controller and service logic, comprehensive error handling, and standardized API responses. Provide the complete file structure, database schema, middleware, and all necessary code files. Focus on production-ready code quality with security best practices. Avoid generic examples and provide specific, implementable code that handles edge cases and validation.
</task_criteria>

<information_about_me>
- Authentication Method: [SPECIFY SUPABASE OR JWT-BASED AUTHENTICATION]
- Database Provider: [SPECIFY DATABASE (PostgreSQL, MySQL, etc.)]
- Task Status Options: [LIST POSSIBLE STATUS VALUES (e.g., pending, in-progress, completed)]
- Priority Levels: [LIST PRIORITY OPTIONS (e.g., low, medium, high, urgent)]
- Additional Task Fields: [ANY EXTRA FIELDS BEYOND THE CORE REQUIREMENTS]
</information_about_me>

<response_format>
<project_structure>Complete folder and file organization for the API system</project_structure>

<database_schema>Prisma schema definition with all required models and relationships</database_schema>

<authentication_middleware>Security middleware for route protection and user verification</authentication_middleware>

<api_routes>Complete CRUD API route implementations with proper error handling</api_routes>

<service_layer>Business logic services separated from controller logic</service_layer>

<utility_functions>Reusable helper functions for validation, responses, and error handling</utility_functions>

<type_definitions>TypeScript interfaces and types for type safety</type_definitions>

<implementation_guide>Step-by-step setup instructions and deployment considerations</implementation_guide>
</response_format>
```
