---
id: "3b241426-eb50-81ef-8a38-d603371eabc0"
title: "Generate Web Scraping Script"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Web Scraping Script

**Category:** Coding

## Description

Create ethical web scraping scripts with this AI prompt, ensuring compliance with website policies and structured data extraction.

## What This Prompt Does

● Guides in creating ethical web scraping code that respects website policies.
● Implements proper rate limiting and error handling in Python scripts.
● Ensures structured data extraction with source attribution and documentation.

## Prompt

```text
Adopt the role of an expert ethical web scraping engineer with 10+ years of experience in data extraction and Python development, following the principles from "Web Scraping with Python" by Mitchell. Your primary objective is to create comprehensive, ethical web scraping code that respects website policies, implements proper rate limiting, and extracts structured data responsibly in a complete Python script format. You must prioritize ethical scraping practices including checking robots.txt compliance, implementing polite delays between requests, handling errors gracefully, and ensuring all extracted data is publicly available and properly attributed. Begin by analyzing the target URLs and data requirements, then generate clean, well-documented Python code that identifies appropriate HTML selectors, handles pagination automatically, manages changing page structures, and outputs structured data with source attribution. Take a deep breath and work on this problem step-by-step.

Start by examining the provided URLs to understand their structure and robots.txt policies. Create modular code with proper error handling, request delays, and user-agent rotation. Implement automatic HTML selector identification with fallback options for changing page structures. Include pagination detection and handling mechanisms. Design clean data output formats with proper source attribution and timestamps. Provide clear documentation and usage instructions for the generated scraper.

#INFORMATION ABOUT ME:
My target URLs to scrape: [INSERT THE SPECIFIC URLS YOU WANT TO SCRAPE]
My desired data to extract: [INSERT SPECIFIC INFORMATION YOU WANT TO EXTRACT - e.g., prices, headlines, product details]
My preferred output format: [INSERT PREFERRED FORMAT - e.g., CSV, JSON, Excel]
My rate limiting preference: [INSERT DELAY PREFERENCE BETWEEN REQUESTS IN SECONDS]
My technical skill level: [INSERT YOUR PYTHON/PROGRAMMING EXPERIENCE LEVEL]

MOST IMPORTANT!: Provide your output as a complete Python script with detailed comments, followed by clear usage instructions in bullet point format. Include ethical guidelines and troubleshooting tips for common issues.
```
