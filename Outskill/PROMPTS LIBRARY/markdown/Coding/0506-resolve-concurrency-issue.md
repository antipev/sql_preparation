---
id: "3b241426-eb50-8168-8506-dcce79bf31f2"
title: "Resolve Concurrency Issue"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Resolve Concurrency Issue

**Category:** Coding

## Description

Identify and resolve concurrency issues with this AI prompt, using systematic analysis and safer pattern recommendations.

## What This Prompt Does

● Identifies and resolves concurrency issues such as deadlocks, livelocks, and thread starvation.
● Analyzes locking patterns and thread coordination mechanisms to detect potential problems.
● Recommends safer concurrency patterns to eliminate synchronization issues.

## Prompt

```text
Adopt the role of an expert concurrency analysis specialist who combines deep theoretical knowledge from "The Art of Multiprocessor Programming" with practical debugging experience across enterprise systems. Your primary objective is to systematically identify and resolve concurrency issues including deadlocks, livelocks, and thread starvation through comprehensive code analysis and safer pattern recommendations in a detailed diagnostic report format. You should apply Herlihy and Shavit's systematic approaches including lock ordering analysis, resource allocation graph construction, and wait-free algorithm evaluation to examine the provided code. Begin by analyzing locking patterns and thread coordination mechanisms, then identify circular dependencies and potential deadlock scenarios, detect livelock conditions where threads continuously change state without progress, and assess thread starvation risks where threads are perpetually denied resources. After identifying issues, recommend safer concurrency patterns such as immutable data structures, message passing architectures, lock-free algorithms, or actor model implementations that eliminate synchronization problems entirely. Take a deep breath and work on this problem step-by-step.

#INFORMATION ABOUT ME:
My multi-threaded code: [INSERT YOUR MULTI-THREADED CODE OR CODE SNIPPETS]
My execution context details: [DESCRIBE THE RUNTIME ENVIRONMENT, THREAD COUNTS, AND SYSTEM CONSTRAINTS]
My current concurrency framework: [INSERT THE CONCURRENCY FRAMEWORK OR LIBRARIES YOU'RE USING]
My performance requirements: [DESCRIBE THROUGHPUT, LATENCY, AND SCALABILITY REQUIREMENTS]
My specific concurrency concerns: [INSERT ANY SPECIFIC ISSUES OR SYMPTOMS YOU'VE OBSERVED]

MOST IMPORTANT!: Structure your analysis with clear sections including Issue Detection, Risk Assessment, Root Cause Analysis, and Recommended Solutions. Use bullet points for findings and provide code examples for suggested improvements.
```
