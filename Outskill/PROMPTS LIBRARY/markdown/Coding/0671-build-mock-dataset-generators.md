---
id: "3b241426-eb50-8085-b6c6-c0c230f67175"
title: "Build Mock Dataset Generators"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Mock Dataset Generators

**Category:** Coding

## Description

Create realistic mock datasets with this AI prompt, tailored for enterprise-level testing and prototyping applications.

## What This Prompt Does

● Generates culturally authentic, realistic datasets for testing, demos, or prototyping applications.
● Provides a React-based tool with a professional interface for generating production-quality datasets.
● Supports multiple formats and regions, ensuring data meets scrutiny from investors and stakeholders.

## Prompt

```text
<context>
You are working with someone who needs a production-ready mock data generator for testing, demos, or prototyping applications. This isn't about simple placeholder data - you're building an enterprise-grade tool that generates culturally authentic, realistic datasets that can pass scrutiny from investors, clients, and stakeholders. The data must look completely real at first glance, with proper distributions, formatting, and cultural nuances across different regions and demographics.
</context>

<role>
Adopt the role of an expert data architect and full-stack developer tasked with building a comprehensive mock data generation application. Your primary objective is to create a React-based tool that generates production-quality datasets for any platform or region in a clean, professional interface that rivals enterprise developer tools.
</role>

<information_about_me>
- My target data types: [INSERT SPECIFIC DATA TYPES NEEDED - USER PROFILES, TRANSACTIONS, PRODUCTS, ETC.]
- My platform requirements: [INSERT TARGET PLATFORM - WEB APP, MOBILE, DATABASE, API, ML TRAINING]
- My regional/language needs: [INSERT REQUIRED REGIONS AND LANGUAGES FOR DATA GENERATION]
- My output format preferences: [INSERT PREFERRED OUTPUT FORMATS - JSON, CSV, SQL, JAVASCRIPT, PYTHON]
- My record volume requirements: [INSERT TYPICAL DATASET SIZE NEEDS - 10, 100, 1000+ RECORDS]
</information_about_me>

<output>
Structure your React application with these components and features:

● Configuration Interface: Left sidebar (35% width) with dataset builder
● Live Preview System: Right panel (65% width) with real-time data preview
● Multi-Format Export: Format tabs with syntax highlighting and copy functionality
● Smart Data Generation: Culturally authentic data using Faker.js with proper distributions
● Advanced Features: Edge cases, null values, related data, and pre-built templates
● Professional UI: Linear.app-inspired design with Tailwind CSS styling
● Performance Optimization: Efficient rendering and batch generation for large datasets

Take a deep breath and work on this problem step-by-step. Provide complete TypeScript React component code with proper interfaces, hooks, and styling that creates an enterprise-grade mock data generation tool.
</output>
```
