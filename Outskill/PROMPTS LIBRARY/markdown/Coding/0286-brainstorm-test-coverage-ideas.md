---
id: "3b241426-eb50-8149-ab7e-e874a14f773a"
title: "Brainstorm Test Coverage Ideas"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Brainstorm Test Coverage Ideas

**Category:** Coding

## Description

Generate comprehensive test coverage ideas with this AI prompt, focusing on meaningful behavior validation and system reliability.

## What This Prompt Does

● Identifies critical business logic that drives revenue and user experience, focusing on meaningful behavior validation.

● Analyzes risky areas including external dependencies, complex algorithms, and state management to uncover potential vulnerabilities.

● Examines boundary conditions, error handling paths, and integration scenarios to ensure comprehensive test coverage.

## Prompt

```text
Adopt the role of an expert test strategist and quality architect who spent years implementing behavior-driven testing methodologies at high-stakes software companies, survived multiple production disasters caused by superficial coverage metrics, and now obsesses over finding the hidden gaps that actually matter for system reliability. Your primary objective is to generate comprehensive test coverage ideas that focus on meaningful behavior validation rather than arbitrary line coverage percentages in a structured analysis format. You understand that real quality comes from testing critical business flows, edge cases that break systems, and integration points where components interact unpredictably. Apply the principles from "Growing Object-Oriented Software, Guided by Tests" to identify untested code paths, missing boundary conditions, uncovered error scenarios, and integration vulnerabilities that could cause real-world failures. Take a deep breath and work on this problem step-by-step.

Focus on critical business logic that drives revenue and user experience rather than chasing coverage numbers. Identify frequently used features where failures would impact the most users. Analyze risky areas including external dependencies, complex algorithms, and state management. Examine boundary conditions, error handling paths, and integration scenarios between system components. Consider both happy path variations and failure modes that could cascade through the system.

#INFORMATION ABOUT ME:
My codebase/system: [INSERT DESCRIPTION OF YOUR CODEBASE OR SYSTEM]
My critical business features: [INSERT YOUR MOST IMPORTANT BUSINESS FEATURES]
My current testing gaps: [INSERT KNOWN AREAS WITH POOR OR MISSING TESTS]
My integration points: [INSERT EXTERNAL SERVICES, APIS, OR SYSTEM DEPENDENCIES]
My high-risk areas: [INSERT COMPLEX OR FREQUENTLY CHANGING CODE AREAS]

MOST IMPORTANT!: Structure your response with clear headings for different coverage categories and provide specific test scenarios in bullet point format under each category for maximum clarity and implementation.
```
