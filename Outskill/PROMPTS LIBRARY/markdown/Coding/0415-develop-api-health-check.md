---
id: "3b241426-eb50-81c0-95eb-d8307e59800f"
title: "Develop API Health Check"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop API Health Check

**Category:** Coding

## Description

Design a comprehensive API health check with this AI prompt, ensuring robust service availability and traffic routing decisions.

## What This Prompt Does

● Provides a comprehensive API health check implementation for monitoring service availability and making traffic routing decisions.

● Designs robust health check patterns to prevent cascading failures in microservices architectures.

● Includes endpoint validation, response code verification, and intelligent retry logic for handling transient failures.

## Prompt

```text
Adopt the role of an expert DevOps engineer and microservices architect who has spent over a decade building resilient distributed systems at scale. Your primary objective is to create a comprehensive API health check implementation that follows industry best practices for service availability monitoring and traffic routing decisions in a detailed, production-ready format. You specialize in designing robust health check patterns that prevent cascading failures in microservices architectures by implementing proper connectivity validation, authentication verification, and dependency testing before load balancers route traffic to services. Design a complete health check solution that includes endpoint validation, response code verification, optional response body format checking, response time measurement, intelligent retry logic for handling transient failures, and clear status reporting for monitoring systems and load balancers. Take a deep breath and work on this problem step-by-step.

Start by analyzing the specific health check requirements and service dependencies. Create a robust health check function with proper error handling, timeout management, and retry mechanisms. Include comprehensive logging and monitoring integration. Design the solution to handle various failure scenarios gracefully while providing actionable insights for operations teams.

#INFORMATION ABOUT ME:
My health endpoint URL: [INSERT YOUR API HEALTH ENDPOINT URL]
My expected successful status code: [INSERT EXPECTED SUCCESS STATUS CODE]
My programming language preference: [INSERT YOUR PREFERRED PROGRAMMING LANGUAGE]
My monitoring system: [INSERT YOUR MONITORING/ALERTING SYSTEM]
My critical service dependencies: [INSERT KEY DEPENDENCIES TO CHECK]

MOST IMPORTANT!: Structure your response with clear code blocks, implementation steps in bullet points, and include comprehensive error handling patterns for maximum production readiness.
```
