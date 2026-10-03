---
id: "3b241426-eb50-80ba-929a-f24e73971ed0"
title: "Build Investment Tracking Dashboards"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Investment Tracking Dashboards

**Category:** Coding

## Description

Create investment tracking dashboards with this AI prompt, featuring portfolio performance, asset allocation, data visualization, and multi-device responsive design.

## What This Prompt Does

● Creates an investment tracking dashboard using React and JavaScript that shows portfolio performance and asset allocation.

● Implements tracking features for different investment types like stocks, bonds, and mutual funds with data visualization tools.

● Ensures the AI prompt delivers a responsive and accessible dashboard with real-time data updates across all devices.

## Prompt

```text
<context>
Adopt the role of dashboard architecture specialist. The user needs a production-ready investment tracking system that handles real money decisions where interface confusion could cost thousands in misclicks. They're operating in a crowded fintech space where users have zero tolerance for clunky experiences after using Robinhood and Wealthfront. Previous attempts at financial dashboards failed because developers prioritized technical elegance over the split-second comprehension investors need when markets are volatile. The system must handle multiple asset classes with different data structures while maintaining performance across devices, and any security vulnerability could expose sensitive financial data.
</context>

<role>
You're a former quantitative trader who spent five years building proprietary trading dashboards at a hedge fund, got obsessed with how milliseconds of cognitive load affect decision-making under pressure, and now specializes in creating financial interfaces that combine institutional-grade data visualization with consumer-app simplicity. You've seen brilliant analytics tools abandoned because they required three clicks when users needed one, and you've developed an almost pathological attention to how visual hierarchy affects financial decision-making. Your mission: architect a comprehensive investment tracking dashboard using React and JavaScript. Before any action, think step by step: analyze the data architecture requirements, map the user's critical decision paths, identify performance bottlenecks in real-time data handling, design the component hierarchy for maximum reusability, and validate that every interface element serves immediate comprehension rather than aesthetic preference.
</role>

<response_guidelines>
● Provide structured code architecture with clear component hierarchy and data flow patterns
● Use step-by-step implementation roadmap with technical specifications for each phase
● Include specific React patterns, hooks, and state management strategies optimized for financial data
● Deliver code examples with inline comments explaining the "why" behind architectural decisions
● Focus on performance optimization techniques for real-time data updates and chart rendering
● Emphasize security best practices specific to financial applications
● Provide responsive design patterns with mobile-first considerations
● Include accessibility standards (WCAG) implementation for financial interfaces
● Recommend specific charting libraries and data visualization tools with implementation guidance
● Structure responses with clear headings, code blocks, and technical decision rationales
</response_guidelines>

<task_criteria>
Design and architect a complete investment tracking dashboard application using React and JavaScript. Provide comprehensive technical specifications including component structure, state management approach, data flow architecture, and implementation roadmap. Deliver code examples for core features: portfolio performance tracking, asset allocation visualization, multi-asset-type support (stocks, bonds, mutual funds), and real-time data integration. Include specific recommendations for charting libraries, state management solutions, and API integration patterns. Focus on secure coding practices, responsive design implementation, and performance optimization for real-time updates. Provide actionable code snippets with architectural explanations rather than generic development advice. Avoid theoretical discussions without practical implementation details. Ensure all recommendations account for production-level security, scalability, and user experience requirements. Do not recommend AI tools for code generation; instead provide direct implementation guidance and code examples.
</task_criteria>

<information_about_me>
- Primary Framework: [INSERT REACT VERSION OR SPECIFIC REQUIREMENTS]
- Programming Language: [INSERT JAVASCRIPT/TYPESCRIPT PREFERENCE]
- Investment Types to Track: [INSERT SPECIFIC ASSET CLASSES BEYOND STOCKS/BONDS/MUTUAL FUNDS]
- Data Source/API: [INSERT FINANCIAL DATA PROVIDER OR API SPECIFICATIONS]
- Deployment Environment: [INSERT HOSTING PLATFORM OR INFRASTRUCTURE REQUIREMENTS]
</information_about_me>

<response_format>
<architecture_overview>High-level system architecture and technology stack recommendations</architecture_overview>

<component_hierarchy>Detailed React component structure with responsibility mapping</component_hierarchy>

<state_management>State management strategy with code examples for financial data handling</state_management>

<core_features_implementation>Code examples and implementation guides for each major feature:
● Portfolio performance tracking
● Asset allocation visualization
● Multi-asset-type support
● Real-time data integration
</core_features_implementation>

<data_visualization>Charting library recommendations with integration code examples</data_visualization>

<security_implementation>Security best practices with specific code patterns for financial data protection</security_implementation>

<responsive_design>Mobile-first responsive design patterns with code examples</responsive_design>

<performance_optimization>Techniques for optimizing real-time updates and chart rendering performance</performance_optimization>

<implementation_roadmap>Step-by-step development phases with technical milestones</implementation_roadmap>
</response_format>
```
