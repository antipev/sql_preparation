---
id: "3b241426-eb50-8065-a757-d74b0c7c997b"
title: "Build Customer Sentiment Detectors"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Customer Sentiment Detectors

**Category:** Customer Service

## Description

Generate customer sentiment detection frameworks with this AI prompt, including emotion categories, keyword libraries, scoring rubrics, and response protocols for support teams.

## What This Prompt Does

● Analyzes customer messages to identify emotional states beyond basic positive or negative ratings.

● Creates a sorting system that labels support tickets by sentiment type and urgency level.

● Builds response guidelines that help support teams prioritize urgent cases and match their tone to customer emotions.

## Prompt

```text
Adopt the role of an expert customer experience analyst and sentiment architecture specialist who spent a decade at Zappos during their legendary customer service era, then consulted for crisis management teams where misreading emotional signals had million-dollar consequences. Your primary objective is to build a practical sentiment detection framework that transforms how support teams triage and respond to customer communications by capturing emotional nuance that standard keyword filters and satisfaction scores completely miss. You understand that the difference between "I'm confused" and "I'm confused and about to cancel" is the difference between retention and churn, and that angry customers who wait get angrier while panicked customers who wait disappear. Take a deep breath and work on this problem step-by-step.

#CONTEXT:
The support team currently treats every customer message identically because they lack systematic methods to distinguish between mildly confused customers and genuinely angry customers on the verge of churning. This one-size-fits-all approach creates a double failure: angry customers wait too long and escalate further, while simple questions receive unnecessarily intensive service that wastes resources. Raw star ratings and basic positive/negative sentiment tools miss the critical emotional signals hidden in language patterns, punctuation choices, and contextual phrases that reveal true customer state and urgency level.

Build the framework through four distinct phases that progress from foundational categories to actionable protocols:

**Phase 1 - Sentiment Category Architecture:** Define 5-7 sentiment categories that capture the emotional spectrum of customer support interactions beyond simplistic positive/negative/neutral labels. Each category must include a clear definition explaining the emotional state and behavioral indicators, three authentic example phrases that real customers would actually write in that emotional state, and an urgency weight on a 1-5 scale that reflects churn risk and response priority. Categories should address states like confused but patient, frustrated and seeking help, angry and threatening to leave, disappointed but loyal, satisfied and grateful, panicked or urgent, and passive-aggressive or sarcastic.

**Phase 2 - Signal Detection Library:** Create a comprehensive keyword and phrase library for each sentiment category that goes far beyond single-word matching. Include multi-word indicators that capture context, punctuation patterns that signal emotional intensity (all caps, excessive exclamation marks, ellipses, lack of punctuation), commonly misspelled emotional words because upset customers type quickly and carelessly, and contextual phrases that indicate escalation risk or loyalty erosion. Organize the library so it works both as a manual reference guide for agents and as the foundation for simple automation rules.

**Phase 3 - Scoring and Classification Rubric:** Build a practical scoring system that combines multiple keyword signals to assign each incoming message both a sentiment label and a confidence score. Define clear thresholds and decision rules: what confidence level triggers automatic tagging versus flagging for human review, how multiple conflicting signals should be weighted, and how to handle edge cases where messages contain mixed emotional signals. The rubric must be simple enough for agents to apply manually but structured enough to translate into basic automation.

**Phase 4 - Response Action Protocol:** For each sentiment category, define the complete response strategy including recommended tone and language approach, maximum response time target before the situation escalates, routing rules for whether the ticket needs specialized agent skills, and proactive gestures agents should consider offering (discounts for angry-and-churning customers, reassurance for panicked customers, educational resources for confused customers). Protocols must provide clear guidance while preserving agent flexibility to respond authentically to emotional situations rather than following rigid scripts.

#INFORMATION ABOUT ME:
- My business description: [DESCRIBE YOUR BUSINESS AND WHAT YOU SELL]
- My customer communication channels: [LIST CHANNELS: email, live chat, social media, phone transcripts, etc.]
- My current support team size and structure: [DESCRIBE TEAM SIZE AND ANY SPECIALIZATION]
- My typical customer pain points: [DESCRIBE COMMON ISSUES CUSTOMERS CONTACT YOU ABOUT]
- My biggest customer service challenges: [DESCRIBE WHAT'S NOT WORKING IN YOUR CURRENT APPROACH]

MOST IMPORTANT!: Structure your output as four clearly labeled sections corresponding to each phase, with detailed examples embedded throughout each section. Use bullet points within each phase for clarity, include specific example phrases in quotation marks, and present the scoring rubric in a simple table format if helpful for understanding thresholds and decision rules.
```
