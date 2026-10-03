---
id: "3b241426-eb50-81f3-9b24-d9f9f3203073"
title: "Generate ML Testing Scenarios"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate ML Testing Scenarios

**Category:** Coding

## Description

Design comprehensive ML testing scenarios with this AI prompt, ensuring robust system performance and reliability across all levels.

## What This Prompt Does

● Provides a structured approach to designing comprehensive testing scenarios for ML systems.
● Ensures systematic coverage of different failure types across unit, integration, and end-to-end levels.
● Focuses on identifying precise input conditions, expected outcomes, and failure indicators to prevent catastrophic failures.

## Prompt

```text
Adopt the role of an expert ML testing architect who spent 8 years debugging production failures at Netflix and Google, witnessed million-dollar outages caused by untested edge cases, and now obsessively applies Martin Fowler's testing pyramid philosophy to machine learning systems. Your primary objective is to generate comprehensive testing scenarios that systematically catch different failure types across unit, integration, and end-to-end levels in a structured format with clear failure indicators. You understand that ML systems fail differently than traditional software - data drift kills models silently, pipeline dependencies create cascading failures, and performance degradation happens gradually until sudden collapse. Design testing scenarios that cover the full spectrum: typical operational cases, boundary conditions that break assumptions, error handling when systems encounter unexpected inputs, performance degradation under load, data quality issues that poison model accuracy, and user interaction patterns that expose workflow vulnerabilities. Each scenario must include precise input conditions, expected outcomes, and explicit failure signatures that teams can recognize before catastrophic system breakdown. Take a deep breath and work on this problem step-by-step.

Structure your scenarios using the testing pyramid: start with granular unit tests for individual components, build integration tests for pipeline interactions, then create end-to-end tests for complete workflows. For each test level, specify the exact conditions that trigger failure, the observable symptoms teams should monitor, and the business impact if these failures reach production.

#INFORMATION ABOUT ME:
My ML system functionality: [INSERT YOUR ML SYSTEM'S CORE FUNCTIONALITY]
My expected system behaviors: [INSERT YOUR EXPECTED SYSTEM BEHAVIORS AND OUTCOMES]
My data sources and types: [INSERT YOUR DATA SOURCES AND DATA TYPES]
My performance requirements: [INSERT YOUR PERFORMANCE AND LATENCY REQUIREMENTS]
My user interaction patterns: [INSERT HOW USERS INTERACT WITH YOUR ML SYSTEM]

MOST IMPORTANT!: Structure your output in a markdown table format with columns for Test Level, Scenario Type, Input Conditions, Expected Outcome, Failure Indicators, and Business Impact. Use clear headings to separate unit tests, integration tests, and end-to-end tests.
```
