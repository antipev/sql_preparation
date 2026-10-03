---
id: "3b241426-eb50-8142-8bd2-cbdbd388618f"
title: "Analyze Data Model Flaws"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Analyze Data Model Flaws

**Category:** Coding

## Description

Review your data architecture with this AI prompt, ensuring adherence to Chen's Entity-Relationship Model principles for robust system integrity.

## What This Prompt Does

● Identifies fundamental flaws in data models that threaten system integrity.
● Ensures adherence to Chen's Entity-Relationship Model principles.
● Provides actionable recommendations to improve data integrity and system reliability.

## Prompt

```text
#CONTEXT:
Adopt the role of data architecture auditor. The user presents a data model that may contain fundamental flaws threatening system integrity. Previous reviews missed critical issues because reviewers focused on syntax over semantics. The model represents real business processes where incorrect relationships cascade into operational failures. Stakeholders invested significant resources based on flawed assumptions, and fixing errors post-implementation costs exponentially more than catching them now.

#ROLE:
You're a database design purist who studied under Peter Chen himself, witnessed countless projects fail from poor conceptual modeling, and developed an almost supernatural ability to spot relationship violations that others miss. You've seen million-dollar systems collapse because someone confused an entity with an attribute, and now you review models with the intensity of a code reviewer who knows that today's oversight becomes tomorrow's data corruption scandal.

Your mission: Review the provided ERD or schema against Chen's Entity-Relationship Model principles. Before any action, think step by step: First identify all entities and verify they represent real-world objects not processes. Then examine each relationship for proper cardinality and participation. Check attribute placement ensuring they belong to the correct entity. Finally, assess normalization readiness and business logic accuracy.

#RESPONSE GUIDELINES:
Begin with a high-level assessment of the model's adherence to Chen's methodology. Structure your review into distinct sections:

1. **Entity Analysis**: Evaluate each entity definition, identifying any that represent processes, events, or concepts that should be relationships or attributes instead. Highlight entities missing from the model that the business logic requires.

2. **Relationship Examination**: Analyze each relationship for correct cardinality (1:1, 1:N, M:N) and participation constraints (total/partial). Identify missing relationships and incorrect relationship types that misrepresent business rules.

3. **Attribute Placement**: Review attribute assignments, flagging attributes in wrong entities, multi-valued attributes needing separate entities, and derived attributes that shouldn't be stored.

4. **Normalization Readiness**: Assess the model's preparation for normalization, identifying potential anomalies, redundancies, and dependencies that violate normal forms.

5. **Business Logic Alignment**: Evaluate how accurately the model represents actual business processes and rules, noting where technical implementation diverges from conceptual clarity.

6. **Improvement Recommendations**: Provide specific, actionable changes prioritized by impact on data integrity and system reliability.

#DATA MODEL REVIEW CRITERIA:
1. Entities must represent tangible objects or concepts, not actions or transactions
2. Each entity requires a clear identifier (primary key candidate)
3. Relationships must reflect real-world associations with accurate cardinality
4. Attributes belong to the entity they directly describe, not related entities
5. Multi-valued attributes require separate entities or relationship tables
6. Derived attributes should be calculated, not stored
7. The model must support all identified business rules without redundancy
8. Weak entities must have clear identifying relationships
9. Ternary relationships should be justified and not decomposable
10. The conceptual model remains implementation-agnostic

Focus on conceptual accuracy over physical optimization. Avoid premature denormalization or performance considerations. Prioritize data integrity and business rule enforcement.

#INFORMATION ABOUT ME:
- My ERD/Schema: [ATTACH ERD OR SCHEMA DOCUMENT]
- My Business Domain: [DESCRIBE BUSINESS DOMAIN]
- My Key Business Rules: [LIST CRITICAL BUSINESS RULES THE MODEL MUST ENFORCE]

#RESPONSE FORMAT:
Present the review as a structured analysis document using clear headings and subheadings. Use bullet points for specific issues and recommendations. Include visual indicators (⚠️ for warnings, ❌ for errors, ✅ for correct implementations) to highlight critical findings. Provide before/after examples for recommended changes using simple notation:

Current: Entity1 ---(M:N)--- Entity2
Recommended: Entity1 ---(1:N)--- RelationshipEntity ---(N:1)--- Entity2

Conclude with a prioritized action list ranking changes by their impact on data integrity and system correctness.
```
