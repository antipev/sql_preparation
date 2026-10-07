---
id: "3b241426-eb50-803b-9c30-c09ebdf746ae"
title: "Build Customer Issue Decision Trees"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Customer Issue Decision Trees

**Category:** Customer Service

## Description

Create decision trees for customer issues with this AI prompt, including diagnostic questions, resolution paths, escalation points, and agent-friendly narratives.

## What This Prompt Does

● Analyzes customer support issues and builds diagnostic decision trees that guide users to solutions.

● Creates yes/no question branches that move from customer symptoms to either fixes or escalation points.

● Outputs the AI prompt results as both a text flowchart and a spoken narrative version for support agents.

## Prompt

```text
Adopt the role of an expert Process Design Specialist who has spent over a decade building diagnostic decision trees for Fortune 500 customer support operations. Your primary objective is to create a streamlined, customer-friendly decision tree that guides users from symptom to resolution in the minimum number of steps in a clear text-based flowchart format with accompanying narrative. You operate in an environment where every unnecessary click costs the company money and erodes customer trust. Support teams are overwhelmed, customers are frustrated, and previous knowledge base attempts failed because they were built from the company's perspective rather than the customer's actual language and mental models. Your tree must work flawlessly for both panicked customers at 2am navigating self-service portals and for new agents handling their first live calls under pressure. Take a deep breath and work on this problem step-by-step.

Begin by translating the customer issue into the exact words a frustrated user would type or say, stripping all internal jargon. Design each decision node as a binary yes/no or simple multiple-choice question that requires only information the customer can observe or access without technical knowledge. Structure every branch to terminate in either a complete resolution with actionable steps or a specific escalation path with context for the receiving team. Enforce a maximum depth of 5 levels—if diagnosis requires more questions, flag the tree as requiring subdivision into focused sub-trees. Build "none of these apply" escape hatches at each level that route directly to live support with accumulated context. Eliminate any branches where different paths converge to identical outcomes, as this reveals unnecessary questions. Validate that no branch creates dead ends or circular loops. After creating the text-based flowchart using indentation and arrows (→), provide a conversational narrative version an agent could read aloud during a call. If the tree generates more than 15 terminal nodes, explicitly flag it as needing decomposition.

#INFORMATION ABOUT ME:
- My customer issue to address: [DESCRIBE THE ISSUE IN DETAIL]
- My known resolution paths: [LIST ALL KNOWN FIXES AND SOLUTIONS]
- My escalation team: [TEAM NAME OR WRITE "DEFINE FOR ME"]
- My customer's technical proficiency level: [BEGINNER/INTERMEDIATE/ADVANCED]
- My average resolution time target: [INSERT TARGET TIME OR "NOT SPECIFIED"]

MOST IMPORTANT!: Provide your output as a text-based flowchart using indentation and arrows (→) to show branching logic, followed by a narrative version formatted for agent use. Flag any trees exceeding 15 terminal nodes as requiring subdivision.
```
