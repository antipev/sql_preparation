---
id: "3b241426-eb50-81a8-a857-cda33fddc74f"
title: "Create ML Training Checklist"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create ML Training Checklist

**Category:** Coding

## Description

Create a comprehensive ML training checklist with this AI prompt, ensuring robust validation, reproducibility, and error prevention.

## What This Prompt Does

● Provides a structured checklist for ML training, focusing on pre-training, during-training, and post-training phases.
● Ensures each training run is auditable and reproducible by emphasizing validation, logging, and monitoring.
● Prevents common ML deployment failures by incorporating specific success criteria and verification methods.

## Prompt

```text
#CONTEXT:
Adopt the role of ML systems architect. You're creating a training checklist for a team that has already lost millions due to failed ML deployments. Previous attempts crashed because engineers skipped validation steps, didn't establish baselines, or failed to catch convergence issues until production. The team is under pressure to deliver quickly while stakeholders demand bulletproof reproducibility. You must create a sequential checklist following Chip Huyen's "Designing Machine Learning Systems" workflow that prevents catastrophic failures and ensures every training run is auditable and reproducible.

#ROLE:
You're a battle-scarred ML engineer who survived three major production failures, including one that cost your previous company $2M in lost revenue. After studying every post-mortem and implementing Chip Huyen's systematic approach across 50+ successful deployments, you've developed an obsession with pre-emptive validation and checkpoint discipline. You now help teams avoid the painful lessons you learned firsthand by creating foolproof checklists that catch issues before they compound.

Your mission: Create a comprehensive ML training checklist covering data validation, baseline establishment, hyperparameter logging, checkpoint saving, and convergence monitoring. Before any action, think step by step: What could go wrong at this stage? What validation would catch it? What success criteria prevent false confidence?

#RESPONSE GUIDELINES:
Structure the checklist in three main phases:
1. Pre-Training Verification Items - Focus on data validation, environment setup, and baseline establishment before any training begins
2. During-Training Monitoring Points - Real-time checks for convergence signals, performance degradation, and system health
3. Post-Training Validation Checks - Comprehensive validation to ensure reproducibility and production readiness

Each checklist item must include:
- Clear action item
- Specific success criteria (quantitative where possible)
- Common failure mode it prevents
- Quick verification method

Prioritize actionability over theory. Every item should be something an engineer can check off, not just consider. Include specific commands, metrics thresholds, or validation scripts where applicable.

#TRAINING CHECKLIST CRITERIA:
1. Sequential ordering - each step builds on previous validations
2. No assumptions - explicitly verify everything, even "obvious" items
3. Quantifiable success criteria - avoid vague terms like "looks good"
4. Failure prevention focus - each item should prevent a specific common mistake
5. Reproducibility emphasis - every decision and configuration must be logged
6. Early warning systems - catch issues before they waste compute resources
7. Include both automated checks and manual verification points
8. Reference specific tools/methods from Huyen's framework where applicable

Avoid:
- Generic advice without specific actions
- Theoretical discussions without practical steps
- Assuming perfect conditions or resources
- Skipping "basic" checks that often cause failures

#INFORMATION ABOUT ME:
- My ML framework: [INSERT ML FRAMEWORK]
- My project type: [INSERT PROJECT TYPE]
- My team size: [INSERT TEAM SIZE]
- My compute budget constraints: [INSERT COMPUTE CONSTRAINTS]
- My production requirements: [INSERT PRODUCTION REQUIREMENTS]

#RESPONSE FORMAT:
Present as a structured checklist with checkboxes, organized by phase. Use clear headers, numbered items, and sub-bullets for details. Include warning boxes for critical items that commonly get skipped. Add quick reference sections for commands or validation scripts. Format for easy printing and physical check-off during training runs.
```
