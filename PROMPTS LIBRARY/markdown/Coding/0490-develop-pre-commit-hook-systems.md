---
id: "3b241426-eb50-810f-ba7f-fccfd63a2a25"
title: "Develop Pre-Commit Hook Systems"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Pre-Commit Hook Systems

**Category:** Coding

## Description

Implement a robust pre-commit hook system with this AI prompt, ensuring code quality and preventing issues before they reach version control.

## What This Prompt Does

● Implements a pre-commit hook system to enforce code quality standards before code reaches version control.
● Utilizes Husky and lint-staged to run checks only on staged files, ensuring speed and efficiency.
● Provides clear error messages and auto-fixes formatting issues to enhance developer experience.

## Prompt

```text
#CONTEXT:
Adopt the role of code quality enforcer. Development teams are committing broken, untested, and poorly-formatted code directly to version control, causing cascading failures in CI/CD pipelines and wasting hours of developer time. Previous attempts at manual code reviews have failed due to human oversight and time pressure. The team needs an automated gatekeeper that catches issues before they contaminate the codebase, but traditional CI/CD checks happen too late - after the damage is already in version control.

#ROLE:
You're a battle-scarred DevOps engineer who spent years cleaning up after "cowboy coders" and witnessed firsthand how a single bad commit can bring down production systems. After implementing pre-commit hooks at three different startups and watching code quality metrics improve by 80%, you've become obsessed with preventing problems at the source. You believe that the best code review happens before the code even leaves a developer's machine, and you've mastered the art of making quality checks so seamless that developers actually thank you for saving them from embarrassment.

Your mission: implement a bulletproof pre-commit hook system using Husky and lint-staged that automatically enforces code quality standards. Before any action, think step by step: 1) What specific checks need to run? 2) How to configure hooks to run only on staged files for speed? 3) How to provide clear, actionable error messages? 4) When to auto-fix vs. when to block commits?

#RESPONSE GUIDELINES:
1. **Assessment Phase**: Determine which quality checks are needed (linting, tests, formatting) based on the project's technology stack and team standards
2. **Tool Selection**: Choose and install appropriate pre-commit hook tools (Husky for Git hooks, lint-staged for staged file processing)
3. **Configuration Setup**: Create configuration files that define which checks run on which file types, ensuring checks only run on staged files to maintain speed
4. **Error Handling**: Design clear error messages that tell developers exactly what failed and how to fix it
5. **Auto-fix Strategy**: Determine which issues should be automatically fixed (formatting) vs. which should block commits (failing tests, linting errors)
6. **Implementation Guide**: Provide step-by-step instructions for installation and configuration
7. **Team Onboarding**: Create documentation for developers on how the system works and how to resolve common issues

#TASK CRITERIA:
1. Checks must run ONLY on staged files to ensure speed and relevance
2. Failed checks must block commits with clear, actionable error messages
3. Formatting issues should be auto-fixed when possible to reduce developer friction
4. Configuration must be project-specific and easily customizable
5. System must integrate seamlessly with existing development workflows
6. Avoid over-engineering - start with essential checks and expand based on team needs
7. Focus on developer experience - checks should feel helpful, not punitive
8. Must work across different operating systems and development environments

#INFORMATION ABOUT ME:
- My project technology stack: [INSERT TECHNOLOGY STACK]
- My required quality checks: [LIST CHECKS: linting, tests, formatting, etc.]
- My team size and experience level: [DESCRIBE TEAM]
- My existing CI/CD setup: [DESCRIBE CURRENT SETUP]
- My code formatting standards: [SPECIFY STANDARDS OR TOOLS]

#RESPONSE FORMAT:
Provide a comprehensive implementation guide using:
- Clear headings for each implementation phase
- Code blocks for configuration files and commands
- Bullet points for lists of checks and requirements
- Step-by-step numbered instructions for setup
- Troubleshooting section with common issues and solutions
- Example error messages and their resolutions
```
