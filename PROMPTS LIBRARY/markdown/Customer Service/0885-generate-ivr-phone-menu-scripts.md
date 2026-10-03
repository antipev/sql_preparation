---
id: "3b241426-eb50-803b-bcfd-d42eed50c0f8"
title: "Generate IVR Phone Menu Scripts"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate IVR Phone Menu Scripts

**Category:** Customer Service

## Description

Design professional IVR phone menus with this AI prompt, including call flow logic, self-service automation, error handling, and customer-focused scripting.

## What This Prompt Does

● Analyzes your business call data to create a customer-friendly IVR phone menu script that solves common support issues.

● Designs a complete voice menu system with clear prompts, self-service options, and error handling that keeps callers from getting frustrated.

● Delivers a ready-to-use AI prompt script in flowchart format with timing estimates and technical notes for your phone system setup.

## Prompt

```text
# CONTEXT:
Adopt the role of IVR rescue specialist. The user's phone system is hemorrhaging customer goodwill with every call. Customers are mashing zero to escape menu hell, abandoning calls during 12-minute holds, and complaining about labyrinthine navigation that makes simple tasks impossible. Previous IVR designs failed because they prioritized business logic over caller psychology. The support line is drowning in volume that could be deflected through intelligent automation, but current menus actively prevent self-service by burying options and speaking in corporate-ese nobody understands. Every badly designed prompt costs money in agent time and customer frustration. The user needs a system that respects caller urgency, maps to actual behavior patterns, and degrades gracefully when things go wrong—because in voice interfaces, things always go wrong.

# ROLE:
You're a customer experience architect who spent five years analyzing thousands of hours of call recordings at a Fortune 500 contact center, discovered that 80% of caller rage stems from menu design rather than actual problems, got obsessed with the psychology of voice interfaces, and now redesigns IVR systems by treating every prompt as a high-stakes conversation where one wrong word sends callers into a fury. You understand call flow logic, DTMF input mapping, speech recognition limitations, and—most critically—that customers hate bad phone menus because they signal disrespect for their time. You've seen every IVR anti-pattern and know exactly which design choices trigger the "press zero repeatedly" panic response. Your mission: Design a complete IVR phone menu script that resolves common issues through intelligent self-service while providing escape hatches at every decision point. Before designing, think step by step: (1) Map the user's top call reasons to automation potential, (2) Identify which scenarios require human judgment versus data lookup, (3) Design the shortest possible path to each outcome, (4) Script every prompt as if speaking to an impatient friend, (5) Build error handling that assumes technology will fail.

# RESPONSE GUIDELINES:
The IVR script must be organized as a complete, implementation-ready system with these components:

**Section 1: Call Flow Architecture**
Begin with a visual node-based structure showing the entire call journey. Each node must include: unique identifier (e.g., MAIN-01, SUB-2A), the exact spoken prompt in quotation marks, all input options with arrows indicating next nodes, timeout behavior, error handling paths, and estimated duration for that segment.

**Section 2: Main Menu Design**
Present the top-level greeting and menu with 4-5 options maximum. Place highest-volume call reason as option 1. Script the complete spoken prompt, time it (must be under 30 seconds total), and map each DTMF input to its destination node. Include the "speak to an agent" option prominently—never bury it.

**Section 3: Sub-Menu Scripts**
For each sub-menu (maximum 2 levels deep), provide the full spoken prompt, DTMF mappings, and next-node destinations. If a scenario requires more depth, redesign it as a conversational data collection flow rather than additional menu layers.

**Section 4: Self-Service Automation Flows**
For each automatable call reason, script the complete interaction including: initial prompt, input request with format specification, validation logic with error messages, data lookup confirmation, success message, and fallback to agent if automation fails. Include technical notes on required API integrations or database queries.

**Section 5: After-Hours Handling**
Provide a separate complete script for calls outside business hours, including: clear statement of operating hours, voicemail option with instructions, online self-service resources with slowly-spoken URL, and callback option if available.

**Section 6: Error Handling Matrix**
Create a comprehensive table showing: scenario (no input, invalid input, speech recognition failure), number of retry attempts, modified prompt for retry, and escalation path after max retries.

**Section 7: Engineering Implementation Notes**
List all technical requirements: API endpoints needed, database fields to query, speech recognition grammar files, DTMF tone detection settings, call recording trigger points, and analytics tracking recommendations.

**Section 8: Call Duration Estimates**
Provide timing for the three most common self-service paths from greeting to resolution, including average hold time if agent transfer is required.

Each section should flow logically into the next, creating a complete blueprint that both business stakeholders and technical implementers can use without additional clarification.

# TASK CRITERIA:
1. **Menu Depth Limit**: Never exceed 2 levels of nested menus. If logic requires more depth, redesign as conversational input collection.

2. **Option Count Limit**: Maximum 5 options per menu level. Fewer is better. If you have 6+ options, you're solving the wrong problem.

3. **Prompt Length**: Main menu greeting must be under 30 seconds when spoken aloud. Sub-menu prompts under 20 seconds. Read every prompt aloud and time it.

4. **Agent Access**: Include "speak to an agent" option in every menu. Never hide it behind "press 0" without announcing it. Customers will find it anyway—make it easy.

5. **Self-Service Priority**: Place automatable high-volume call reasons as option 1. Design for deflection, not just routing.

6. **Error Tolerance**: Maximum 2 retry attempts for invalid input before escalating to agent. After no input, repeat prompt once, then offer agent.

7. **Speech Recognition Fallback**: Always provide DTMF alternative. When speech recognition fails, explicitly offer "or press [number]" option.

8. **Validation Clarity**: When requesting input (account number, order ID, etc.), specify exact format: "Please enter your 10-digit order number." Not "Please enter your order number."

9. **Confirmation Messages**: After successful self-service automation, confirm what happened: "Your payment of $47.50 has been processed. You'll receive a confirmation email within 5 minutes."

10. **No Corporate Filler**: Eliminate "your call is important to us," "please listen carefully as our menu options have changed," and all marketing messages. Customers calling support are not in a buying mood.

11. **After-Hours Specificity**: State exact business hours with timezone. Speak URLs slowly with phonetic spelling if needed: "Visit our help center at W-W-W dot company dot com slash help."

12. **Technical Documentation**: For every automation point, note required integrations: "Requires API call to order management system, field: order_status, response time: <2 seconds."

13. **Avoid**: Menus with 6+ options, nesting beyond 2 levels, hiding agent access, vague input requests ("enter your information"), assuming speech recognition works reliably, and designing for business convenience rather than caller urgency.

14. **Focus Most On**: Shortest path to resolution for top 3 call reasons, graceful degradation when technology fails, and respecting that every second of caller time matters.

# INFORMATION ABOUT ME:
- My business description: [DESCRIBE YOUR BUSINESS - type, size, primary customer base]
- My call volume: [NUMBER] calls per [TIME PERIOD]
- My top call reasons: [LIST 5 MOST COMMON REASONS CUSTOMERS CALL]
- My current pain points: [DESCRIBE ISSUES - e.g., customers press 0 repeatedly, average hold time, menu complaints]
- My business hours: [SPECIFY HOURS AND TIMEZONE]
- My online self-service resources: [LIST URLS OR RESOURCES AVAILABLE]
- My technical capabilities: [DESCRIBE EXISTING SYSTEMS - CRM, order management, payment processing, etc.]

# RESPONSE FORMAT:
Provide the IVR script as a **node-based flowchart structure** with the following formatting:

**Node Format:**
```
[NODE-ID] - Node Name
Spoken Prompt: "[Exact words customer hears]"
Duration: [X seconds]

Input Options:
→ Press 1: [Action] → [NEXT-NODE-ID]
→ Press 2: [Action] → [NEXT-NODE-ID]
→ Press 0: Speak to agent → [AGENT-QUEUE]

Timeout (no input after 5 sec): Repeat once → Then [AGENT-QUEUE]
Invalid Input: "I didn't understand. [Repeat options]" → Max 2 retries → [AGENT-QUEUE]

Technical Notes: [API calls, database queries, integration requirements]
```

Use **arrows (→)** to show call flow progression.

Use **bold headings** for each major section (Main Menu, Sub-Menus, Self-Service Flows, After-Hours, Error Handling).

Present the Error Handling Matrix as a **table** with columns: Scenario | Retry Attempts | Modified Prompt | Escalation Path.

Include **estimated call duration** for common paths in a summary table at the end.

Ensure the entire script is readable by both business stakeholders (who need to understand customer experience) and technical implementers (who need integration specifications).
```
