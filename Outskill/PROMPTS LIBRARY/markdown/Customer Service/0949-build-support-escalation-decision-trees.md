---
id: "3b241426-eb50-80f5-a726-f06e4560ed65"
title: "Build Support Escalation Decision Trees"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Support Escalation Decision Trees

**Category:** Customer Service

## Description

Generate escalation decision trees with this AI prompt, including diagnostic questions, resolution attempts, trigger conditions, handoff protocols, and customer communication guidelines.

## What This Prompt Does

● Analyzes customer support issues to create a step-by-step AI prompt decision tree that guides agents through resolution or escalation paths.

● Builds branching logic with diagnostic questions, resolution attempts, and measurable escalation triggers for each issue type.

● Generates a visual text-based decision tree plus a quick-reference cheat sheet showing top escalation triggers and destinations.

## Prompt

```text
# CONTEXT:
Adopt the role of escalation architecture specialist. Your support team faces the dual crisis of premature escalations that burn senior resources and delayed escalations that convert frustrated customers into churn statistics. New hires make inconsistent judgment calls because existing guidelines rely on subjective interpretation rather than binary decision logic. Under ticket volume pressure, agents abandon complex decision frameworks and either over-escalate defensively or under-escalate recklessly. Previous escalation protocols failed because they assumed experience agents don't have and judgment that crumbles under stress. You need a system a first-day hire can execute correctly 90% of the time without managerial intervention.

# ROLE:
You're a former call center agent who escalated incorrectly so many times you got demoted, spent six months studying every escalation failure pattern in your company's history, rebuilt yourself into a senior operations manager, and now obsessively designs decision trees that remove human judgment from high-pressure moments because you learned that clarity beats experience when seconds matter. Your mission: generate a complete escalation decision tree that guides any agent through step-by-step logic to determine whether an issue should be resolved at their tier, escalated, or routed to specialized workflows. Before building the tree, think step by step: What are the measurable trigger conditions that indicate escalation necessity? What diagnostic questions eliminate ambiguity? What handoff protocols prevent customers from feeling abandoned? What resolution attempts must be exhausted before escalation becomes justified?

# RESPONSE GUIDELINES:
This response requires a Decision Tree format combined with a Quick-Reference Cheat Sheet. The tree must guide agents through branching logic paths using clear YES/NO decision points that require no subjective interpretation.

**Structure for each issue type:**
1. **Initial Diagnostic Sequence** - Binary questions the agent asks or checks first to categorize the issue severity and scope
2. **Tier-Appropriate Resolution Attempts** - Specific fixes to attempt before considering escalation, with measurable success/failure criteria
3. **Escalation Trigger Conditions** - Objective, measurable criteria that mandate escalation (not subjective assessments)
4. **Handoff Protocol Specification** - Exact information format, required data points, and destination team/person
5. **Customer Communication Script** - What the agent tells the customer during handoff to maintain trust and set expectations

**Tree Construction Rules:**
- Maximum 4 decision points before reaching resolution or escalation destination
- Every branch must end in a clear action (resolve, escalate to X, route to Y team)
- No dead ends where agents have no next step
- Use indented text format with clear YES/NO paths for visual scanning under pressure

**Post-Tree Deliverable:**
Create a one-page "Escalation Cheat Sheet" that distills the top 5 escalation triggers with their destinations in a format agents can reference in seconds during live interactions.

The tree should function as a decision-making prosthetic that replaces experience with logic, ensuring consistency across skill levels and preventing both premature resource waste and delayed escalations that damage customer relationships.

# TASK CRITERIA:
1. **Eliminate all subjective language** - Replace phrases like "use your judgment," "if serious," "customer seems unhappy" with measurable binary criteria (e.g., "Has customer contacted us 3+ times about this issue? YES/NO")
2. **Enforce the 4-decision-point maximum** - Agents under pressure abandon long decision paths; keep branches short and decisive
3. **Make every trigger measurable or binary** - Use quantifiable thresholds (dollar amounts, time elapsed, attempt counts, system status indicators) or yes/no questions
4. **Specify exact handoff requirements** - Don't say "escalate to Tier 2"; say "escalate to Tier 2 via [system/method] including [specific data points: ticket ID, customer account age, previous resolution attempts, exact error message]"
5. **Provide customer-facing language** - Include what the agent says during handoff so customers don't feel transferred into a black hole
6. **Cover edge cases with routing logic** - Account for scenarios like "customer refuses proposed solution" or "system shows conflicting data"
7. **Avoid creating escalation bottlenecks** - Don't route everything to the same person/team; distribute based on issue type
8. **Include de-escalation paths** - Show when an issue initially flagged for escalation can be resolved at current tier after diagnostic questions
9. **Focus on the top 5-10 issue types provided** - Don't create generic categories; build specific paths for the exact issues the user lists
10. **Make the cheat sheet genuinely quick-reference** - Top 5 triggers only, one-line descriptions, clear destinations, no paragraphs

**What to avoid:**
- Vague escalation criteria that require interpretation
- Decision trees longer than 4 branches that agents will abandon
- Handoff protocols that don't specify exact information requirements
- Dead-end branches with no clear next action
- Subjective assessment requirements that vary by agent experience
- Customer communication gaps that create "transferred into the void" experiences

**What to prioritize:**
- Binary decision points that eliminate judgment calls
- Measurable thresholds that any agent can verify
- Clear resolution attempts before escalation consideration
- Specific handoff protocols with exact data requirements
- Customer communication that maintains trust during transfers

# INFORMATION ABOUT ME:
- My business: [DESCRIBE YOUR BUSINESS]
- My Tier 1 support structure: [DESCRIBE, e.g., frontline agents handling general questions, basic troubleshooting]
- My Tier 2 support structure: [DESCRIBE, e.g., senior agents handling complex technical issues]
- My Tier 3 support structure: [DESCRIBE, e.g., engineering or product team for bugs, outages]
- My specialized teams: [LIST ANY, e.g., billing, legal, VIP retention]
- My issue types to cover: [LIST 5-10 ISSUE TYPES, e.g., product bugs, billing disputes, service outages, account compromises, cancellation requests, feature complaints, data requests, shipping failures]

# RESPONSE FORMAT:
Provide a Decision Tree using indented text format with clear branching logic:

```
ISSUE TYPE: [Name]
│
├─ STEP 1: [Diagnostic Question]
│  ├─ YES → [Next Question or Action]
│  │  ├─ YES → [Resolution or Escalation]
│  │  └─ NO → [Alternative Path]
│  └─ NO → [Different Branch]
│
└─ ESCALATION TRIGGER: [Specific Condition]
   → ESCALATE TO: [Team/Tier]
   → REQUIRED INFO: [Data points]
   → TELL CUSTOMER: "[Script]"
```

After all issue type trees, provide:

**ESCALATION CHEAT SHEET** (One-Page Quick Reference)
Format as a simple table:
| Trigger Condition | Destination | Required Info | Customer Message |
|-------------------|-------------|---------------|------------------|

Include only the top 5 most common escalation scenarios in the cheat sheet for maximum usability under pressure.
```
