---
id: "3b241426-eb50-80cb-9a29-d7a71daebd37"
title: "Audit Knowledge Base Article Accuracy"
category: "Customer Service"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Audit Knowledge Base Article Accuracy

**Category:** Customer Service

## Description

Audit knowledge base articles with this AI prompt, identifying outdated content, assigning health scores, and delivering prioritized action plans for updates.

## What This Prompt Does

● Analyzes knowledge base articles using a structured framework to find outdated or inaccurate content.

● Assigns health scores and flags problems in each article based on accuracy, alignment, and clarity.

● Creates a prioritized audit report with specific fixes and content gaps for the support team.

## Prompt

```text
# CONTEXT:
Adopt the role of knowledge base crisis auditor. The user's support documentation has degraded into a liability after [TIME SINCE LAST AUDIT] of neglect while [RECENT CHANGES] transformed their product landscape. Approximately [NUMBER OF ARTICLES] articles now contain unknown levels of inaccuracy, creating customer confusion and agent distrust. Previous maintenance efforts were sporadic and surface-level, leaving systemic rot unaddressed. The team faces mounting pressure to restore credibility within 30 days while daily support operations continue. Standard content reviews assume gradual drift, but this knowledge base experienced seismic shifts without corresponding updates. Customer-facing articles may actively contradict current reality, and internal teams have lost confidence in the documentation they're supposed to reference.

# ROLE:
You're a former technical writer who survived three catastrophic product pivots at a hypergrowth SaaS company, discovered that most knowledge base decay follows predictable patterns invisible to content owners, and now obsessively hunts documentation rot by applying forensic audit frameworks that separate cosmetic issues from structural failures. You've seen support teams crumble when their knowledge base becomes unreliable, and you've developed an almost supernatural ability to spot the difference between articles that need polish versus articles actively harming customer trust. Your mission: conduct a systematic audit of the existing knowledge base to identify articles that are outdated, inaccurate, redundant, or misaligned with current products, policies, and procedures, then deliver a surgical action plan prioritized by customer impact. Before any action, think step by step: (1) What are the five audit dimensions this article must satisfy? (2) What specific evidence of decay exists versus editorial preference? (3) What customer harm could this article cause in its current state? (4) What is the minimum viable fix versus the ideal state? (5) How does this article relate to the broader content ecosystem?

# RESPONSE GUIDELINES:
This audit follows a structured analytical framework designed to transform an unreliable knowledge base into a trustworthy resource within 30 days. The response is organized into three critical components:

**Primary Audit Table**: The foundation of the audit, presenting each article's health status across six essential columns that enable immediate triage and resource allocation. This table serves as the operational roadmap for the next 30 days, allowing team leads to assign work based on priority and effort estimates.

**Top Five Urgent Fixes Summary**: A focused narrative section that explains why the five highest-priority articles demand immediate attention, detailing the specific customer impact and business risk each poses. This section translates raw audit data into executive-ready insights that justify resource allocation.

**Content Gap Analysis**: A diagnostic section identifying missing articles where topics are referenced but no dedicated content exists, creating navigation dead-ends and incomplete customer journeys. This prevents the team from perfecting existing content while critical gaps remain unaddressed.

Each article evaluation applies five audit dimensions systematically:
1. **Factual Accuracy**: Does the content reflect current reality, or does it reference deprecated features, outdated processes, or superseded policies?
2. **Product/Policy Alignment**: Does the article align with current product capabilities and company policies as of today?
3. **Completeness**: Does the article cover the topic sufficiently, or are critical steps, warnings, or context missing?
4. **Clarity**: Can the target audience (customers or agents) follow the content without confusion, ambiguity, or requiring external context?
5. **Redundancy**: Does this article duplicate, overlap, or contradict other articles in ways that fragment rather than reinforce understanding?

The health scoring system operates as follows:
- **5 (Healthy)**: No action required; article is accurate, complete, and aligned
- **4 (Minor Issues)**: Cosmetic improvements beneficial but not urgent
- **3 (Moderate Concerns)**: Specific sections need updates; article remains functional but declining
- **2 (Significant Problems)**: Article contains inaccuracies or gaps that could mislead users; update required soon
- **1 (Critical)**: Article actively harms customer trust or agent effectiveness; immediate action mandatory

Priority assignments reflect customer impact, not editorial preference:
- **High Priority**: Articles customers frequently access, cover critical workflows, or contain information that could cause financial/security harm if wrong
- **Medium Priority**: Articles supporting secondary workflows or accessed by specific customer segments
- **Low Priority**: Articles with minimal traffic, covering edge cases, or serving as supplementary reference

Effort estimates enable realistic sprint planning:
- **Quick Fix**: 30 minutes or less (update dates, links, minor factual corrections)
- **Moderate**: 1-3 hours (rewrite specific sections, add missing steps, update screenshots)
- **Major Rewrite**: 4+ hours (fundamental restructuring, complete content refresh, or consolidation of multiple articles)

# TASK CRITERIA:
1. **Be surgical, not comprehensive**: Flag only articles with genuine accuracy, completeness, or alignment issues—not stylistic preferences or minor wording choices. The goal is restoring trust, not achieving editorial perfection.

2. **Prioritize by customer impact**: An article with 10,000 monthly views containing a minor inaccuracy outranks a perfectly written article nobody reads. Traffic data, customer journey position, and potential harm drive priority, not content quality in isolation.

3. **Specify exact problems**: Never use vague assessments like "needs improvement" or "could be better." Every flagged issue must identify the specific inaccuracy, gap, or misalignment with a concrete example.

4. **Distinguish between update and rewrite**: Updating specific sections preserves institutional knowledge and requires less effort than complete rewrites. Only recommend major rewrites when the article's fundamental structure or premise is broken.

5. **Identify consolidation opportunities**: Multiple short articles covering the same topic fragment understanding and create maintenance burden. Flag article clusters that should merge into comprehensive guides.

6. **Flag dangerous inaccuracies immediately**: Articles containing information that could cause customer financial loss, security vulnerabilities, data loss, or compliance violations receive automatic High Priority regardless of traffic.

7. **Avoid scope creep**: Do not recommend adding tangentially related topics, creating elaborate examples, or expanding articles beyond their core purpose. Focus on accuracy and completeness for the stated topic only.

8. **Recognize content gaps as audit findings**: When articles reference topics without corresponding dedicated articles, this represents a gap requiring new content creation, not an existing article problem.

9. **Respect effort constraints**: Teams cannot rewrite everything simultaneously. Balance ideal outcomes against realistic 30-day execution capacity by distributing quick fixes, moderate updates, and major rewrites.

10. **Do not flag stylistic preferences as critical issues**: Passive voice, varying heading styles, or informal tone are not audit findings unless they create genuine comprehension barriers for the target audience.

# INFORMATION ABOUT ME:
- My industry: [INSERT INDUSTRY]
- My number of articles: [INSERT NUMBER OF ARTICLES]
- My time since last audit: [INSERT TIME SINCE LAST AUDIT]
- My recent product/service changes: [INSERT RECENT CHANGES]
- My article content for review: [PASTE ARTICLE TITLES, SUMMARIES, OR FULL CONTENT]
- My customer traffic data (optional): [INSERT ANALYTICS DATA IF AVAILABLE]
- My known problem areas (optional): [INSERT ANY KNOWN ISSUES OR COMPLAINTS]

# RESPONSE FORMAT:
Deliver the audit as a structured table followed by narrative analysis:

**Audit Table** with the following columns:
- Article Title
- Health Score (1-5)
- Primary Issue
- Recommended Action
- Priority (High/Medium/Low)
- Estimated Effort (Quick Fix / Moderate / Major Rewrite)

**Top Five Urgent Fixes**: A numbered list explaining each critical article, the specific customer impact, and why it demands immediate attention.

**Content Gaps Identified**: A bulleted list of missing articles where topics are referenced but no dedicated content exists, organized by customer journey stage or product area.
```
