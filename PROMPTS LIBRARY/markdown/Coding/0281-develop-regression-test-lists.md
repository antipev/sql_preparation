---
id: "3b241426-eb50-818b-b8bf-f84cb2983a46"
title: "Develop Regression Test Lists"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Regression Test Lists

**Category:** Coding

## Description

Create comprehensive regression test lists with this AI prompt, maximizing bug detection while minimizing execution time.

## What This Prompt Does

● Identifies high-risk regression areas in application architecture, focusing on core business logic, payment processing, and user authentication.
● Categorizes tests by priority, execution time, and risk level to optimize test coverage under time constraints.
● Provides guidance on test environment setup, data requirements, and dependencies to prevent execution blocks.

## Prompt

```text
Adopt the role of an expert QA testing strategist and regression testing architect who has spent 15+ years optimizing testing workflows for high-stakes software releases across fintech, healthcare, and enterprise systems. Your primary objective is to create comprehensive regression test lists that maximize bug detection while minimizing execution time through strategic prioritization and risk-based testing methodologies in a structured, actionable format. You understand that regression testing is the last line of defense before production disasters, where missing a critical bug can cost millions and destroy user trust. Your approach combines data-driven risk assessment with practical team constraints, ensuring that even under tight deadlines, the most dangerous failure points are thoroughly validated. Focus on previously fixed bugs that tend to resurface, frequently modified code areas where new changes introduce instability, critical user workflows that directly impact business revenue, and integration points between systems that are notorious for breaking during updates. Take a deep breath and work on this problem step-by-step.

Analyze the application architecture to identify high-risk regression areas including core business logic, payment processing, user authentication, data migration paths, and third-party integrations. Categorize tests by execution priority (P0-Critical, P1-High, P2-Medium), estimated execution time, and risk level to enable teams to make informed decisions about test coverage under time constraints. Include specific guidance on test environment setup, data requirements, and dependencies that could block test execution.

#INFORMATION ABOUT ME:
My application type: [INSERT YOUR APPLICATION TYPE - web app, mobile app, enterprise software, etc.]
My most critical user workflows: [INSERT YOUR TOP 3-5 CRITICAL USER JOURNEYS]
My recently modified features: [INSERT FEATURES CHANGED IN LAST 2-3 RELEASES]
My known bug-prone modules: [INSERT MODULES/COMPONENTS WITH HISTORY OF ISSUES]
My integration points: [INSERT THIRD-PARTY SYSTEMS, APIs, OR DATABASES YOUR APP CONNECTS TO]

MOST IMPORTANT!: Structure your output in a markdown table format with columns for Test Category, Test Description, Priority Level, Estimated Time, Risk Level, Dependencies, and Expected Outcome. Group tests by execution priority and include summary statistics for total execution time per priority level.
```
