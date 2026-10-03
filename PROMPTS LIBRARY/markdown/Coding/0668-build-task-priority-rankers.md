---
id: "3b241426-eb50-805f-9189-cf5c226553fa"
title: "Build Task Priority Rankers"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Task Priority Rankers

**Category:** Coding

## Description

Create a sophisticated Task Priority Ranker with this AI prompt, designed to streamline decision-making and enhance productivity.

## What This Prompt Does

● Provides a structured approach to building a sophisticated Task Priority Ranker application.

● Utilizes weighted scoring algorithms to objectively rank tasks by priority.

● Adapts real-time prioritization to changing conditions, reducing decision fatigue.

## Prompt

```text
<context>
You are working with someone who needs a production-ready Task Priority Ranker application that cuts through decision fatigue and analysis paralysis. This isn't about simple to-do lists - you're building an intelligent system that uses weighted scoring algorithms to objectively rank tasks by true priority. The person is likely overwhelmed by competing deadlines and needs a sophisticated tool that feels like having a personal productivity coach, with enterprise-grade interface design and real-time prioritization that adapts as conditions change.
</context>

<role>
Adopt the role of an expert product engineer and cognitive psychology specialist tasked with building intelligent productivity systems. Your primary objective is to create a complete Task Priority Ranker application that uses multi-factor scoring algorithms to rank tasks objectively in a single-file React artifact format that's immediately usable and production-ready.
</role>

<information_about_me>
- My preferred visual style: [INSERT DESIGN PREFERENCES - CLEAN/ENTERPRISE/COLORFUL/MINIMAL]
- My typical task volume: [INSERT AVERAGE NUMBER OF TASKS YOU MANAGE DAILY/WEEKLY]
- My work environment: [INSERT WHETHER YOU WORK SOLO/TEAM/CORPORATE/STARTUP]
- My priority factors: [INSERT WHAT MATTERS MOST - DEADLINES/IMPACT/EFFORT/DEPENDENCIES]
- My technical preferences: [INSERT ANY SPECIFIC REQUIREMENTS OR CONSTRAINTS]
</information_about_me>

<output>
Create a single-file React TypeScript application with these core components:
● Task Input Interface: Quick-add form with name, deadline, impact slider (1-10), effort slider (1-10), and dependency tags
● Intelligent Scoring Engine: Priority calculation using formula: (Impact × Urgency Weight) - (Effort × 0.3) + Dependency Bonus
● Dynamic Ranking Display: Auto-sorted task cards with color-coded priorities (Red/Orange/Yellow/Green) and smooth reorder animations
● Customization Panel: Adjustable weight sliders and preset modes ("Deadline Driven", "Impact Focused", "Quick Wins")
● Interaction Features: One-click completion, keyboard shortcuts, data persistence, and mobile responsiveness

Technical Requirements:
● React 18+ with TypeScript, Tailwind CSS, Framer Motion for animations
● Urgency weights: Due today = 10x, This week = 5x, This month = 2x, Later = 1x
● Visual groupings: "Do Now" (top 3), "Do Today" (next 5), "Schedule Later" (rest)
● LocalStorage persistence, keyboard shortcuts (n/1-9/x), swipe-to-complete on mobile

Take a deep breath and work on this problem step-by-step. Provide clean, commented code that's immediately functional with zero configuration required.
</output>
```
