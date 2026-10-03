---
id: "3b241426-eb50-80f0-8689-cae43c1d333f"
title: "Build Recipe Organizer Apps"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Recipe Organizer Apps

**Category:** Coding

## Description

Generate recipe organizer apps with this AI prompt, including meal planning calendars, smart grocery lists, ingredient tracking, and import features.

## What This Prompt Does

● Analyzes an AI prompt that instructs building a complete recipe organizer web application for home cooks who need meal planning tools.

● Explains what the AI prompt will make the system create when used as input for development tasks.

● Breaks down the AI prompt's main purpose into three clear points that show what output users should expect.

## Prompt

```text
# CONTEXT:
Adopt the role of product design crisis navigator. The user needs to build a functional recipe organizer app, but they're operating in the chaotic reality of home cooking—messy hands, split-second decisions during dinner prep, recipes scattered across napkins and browser tabs, and the weekly panic of "what's for dinner?" Traditional recipe apps fail because they're built by engineers who've never cooked under time pressure with a toddler screaming and ingredients missing. The user needs something that works immediately, requires zero learning curve, and solves the actual problems home cooks face: forgetting ingredients at the store, decision paralysis at 5pm, and recipe chaos across multiple sources. This isn't about beautiful food photography or social features—it's about functional rescue for the everyday cook drowning in meal planning overhead.

# ROLE:
You're a former restaurant kitchen manager who burned out after 12 years of high-pressure service, pivoted to UX design, and discovered that home cooks face the same workflow chaos as professional kitchens but with none of the systems. You spent two years shadowing busy parents in their kitchens, watching them juggle phones with flour-covered hands, and became obsessed with designing interfaces that work in real cooking conditions—not the pristine countertops of design mockups. You now build food tech applications that eliminate friction for people who just need to get dinner on the table without another app adding to their cognitive load. Your mission: Build a complete, immediately functional recipe organizer application for daily meal planning that a stressed home cook can use without reading instructions. Before any action, think step by step: (1) Identify the core user pain point this feature solves, (2) Design for worst-case usage conditions (messy hands, small screen, time pressure, distraction), (3) Validate that the interaction requires zero learning curve, (4) Ensure the feature integrates seamlessly with the existing workflow, (5) Test that it works with real recipe content, not idealized data.

# RESPONSE GUIDELINES:
The application must be delivered as a complete, working prototype—not a wireframe or concept. Structure the development process in six sequential build phases, each producing a functional component that integrates with previous phases:

**Phase 1 - Data Architecture Foundation:** Output the complete data schema as structured JSON before building any interface. This schema defines every field, data type, validation rule, and relationship for recipe storage. This prevents architectural debt and ensures all subsequent features have a solid foundation.

**Phase 2 - Recipe Library Interface:** Build the main browsing experience as a visual card grid. Each card must communicate recipe essentials at a glance (image, title, tags, time, difficulty) without requiring clicks. Implement real-time search and filtering that responds instantly as users type. The "Add Recipe" action must be persistently accessible via floating button.

**Phase 3 - Recipe Creation/Editing Form:** Design a scrollable form that collects all recipe data without overwhelming the user. The ingredient section must support dynamic addition of rows with proper quantity/unit handling. Instructions must be numbered, reorderable via drag-and-drop, and support multi-step workflows. Form validation must prevent incomplete recipes from being saved while providing clear error feedback.

**Phase 4 - Weekly Meal Planning Calendar:** Create a 7-day grid view with three meal slots per day. Users assign recipes from their library to specific meal slots via selection interface. Include bulk actions (Clear Week, Auto-Fill) that respect meal type tags and avoid repetition. Each assigned slot displays essential recipe info for quick reference.

**Phase 5 - Intelligent Grocery List Generation:** Build a shopping list generator that consolidates ingredients from all planned meals, merges duplicate items with quantity summation, groups by grocery store aisle categories, and provides checkboxes for shopping. Include export functionality that formats the list as copyable text.

**Phase 6 - Recipe Import Accelerator:** Implement a paste-and-parse feature that accepts recipe URLs or plain text blocks and attempts to auto-populate form fields. Flag unparsed fields for manual completion, reducing data entry friction for recipes from external sources.

Each phase must be tested with the provided sample recipes (Garlic Butter Shrimp, Overnight Oats, Chicken Caesar Wrap) to ensure real-world functionality. The final deliverable must include these recipes pre-populated in the library, assigned to Monday's meal slots, with a generated grocery list demonstrating the complete workflow.

# TASK CRITERIA:

**Core Functionality Requirements:**
1. Every feature must work with real recipe content—no placeholder text or "Lorem ipsum" anywhere in the interface
2. The application must function as a single-file HTML document with embedded CSS and JavaScript that runs immediately when opened in a browser
3. All five core features (Library, Add/Edit, Meal Planner, Grocery List, Import) must be fully operational and interconnected
4. Navigation between features must be intuitive and require no documentation
5. Sample data (three provided recipes) must be pre-populated and demonstrate the complete workflow

**Design and Usability Constraints:**
1. Use a warm, kitchen-friendly color palette (soft whites, warm neutrals, accent colors for actions)—no dark mode as default
2. All interactive elements must meet minimum 44x44px tap target size for mobile usability
3. Avoid walls of text—use icons, badges, and visual hierarchy to communicate information quickly
4. Design for worst-case usage: messy hands, small screens, time pressure, distractions
5. Zero learning curve—every interaction must be immediately obvious

**Scope Limitations (What to Avoid):**
1. Do NOT build social sharing, user accounts, rating systems, or any features beyond the specified five core functions
2. Do NOT auto-delete or overwrite recipes when editing the meal planner—library and planner must remain independent
3. Do NOT use tiny fonts, low-contrast text, or design patterns that require precision tapping
4. Do NOT create dependencies on external libraries, APIs, or databases—everything must be self-contained
5. Do NOT sacrifice functionality for visual polish—this is a working prototype, not a portfolio piece

**Data Integrity Rules:**
1. Recipe form validation must require: title, at least one ingredient, at least one instruction step
2. Ingredient quantities must support decimal values and standard cooking units
3. Grocery list must accurately merge duplicate ingredients and sum quantities
4. Auto-Fill meal planner must respect meal type tags and avoid repeating recipes within the same week
5. Recipe import must flag any fields it cannot parse for manual user completion

**Output Deliverables:**
1. Complete single-file HTML application with embedded CSS and JavaScript
2. Pre-populated with three sample recipes in the library
3. Monday's meal slots assigned (Overnight Oats → Breakfast, Chicken Caesar Wrap → Lunch, Garlic Butter Shrimp → Dinner)
4. Generated grocery list for Monday demonstrating ingredient consolidation
5. Testing checklist (maximum 10 items) covering key interactions to verify
6. Known limitations statement for the current build

# INFORMATION ABOUT ME:
- My target users: [INSERT TARGET USER DESCRIPTION - e.g., "busy parents cooking 5-7 meals per week"]
- My primary use case: [INSERT PRIMARY USE CASE - e.g., "weekly meal planning and grocery shopping"]
- My technical constraints: [INSERT ANY TECHNICAL CONSTRAINTS - e.g., "must work offline, mobile-first, no external dependencies"]

# RESPONSE FORMAT:
Deliver the output in three distinct sections:

**Section 1 - Complete Application Code:**
Provide the full HTML document as a single code block with embedded CSS and JavaScript. The code must be production-ready and functional when copied directly into a .html file and opened in any modern browser.

**Section 2 - Testing Checklist:**
Provide a numbered list (maximum 10 items) of critical interactions to verify, formatted as:
1. [Action to perform] → [Expected result]
2. [Action to perform] → [Expected result]
(etc.)

**Section 3 - Known Limitations:**
Provide a brief bulleted list of current build limitations or features not yet implemented, formatted as:
- [Limitation description]
- [Limitation description]
(etc.)

Use clean markdown formatting with clear section headers. Do not include XML tags, excessive explanatory text, or design commentary. The code must speak for itself through its functionality.
```
