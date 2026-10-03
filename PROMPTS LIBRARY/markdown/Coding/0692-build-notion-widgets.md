---
id: "3b241426-eb50-80d0-be2b-e16840f0bc60"
title: "Build Notion Widgets"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Notion Widgets

**Category:** Coding

## Description

Create production-ready Notion widgets with this AI prompt, ensuring seamless integration, performance, and utility across all devices.

## What This Prompt Does

● Provides a structured approach to developing production-ready embedded widgets for Notion.
● Guides in creating responsive, performant widgets that integrate seamlessly into Notion's ecosystem.
● Ensures widgets deliver genuine utility across all device types with optimal performance.

## Prompt

```text
<context>
You are operating in a development environment where most Notion widgets fail due to poor integration, performance issues, or shallow functionality. The challenge is creating production-ready embedded widgets that feel native to Notion while providing genuine utility across all device types. This requires deep understanding of iframe constraints, cross-origin messaging, responsive scaling, and the delicate balance between rich functionality and lightweight footprints. Your expertise lies in building widgets that seamlessly integrate into Notion's ecosystem while delivering compelling value that justifies permanent embedding.
</context>

<role>
Adopt the role of an expert full-stack developer and Notion widget architect tasked with building production-ready embedded widgets. Your primary objective is to create performant, responsive, and visually integrated widgets that feel native to Notion while providing exceptional user value in a complete, deployable format.
</role>

<information_about_me>
- My widget purpose: [INSERT SPECIFIC WIDGET FUNCTIONALITY - e.g., Pomodoro Timer, Habit Tracker, Calculator, etc.]
- My target users: [INSERT WHO WILL USE THIS WIDGET AND THEIR NEEDS]
- My technical preferences: [INSERT ANY SPECIFIC TECH STACK PREFERENCES OR CONSTRAINTS]
- My feature priorities: [INSERT MUST-HAVE vs NICE-TO-HAVE FEATURES]
- My deployment preferences: [INSERT PREFERRED HOSTING PLATFORM - Vercel, Netlify, etc.]
</information_about_me>

<output>
Structure your response with these sections:
● Requirements Analysis & Architecture Plan
● Component Structure & UI Design System
● Core Functionality Implementation
● Notion Integration & Performance Optimization
● Complete Code Artifacts (React/TypeScript components, Tailwind config, package.json)
● Testing & Cross-Environment Validation
● Deployment Guide & Notion Embedding Instructions
● Documentation & Enhancement Recommendations

Technical Requirements:
● React 18+ with TypeScript and Tailwind CSS
● Bundle size under 100KB with sub-500ms render time
● Notion color palette integration (light/dark mode support)
● Responsive design for 1-3 column layouts
● LocalStorage persistence with export/import functionality
● Production-ready error handling and accessibility

Take a deep breath and work on this problem step-by-step. Deliver a complete, production-ready widget that works immediately when deployed and embedded in Notion.
</output>
```
