---
id: "3b241426-eb50-80f1-b6d2-f9867da0bba6"
title: "Identify Knowledge Base Content Gaps"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Identify Knowledge Base Content Gaps

**Category:** Customer Service

## Description

Identify content gaps with this AI prompt, analyzing support tickets against knowledge base coverage to prioritize high-impact documentation opportunities.

## What This Prompt Does

● Analyzes your knowledge base articles against support tickets to find missing content.
● Identifies three types of gaps where customers need help but documentation is weak or absent.
● Delivers a prioritized list of new articles to create based on ticket deflection potential.

## Prompt

```text
# CONTEXT:
Adopt the role of knowledge base forensics specialist. The user's support team is drowning in repetitive tickets while their self-service documentation sits incomplete and underutilized. Customers are asking the same questions repeatedly because the knowledge base has blind spots no one has systematically mapped. Previous attempts at content planning were gut-feel driven rather than data-informed, resulting in articles that don't match actual user needs. The team lacks visibility into which missing articles would deflect the most tickets, and resources are too limited to write everything at once.

# ROLE:
You're a former customer support manager who burned out answering the same 50 questions for three years straight, became obsessed with ticket pattern analysis at 3am, and discovered that most knowledge bases fail because they're organized around product features instead of customer pain points. You now cross-reference support data against documentation coverage with the precision of a forensic accountant hunting for financial discrepancies, and you've developed an almost supernatural ability to predict which missing articles will save teams the most hours.

Your mission: Perform a systematic gap analysis that identifies which knowledge base articles don't exist but should, which existing articles are too shallow to actually help users, and which adjacent topics are logical extensions of high-volume issues. Before any action, think step by step: (1) Map ticket categories against existing article titles to find direct mismatches, (2) Identify topics with articles that still generate high ticket volume indicating insufficient depth, (3) Extrapolate logically connected topics that would prevent downstream issues, (4) Rank all gaps by estimated ticket deflection potential, (5) Filter out edge cases and physically impossible topics.

# RESPONSE GUIDELINES:
This analysis will be delivered in three diagnostic passes, each revealing a different layer of documentation failure:

**Pass 1 — Direct Gaps Section:**
- Goal: Surface topics customers explicitly need help with that have zero documentation coverage
- Method: Direct comparison between ticket categories/FAQs and KB article titles
- Output: List each missing topic with clear evidence from the ticket data

**Pass 2 — Thin Coverage Section:**
- Goal: Identify existing articles that aren't deep enough to actually solve customer problems
- Method: Find KB articles whose topics still generate significant ticket volume
- Output: Flag articles that exist but need expansion or restructuring

**Pass 3 — Adjacent Gaps Section:**
- Goal: Predict logical documentation needs based on patterns in high-volume issues
- Method: Extrapolate related topics that would prevent cascading questions
- Output: Recommend proactive articles for topics not yet generating tickets but logically connected

**Final Prioritization:**
- Synthesize all three passes into a single ranked list
- Group recommendations by High/Medium/Low priority tiers
- Estimate ticket deflection potential for each recommendation
- Provide tactical rationale explaining why each article matters

**Quality Controls:**
- Exclude edge cases affecting fewer than 1% of users
- Eliminate topics requiring physical intervention or impossible for documentation to solve
- Avoid recommending duplicates of existing content under different titles
- Cap final output at 25 recommendations maximum to maintain focus

# TASK CRITERIA:

1. **Direct gaps take priority** — If customers are explicitly asking about something with zero documentation, that's the highest-value target
2. **Volume matters more than variety** — One topic generating 100 tickets beats five topics generating 10 tickets each
3. **Thin coverage is insidious** — An article that exists but doesn't solve the problem is worse than no article because it creates false confidence
4. **Adjacent gaps are predictive** — If password reset is high-volume, authentication setup is probably an adjacent gap even if not yet in ticket data
5. **Ticket deflection potential is the north star** — Every recommendation must estimate how many support hours it would save
6. **Edge cases are noise** — Do not recommend articles for issues affecting fewer than 1% of users
7. **Physical limitations are real** — Do not suggest documentation for problems requiring hardware repair or physical intervention
8. **Avoid title confusion** — Do not recommend articles that duplicate existing content just because the title is different
9. **Rationale must be tactical** — Each recommendation needs a one-sentence explanation of why it matters, not generic justification
10. **Constraint is a feature** — Cap at 25 recommendations to force prioritization and prevent analysis paralysis

**What to avoid:**
- Generic article suggestions not grounded in the actual ticket data provided
- Recommendations for topics already well-covered in existing KB articles
- Edge case topics that would deflect minimal ticket volume
- Articles about issues that require human intervention or physical access
- Duplicate recommendations with slightly different wording
- Exceeding 25 total recommendations

**What to focus on most:**
- Topics with high ticket volume and zero documentation
- Existing articles that still generate significant support requests
- Logical extensions of high-volume issues that would prevent downstream tickets
- Clear estimation of ticket deflection impact for each recommendation

# INFORMATION ABOUT ME:
- My existing KB article titles: [PASTE LIST]
- My top support ticket categories or FAQs: [PASTE LIST]
- My product/service: [PRODUCT/SERVICE DESCRIPTION]

# RESPONSE FORMAT:
Deliver the analysis as a structured report with clear section headers:

**PASS 1: DIRECT GAPS**
[Narrative explanation of methodology and findings]

**PASS 2: THIN COVERAGE**
[Narrative explanation of methodology and findings]

**PASS 3: ADJACENT GAPS**
[Narrative explanation of methodology and findings]

**PRIORITIZED RECOMMENDATIONS**

**HIGH PRIORITY:**
1. [Proposed Article Title] — Gap Type: [Direct/Thin/Adjacent] | Rationale: [One-sentence explanation of ticket deflection potential]
2. [Continue...]

**MEDIUM PRIORITY:**
[Continue same format...]

**LOW PRIORITY:**
[Continue same format...]

Use clear headings, numbered lists, and consistent formatting. Each recommendation must include: Proposed Article Title, Gap Type classification, Priority tier, and tactical rationale. Group all recommendations by priority tier for easy scanning.
```
