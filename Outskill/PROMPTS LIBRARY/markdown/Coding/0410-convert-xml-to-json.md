---
id: "3b241426-eb50-817a-81ac-f58a6b47d675"
title: "Convert XML to JSON"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Convert XML to JSON

**Category:** Coding

## Description

Analyze XML-to-JSON conversion with this AI prompt, focusing on structured data migration, API integration, and data interoperability.

## What This Prompt Does

● Analyzes XML payload structures to identify patterns, namespaces, and attribute handling requirements.
● Designs conversion rules to map XML elements to JSON keys, ensuring proper array detection and namespace management.
● Generates transformation code with error handling and validation to produce clean, readable JSON output.

## Prompt

```text
Adopt the role of an expert data transformation engineer who specializes in XML-to-JSON conversion with deep expertise in structured data migration, API integration, and cross-platform data interoperability. Your primary objective is to analyze XML payload structures and generate clean, efficient transformation code that preserves data hierarchy while producing JSON that meets modern API standards in a comprehensive step-by-step format. You understand that XML's element-attribute model requires careful mapping to JSON's key-value structure, and you excel at handling complex scenarios like namespaces, mixed content, and array detection. Begin by examining the provided XML samples to identify structural patterns, namespace usage, attribute handling requirements, and potential array scenarios where multiple elements share the same name. Then create transformation logic that converts XML elements to JSON objects, handles attributes as special properties, manages namespaces appropriately, detects and converts arrays correctly, and produces clean JSON output that follows common API conventions. Take a deep breath and work on this problem step-by-step.

Analyze the XML structure for hierarchy depth, attribute usage, namespace declarations, and repeating elements. Design conversion rules that map XML elements to JSON keys, handle attributes using consistent naming conventions, preserve namespace information when needed, and detect array patterns for proper JSON array creation. Generate transformation code with proper error handling, validation steps, and output formatting that produces clean, readable JSON matching industry standards for nested data structures.

#INFORMATION ABOUT ME:
My XML payload samples: [INSERT YOUR XML PAYLOAD EXAMPLES]
My preferred programming language: [INSERT PREFERRED LANGUAGE - Python, JavaScript, etc.]
My target JSON structure requirements: [INSERT ANY SPECIFIC JSON FORMAT REQUIREMENTS]
My namespace handling preference: [INSERT HOW YOU WANT NAMESPACES HANDLED]
My attribute conversion preference: [INSERT HOW YOU WANT XML ATTRIBUTES CONVERTED]

MOST IMPORTANT!: Structure your response with clear headings for analysis, transformation rules, and code implementation. Provide the transformation code in properly formatted code blocks with detailed comments explaining each conversion step.
```
