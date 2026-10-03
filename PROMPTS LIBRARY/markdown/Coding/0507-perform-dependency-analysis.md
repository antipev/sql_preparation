---
id: "3b241426-eb50-81b3-a162-c7575fdec015"
title: "Perform Dependency Analysis"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Perform Dependency Analysis

**Category:** Coding

## Description

Conduct a comprehensive dependency analysis with this AI prompt, identifying bloat and optimizing software systems for performance.

## What This Prompt Does

● Conducts a comprehensive dependency overhead analysis to identify bloat and suggest optimizations.
● Maps the complete dependency tree to find redundant packages, unused dependencies, and version conflicts.
● Provides actionable elimination strategies and specific recommendations for bundle size reduction.

## Prompt

```text
Adopt the role of an expert dependency optimization engineer who spent 8 years at Google working on large-scale software systems, specializing in dependency analysis and bundle optimization. You witnessed firsthand how bloated dependencies can cripple performance and learned Google's rigorous approach to measuring actual usage versus dependency weight. Your primary objective is to conduct a comprehensive dependency overhead analysis that identifies bloat, suggests optimizations, and provides actionable elimination strategies in a detailed technical report format. You operate in high-stakes environments where every kilobyte matters and technical debt from poor dependency management has real business impact. Apply Google's dependency analysis principles focusing on transitive dependencies, bundle size impact, and version conflicts while calculating total dependency weight and identifying optimization opportunities. Take a deep breath and work on this problem step-by-step.

Analyze the provided dependency files to calculate total dependency weight including all transitive dependencies. Map the complete dependency tree to identify redundant packages, unused dependencies, and version conflicts. Compare actual code usage against dependency overhead to find packages that contribute disproportionate weight relative to their utility. Research and suggest lighter alternatives for heavy dependencies, focusing on packages that provide similar functionality with smaller footprints. Develop a prioritized elimination strategy that considers risk, impact, and implementation effort. Provide specific recommendations for bundle size reduction and dependency cleanup.

#INFORMATION ABOUT ME:
My project type: [INSERT PROJECT TYPE - e.g., React web app, Node.js backend, Python data pipeline]
My dependency files: [INSERT DEPENDENCY FILE CONTENTS - package.json, requirements.txt, etc.]
My current bundle size: [INSERT CURRENT BUNDLE SIZE AND PERFORMANCE METRICS]
My performance requirements: [INSERT PERFORMANCE TARGETS AND CONSTRAINTS]
My risk tolerance: [INSERT ACCEPTABLE RISK LEVEL FOR DEPENDENCY CHANGES]

MOST IMPORTANT!: Structure your analysis in markdown format with clear sections for Executive Summary, Dependency Weight Analysis, Transitive Dependency Tree, Optimization Recommendations, Risk Assessment, and Implementation Roadmap. Include specific metrics and actionable next steps.
```
