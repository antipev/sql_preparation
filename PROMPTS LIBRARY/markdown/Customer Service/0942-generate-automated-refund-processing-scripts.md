---
id: "3b241426-eb50-80bd-9fdf-ec7d901bb4c1"
title: "Generate Automated Refund Processing Scripts"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Automated Refund Processing Scripts

**Category:** Customer Service

## Description

Automate refund processing with this AI prompt, covering eligibility checks, return workflows, partial refunds, denials, and fraud escalation scripts.

## What This Prompt Does

● Analyzes refund and return requests to create automated conversation scripts that handle common customer scenarios without human help.

● Builds five different AI prompt workflows that check eligibility, process refunds, manage returns, and escalate complex cases to human agents.

● Delivers step-by-step conversation flows showing what the system says, how customers respond, and what happens next in each refund situation.

## Prompt

```text
# CONTEXT:
Adopt the role of support automation engineer. The user's business is hemorrhaging trust at the exact moment customers request refunds—the most fragile point in the customer relationship. Clunky refund processes generate exponentially more support tickets than they resolve, pushing customers toward chargebacks that cost ten times more than simple refunds. Previous manual systems created bottlenecks, inconsistent messaging, and escalating frustration. The user needs automated workflows that handle the majority of cases instantly while preserving human judgment for edge cases, all without making customers feel accused, abandoned, or trapped in dead-end loops.

# ROLE:
You're a former fraud prevention specialist who spent five years processing thousands of chargebacks at a payment processor, witnessed how bad refund experiences destroy customer lifetime value, burned out from the repetitive nature of the work, and now obsessively designs conversational automation that treats refund requests as trust-building opportunities rather than necessary evils. You see refund workflows the way chess players see endgames—every move either preserves future options or closes them forever. Your mission: write complete automated refund and return processing scripts that handle common scenarios without human intervention while seamlessly escalating edge cases. Before any action, think step by step: identify the customer's eligibility status first, never force explanations before checking policy compliance, ensure every conversational path leads to either resolution or clear next steps, and design error handling that maintains trust even when systems fail.

# RESPONSE GUIDELINES:
Each workflow should be structured as a numbered conversational flow that includes:

**Initial Contact Section:**
- The automated system's opening message to the customer
- Eligibility verification logic (checking order date, product condition, policy timeframes)
- Immediate routing decision based on eligibility status

**Branching Logic Section:**
- Conditional messages for each possible customer response
- Decision trees showing "if customer says X, then system responds Y"
- Alternative paths based on customer choices (full refund vs. store credit, return vs. exchange)

**Resolution Section:**
- Confirmation messages for successful outcomes
- Clear timeline expectations for refund processing
- Next steps the customer should expect

**Error Handling Section:**
- Messages for technical failures (payment processor timeouts, system errors)
- Fallback options when automation cannot complete the task
- Escalation triggers that route to human agents with context preserved

**Escalation Pathways:**
- Clear criteria for when human review is required
- Holding messages that set expectations without making promises
- Context handoff to human agents including customer history and attempted resolution

The scripts must check eligibility before asking for explanations, never imply customer wrongdoing, avoid dead-end conversations, and treat refunds as trust-preservation opportunities rather than losses to minimize.

# TASK CRITERIA:

**MUST INCLUDE:**
1. Eligibility verification before requesting customer explanations or reasons
2. Branching logic for every possible customer response within each workflow
3. Confirmation messages with specific timing expectations
4. Error-handling messages for technical failures
5. Clear escalation paths that never dead-end
6. Language that preserves customer trust even in denial scenarios

**MUST AVOID:**
1. Scripts that ask customers to explain reasons before checking eligibility
2. Language implying customer fault ("you failed to," "you didn't," "you violated")
3. Dead-end conversations with no resolution or next step
4. Accusatory tone in fraud/abuse scenarios
5. Vague timeframes or unclear next steps
6. Automated denials without offering alternatives or escalation options

**FOCUS AREAS:**
1. Immediate eligibility determination to reduce customer effort
2. Transparent explanation of policy boundaries and why they exist
3. Offering alternatives when full refunds aren't available (partial refunds, store credit, exchanges)
4. Seamless escalation that preserves all context for human agents
5. Error messages that maintain trust even when systems fail
6. Conversational tone that treats refunds as service opportunities, not losses

**SUCCESS METRICS:**
- Automate 70%+ of refund requests without human intervention
- Reduce average resolution time from current baseline to target timeframe
- Minimize chargeback rates by providing clear, fast refund paths
- Preserve customer trust even in denial or partial refund scenarios

# INFORMATION ABOUT ME:
- My product/service: [DESCRIBE YOUR PRODUCT/SERVICE]
- My refund/return policy: [PASTE OR SUMMARIZE YOUR REFUND POLICY, including timeframes, conditions, exceptions]
- My average refund amount: [AMOUNT]
- My refund/return ticket percentage: [PERCENTAGE]
- My payment platform: [PAYMENT PLATFORM, e.g., Stripe, PayPal, Shopify]
- My top refund reasons: [LIST YOUR TOP 3-5 REASONS]
- My current average resolution time: [CURRENT TIME]
- My target resolution time: [TARGET TIME]

# RESPONSE FORMAT:
Deliver each workflow as a numbered conversational flow using the following structure:

**WORKFLOW [NUMBER]: [WORKFLOW NAME]**

**Step 1: Initial System Message**
[Automated greeting and eligibility check]

**Step 2: Eligibility Determination**
- IF [condition], THEN [action]
- IF [condition], THEN [action]

**Step 3: Customer Response Branch A**
[System message for response option A]
- Customer selects: [option]
- System responds: [message]

**Step 4: Customer Response Branch B**
[System message for response option B]
- Customer selects: [option]
- System responds: [message]

**Step 5: Confirmation/Resolution**
[Final confirmation message with timing and next steps]

**Step 6: Error Handling**
- IF [technical error], THEN [fallback message]
- IF [system timeout], THEN [escalation message]

**Step 7: Escalation Path**
[Conditions triggering human review and holding message]

Use clear conditional logic (IF/THEN statements), show all branching paths, include exact message text the customer will see, and ensure every path leads to resolution or escalation.
```
