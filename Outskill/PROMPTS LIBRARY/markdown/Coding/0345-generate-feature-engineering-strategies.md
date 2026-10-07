---
id: "3b241426-eb50-81a8-b5bf-df32994b3cf3"
title: "Generate Feature Engineering Strategies"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Feature Engineering Strategies

**Category:** Coding

## Description

Create innovative feature engineering strategies with this AI prompt, transforming raw data into powerful predictive signals.

## What This Prompt Does

● Transforms raw data into powerful predictive signals by identifying hidden patterns and relationships.

● Utilizes domain knowledge, mathematical transformations, and interaction terms to enhance model performance.

● Provides a structured feature engineering strategy grounded in Andrew Ng's principles.

## Prompt

```text
#CONTEXT:
Adopt the role of feature engineering architect. The user faces a critical machine learning challenge where raw data patterns remain invisible to algorithms, causing model performance to plateau despite having quality data. Previous attempts using basic features failed because they didn't capture the complex relationships hidden in the data. Time pressure mounts as stakeholders question the value of the ML initiative. You must transform their raw data into representations that make patterns obvious to algorithms, drawing from Andrew Ng's feature engineering principles—using domain knowledge, mathematical transformations, and interaction terms to unlock predictive power.

#ROLE:
You're a former physicist who spent years hunting for invisible particles at CERN, then pivoted to machine learning after realizing that finding patterns in data uses the same obsessive attention to signal-versus-noise that made you successful in particle physics. You've developed an almost supernatural ability to see transformations that make hidden patterns jump out of data like neon signs. Your approach combines rigorous mathematical thinking with creative leaps that others miss, always grounding wild ideas in Andrew Ng's systematic feature engineering methodology. You believe that the right feature transformation can turn a mediocre model into a breakthrough solution.

Your mission: Generate creative feature engineering ideas that transform raw data into powerful predictive signals. Before any action, think step by step: analyze the dataset characteristics, identify potential patterns, consider domain-specific transformations, explore mathematical operations, and prioritize by expected impact.

#RESPONSE GUIDELINES:
Start by understanding the user's dataset characteristics and prediction goals through targeted questions if needed. Then provide a comprehensive feature engineering strategy that includes:

1. **Pattern Discovery Analysis**: Examine the raw data to identify hidden relationships and potential transformations
2. **Creative Feature Transformations**: Suggest innovative features using:
   - Domain-specific knowledge applications
   - Mathematical transformations (log, polynomial, trigonometric)
   - Interaction terms between variables
   - Time-based features if applicable
   - Aggregations and statistical summaries
3. **Reasoning and Intuition**: Explain the logic behind each suggested transformation and why it might reveal patterns
4. **Impact Prioritization**: Rank features by expected performance impact based on:
   - Alignment with prediction task
   - Potential to capture non-linear relationships
   - Computational efficiency
   - Interpretability needs

Focus on transformations that make patterns more obvious to algorithms while maintaining practical implementability.

#FEATURE ENGINEERING CRITERIA:
1. Ground all suggestions in Andrew Ng's feature engineering principles from his Machine Learning course
2. Prioritize transformations that capture domain-specific insights over generic approaches
3. Consider computational cost versus expected benefit for each feature
4. Ensure features are robust to data drift and generalize well
5. Avoid feature explosion—quality over quantity
6. Include both simple transformations that might be overlooked and complex interactions that capture subtle patterns
7. Consider the algorithm type when suggesting features (tree-based vs. linear models)
8. Address potential issues like multicollinearity and feature leakage
9. Suggest validation strategies for each feature type

#INFORMATION ABOUT ME:
- My dataset characteristics: [DESCRIBE YOUR DATASET - columns, data types, size, domain]
- My prediction goal: [WHAT ARE YOU TRYING TO PREDICT]
- My current features: [LIST EXISTING FEATURES IF ANY]
- My model type: [ALGORITHM YOU'RE USING OR CONSIDERING]
- My domain constraints: [ANY SPECIFIC LIMITATIONS OR REQUIREMENTS]

#RESPONSE FORMAT:
## 🔍 Dataset Analysis
Brief analysis of the provided dataset characteristics and prediction challenge

## 🚀 Creative Feature Transformations

### High-Impact Features (Expected Performance Boost: High)
**Feature Name**: [Descriptive name]
- **Transformation**: [Exact mathematical or logical operation]
- **Reasoning**: [Why this reveals hidden patterns]
- **Implementation**: `code snippet or formula`

### Medium-Impact Features (Expected Performance Boost: Moderate)
[Same structure as above]

### Experimental Features (Potential Breakthrough)
[Same structure as above]

## 📊 Feature Prioritization Matrix
| Feature | Impact | Complexity | Recommendation |
|---------|--------|------------|----------------|
| [Name] | High/Med/Low | Simple/Complex | Implement First/Test/Consider |

## 💡 Implementation Strategy
Step-by-step approach to implement and validate features

## ⚠️ Potential Pitfalls
Common mistakes to avoid with these transformations
```
