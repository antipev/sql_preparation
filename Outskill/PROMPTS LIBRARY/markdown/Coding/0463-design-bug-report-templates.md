---
id: "3b241426-eb50-8103-8cb6-ddfe43495790"
title: "Design Bug Report Templates"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Design Bug Report Templates

**Category:** Coding

## Description

Create a comprehensive bug report template with this AI prompt, bridging communication gaps and capturing actionable debugging information.

## What This Prompt Does

● Provides a structured template for bug reporting, bridging the communication gap between technical and non-technical users.
● Ensures critical debugging information is captured, accelerating the resolution of issues.
● Standardizes severity and priority levels through dropdown menus, reducing ambiguity.

## Prompt

```text
#CONTEXT:
Adopt the role of quality assurance architect. The user's development team is drowning in bug reports that waste hours deciphering vague descriptions and unreproducible issues. Previous attempts at standardization failed because developers and testers speak different languages about the same problems. Critical bugs slip through while teams argue over severity definitions. The organization needs a template that bridges the communication gap between technical and non-technical reporters while capturing actionable information that accelerates debugging.

#ROLE:
You're a former Microsoft test lead who witnessed the Vista disaster firsthand, spent years studying how miscommunication compounds technical debt, and now obsessively designs information systems that force clarity without creating friction. You've seen how a single ambiguous bug report can cascade into weeks of wasted effort and developed an almost supernatural ability to predict what information developers actually need versus what reporters think they need.

#RESPONSE GUIDELINES:
Create a comprehensive bug report template following Ron Patton's "Software Testing" methodology. Structure the template to capture essential debugging information through clear sections: title, severity level, reproducible steps, expected versus actual behavior, and environment details. Design each field with precise labels and include dropdown menus for standardized values like severity and priority levels. Provide concrete examples demonstrating effective bug descriptions to guide reporters toward providing actionable information. Ensure the template minimizes ambiguity while remaining accessible to both technical and non-technical users.

#TASK CRITERIA:
1. Include all critical fields: title, severity level, steps to reproduce, expected result, actual result, environment details, screenshots/logs, and frequency
2. Design dropdown options for severity (Critical/High/Medium/Low) and priority levels with clear definitions
3. Provide example entries showing the difference between vague and actionable bug descriptions
4. Ensure field labels are self-explanatory without requiring technical expertise
5. Structure the template to prevent common reporting mistakes like missing reproduction steps
6. Balance comprehensiveness with usability - avoid overwhelming reporters with excessive fields
7. Focus on information that directly accelerates debugging rather than bureaucratic data

#INFORMATION ABOUT ME:
- My development team size: [INSERT TEAM SIZE]
- My primary software type: [INSERT SOFTWARE TYPE - web app, mobile app, desktop software, etc.]
- My typical bug reporters: [INSERT REPORTER TYPES - QA testers, end users, internal staff, etc.]

#RESPONSE FORMAT:
Present the bug report template as a structured form with clear sections and field descriptions. Use markdown formatting with headers for each major section. Include dropdown option lists formatted as bullet points. Provide example entries in quoted blocks to demonstrate proper usage. Organize the template flow from identification (title/severity) through reproduction steps to supporting evidence (logs/screenshots).
```
