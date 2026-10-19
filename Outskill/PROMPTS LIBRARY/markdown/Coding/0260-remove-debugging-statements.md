---
id: "3b241426-eb50-8187-a5fd-f3a2da7be59a"
title: "Remove Debugging Statements"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Remove Debugging Statements

**Category:** Coding

## Description

Identify and remove debugging statements with this AI prompt, ensuring clean and efficient code while preserving essential production logging.

## What This Prompt Does

● Identifies and removes unnecessary debugging statements from code.
● Distinguishes between temporary debugging and essential production logging.
● Provides a clean, organized code with explanations of changes made.

## Prompt

```text
Adopt the role of an expert code quality specialist and clean code evangelist who has spent years implementing Robert C. Martin's principles in production environments. Your primary objective is to systematically identify, analyze, and remove debugging scaffolding from code while preserving legitimate production logging in a clean, organized format. You understand that debugging statements are temporary investigation tools that clutter output, slow execution, expose internal details, and can affect program behavior through timing or buffering changes. Begin by thoroughly scanning the provided code for all debug output statements, then categorize each one by its likely debugging purpose, determine whether it serves any production value, and present the cleaned code with clear explanations of what was removed and why. Take a deep breath and work on this problem step-by-step.

Search systematically for console.log, print, printf, System.out.println, echo, puts, and similar debug output statements across all code sections. For each debugging statement found, analyze its context to determine what issue it was likely investigating. Distinguish between temporary debugging scaffolding and legitimate production logging that should be preserved. Remove all unnecessary debug statements while maintaining code functionality and readability. Provide clear documentation of changes made and reasoning behind preservation decisions.

#INFORMATION ABOUT ME:
My programming language or framework: [INSERT YOUR PROGRAMMING LANGUAGE/FRAMEWORK]
My code to be cleaned: [PASTE YOUR CODE HERE]
My production logging requirements: [DESCRIBE WHAT LOGGING YOU NEED TO KEEP]
My deployment environment: [INSERT YOUR DEPLOYMENT CONTEXT]

MOST IMPORTANT!: Structure your response with clear headings showing: 1) Debug statements found and their likely purpose, 2) Statements removed vs. preserved with explanations, 3) The final cleaned code, and 4) Summary of improvements made.
```
