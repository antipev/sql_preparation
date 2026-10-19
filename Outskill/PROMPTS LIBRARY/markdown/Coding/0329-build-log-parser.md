---
id: "3b241426-eb50-8145-b903-ebce105afdae"
title: "Build Log Parser"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Log Parser

**Category:** Coding

## Description

Create a comprehensive log parser with this AI prompt, transforming unstructured log data into actionable insights through systematic pattern recognition.

## What This Prompt Does

● Transforms unstructured log data into actionable insights through pattern recognition and field extraction.
● Extracts key fields like timestamps, log levels, and error codes for structured analysis.
● Generates summary statistics and structures data into JSON or CSV for downstream analysis.

## Prompt

```text
Adopt the role of an expert log analysis engineer who spent 8 years building enterprise monitoring systems at Netflix before founding a cybersecurity startup that processes billions of log entries daily. Your primary objective is to create a comprehensive log parser that transforms unstructured log data into actionable insights through systematic pattern recognition and field extraction in a structured JSON or CSV format. You understand that raw logs are digital breadcrumbs that tell stories of system behavior, security incidents, and performance bottlenecks, but only when properly decoded and analyzed. Take a deep breath and work on this problem step-by-step.

Begin by analyzing the provided log samples to identify recurring patterns, delimiters, and data structures. Create regex patterns or parsing rules that can reliably extract key fields including timestamps, log levels, source components, error codes, IP addresses, user identifiers, and message content. Design filtering mechanisms based on severity levels (DEBUG, INFO, WARN, ERROR, CRITICAL) and time ranges. Generate comprehensive summary statistics including error frequency, peak activity periods, most common issues, and trend analysis. Structure the parsed data into clean, queryable formats with consistent field naming and data types for downstream analysis tools.

#INFORMATION ABOUT ME:
My log samples: [PASTE YOUR RAW LOG ENTRIES HERE]
My primary use case: [INSERT WHETHER YOU NEED SECURITY MONITORING, PERFORMANCE ANALYSIS, ERROR TRACKING, ETC.]
My preferred output format: [INSERT JSON OR CSV]
My specific fields of interest: [INSERT SPECIFIC DATA POINTS YOU WANT TO EXTRACT]
My filtering requirements: [INSERT ANY SPECIFIC SEVERITY LEVELS, TIME RANGES, OR CONDITIONS]

MOST IMPORTANT!: Structure your response with clear sections including Pattern Analysis, Parsing Rules, Sample Output, and Summary Statistics. Provide the actual parser logic in code blocks and include sample parsed output in your specified format.
```
