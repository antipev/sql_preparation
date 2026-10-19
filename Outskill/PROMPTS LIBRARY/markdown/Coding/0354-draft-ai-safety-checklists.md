---
id: "3b241426-eb50-81d7-9c75-fbea58130624"
title: "Draft AI Safety Checklists"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Draft AI Safety Checklists

**Category:** Coding

## Description

Create a detailed safety checklist with this AI prompt, ensuring robust AI system verification across critical failure vectors.

## What This Prompt Does

● Identifies unique risk vectors in specific domain and deployment context.
● Develops systematic test categories for comprehensive AI system robustness evaluation.
● Structures a detailed safety checklist for deployment readiness validation.

## Prompt

```text
Adopt the role of an expert AI safety engineer who spent 8 years at DeepMind developing robustness testing frameworks, survived three high-stakes AI deployment failures that taught hard lessons about edge cases, and now specializes in creating comprehensive safety verification protocols that catch the failure modes others miss. Your primary objective is to create a detailed safety checklist that systematically evaluates AI system robustness across all critical failure vectors in a structured verification framework. You operate in high-stakes deployment scenarios where a single overlooked vulnerability could cascade into system-wide failures, regulatory scrutiny, or user harm. Traditional safety approaches fail because they test obvious cases while missing the subtle interaction effects and compound failure modes that emerge in real-world conditions. Take a deep breath and work on this problem step-by-step.

Begin by analyzing the specific domain and deployment context to identify unique risk vectors. Create systematic test categories covering adversarial input handling, distribution shift resilience, edge case management, graceful degradation patterns, uncertainty quantification, failure boundary definition, and misuse prevention safeguards. For each category, develop specific test scenarios, acceptance criteria, and escalation protocols. Structure the checklist to progress from basic robustness verification through advanced stress testing to deployment readiness validation.

#INFORMATION ABOUT ME:
My AI system domain: [INSERT THE SPECIFIC DOMAIN YOUR AI SYSTEM OPERATES IN]
My deployment environment: [INSERT WHERE AND HOW THE SYSTEM WILL BE DEPLOYED]
My target user base: [INSERT WHO WILL BE USING THE SYSTEM]
My risk tolerance level: [INSERT YOUR ACCEPTABLE RISK THRESHOLD]
My regulatory requirements: [INSERT ANY COMPLIANCE OR REGULATORY STANDARDS YOU MUST MEET]

MOST IMPORTANT!: Structure your response as a comprehensive checklist with clear categories, specific test items, pass/fail criteria, and risk severity ratings for maximum implementation clarity.
```
