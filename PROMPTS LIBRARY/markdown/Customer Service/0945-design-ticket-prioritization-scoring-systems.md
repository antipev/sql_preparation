---
id: "3b241426-eb50-80a6-987e-daa9114ce0e1"
title: "Design Ticket Prioritization Scoring Systems"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Design Ticket Prioritization Scoring Systems

**Category:** Customer Service

## Description

Create automated ticket prioritization with this AI prompt, including scoring criteria, weighted formulas, priority thresholds, dynamic adjustments, and calibration processes.

## What This Prompt Does

● Builds a complete ticket prioritization scoring system that assigns numerical scores to support tickets based on weighted criteria.

● Creates scoring rules, priority levels, response time targets, and dynamic adjustments that escalate tickets automatically over time.

● Provides implementation specifications and calibration processes to ensure the AI prompt delivers a working system for support teams.

## Prompt

```text
Adopt the role of an expert support operations analyst and systems architect who has designed ticket prioritization frameworks for high-volume customer support teams across SaaS, e-commerce, and enterprise software companies. Your primary objective is to design a complete, mathematically sound ticket prioritization scoring system that automatically assigns numerical priority scores to incoming support tickets based on weighted, measurable criteria in a comprehensive, implementation-ready format. You understand that manual prioritization collapses under volume, creates inconsistency, and biases toward loud customers rather than actual urgency. You know that effective prioritization requires objective criteria, clear weighting rationale, dynamic adjustments over time, and calibration mechanisms to prevent score inflation. Take a deep breath and work on this problem step-by-step.

Design a five-component ticket prioritization system: (1) Define 6-8 scoring criteria with assigned weights totaling 100%, including customer tier/account value, issue severity, issue scope, time sensitivity, customer sentiment signals, and ticket age - explain the rationale for each weight assignment; (2) Create a 0-100 scoring scale mapped to four priority levels (P1 Critical, P2 High, P3 Medium, P4 Low) with specific score ranges and target response/resolution times for each level, ensuring no more than 20% of tickets fall into P1; (3) Build dynamic score adjustment rules including age-based escalation formulas, re-open penalties, repeat contact bonuses, and VIP override conditions that trigger automatic priority changes; (4) Write a plain-language implementation specification that developers can use to build this system, including the complete scoring formula, required data fields, automation triggers, and update frequency; (5) Define a monthly calibration process with specific metrics to review, questions to ask, and decision criteria for adjusting weights based on actual outcomes.

Ensure all criteria are objectively measurable using data automatically captured by support platforms. Differentiate weights meaningfully rather than distributing them equally. Design the system to prevent priority inflation where too many tickets become "urgent." Avoid subjective criteria that depend on individual interpretation. Include specific formulas, calculation examples, and threshold values throughout.

#INFORMATION ABOUT ME:
- My business description: [INSERT YOUR BUSINESS DESCRIPTION]
- My ticket volume: [INSERT NUMBER] tickets per [DAY/WEEK/MONTH]
- My support channels: [LIST YOUR SUPPORT CHANNELS]
- My current prioritization method: [DESCRIBE YOUR CURRENT METHOD]
- My main prioritization problems: [DESCRIBE YOUR CURRENT PROBLEMS]
- My customer tiers: [LIST YOUR CUSTOMER TIERS]
- My team structure: [DESCRIBE YOUR TEAM STRUCTURE BRIEFLY]
- My support platform: [INSERT YOUR SUPPORT PLATFORM NAME]

MOST IMPORTANT!: Structure your output with clear headings for all five components. Present the scoring criteria in a markdown table with columns for Criterion, Weight (%), Measurement Method, and Rationale. Present the priority level thresholds in a markdown table with columns for Priority Level, Score Range, Target Response Time, and Target Resolution Time. Include the complete scoring formula in a clearly formatted code block or highlighted section. Provide all dynamic adjustment rules as numbered lists with specific formulas where applicable.
```
