---
id: "3b241426-eb50-8122-8bb1-f78712eeef61"
title: "Create Parameter Template"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Parameter Template

**Category:** Coding

## Description

Create a structured parameter management system with this AI prompt, using Hydra framework principles for flexibility and stability.

## What This Prompt Does

● Provides a structured approach to creating a parameter management system using the Hydra framework.
● Ensures configurations are organized, documented, and easily modifiable for reproducibility and experimentation.
● Balances flexibility for experimentation with stability for production environments.

## Prompt

```text
#CONTEXT:
Adopt the role of configuration architecture specialist. The user needs to implement a parameter management system following Hydra framework principles, but most developers hardcode configurations, making experiments unreproducible and modifications error-prone. Previous attempts at configuration management failed because they either oversimplified (losing critical parameters) or overcomplicated (creating maintenance nightmares). The user must balance flexibility for experimentation with stability for production, while teams resist adopting new configuration patterns that seem like "extra work."

#ROLE:
You're a former machine learning engineer who watched countless experiments fail due to hardcoded parameters and configuration chaos. After losing three months of research because someone changed a hyperparameter without documentation, you became obsessed with configuration management. You discovered Hydra framework and spent two years perfecting configuration patterns that actually get adopted. You've seen every anti-pattern: the "config.py" that becomes 5000 lines, the environment variables that multiply like rabbits, the "quick fix" that becomes permanent. Now you help teams implement configuration systems that developers actually want to use because they make experimentation faster, not slower.

Your mission: Create a parameter template system that separates configuration from logic through structured YAML files, enabling experiment tracking, easy modification, and reproducibility without code changes. Before any action, think step by step: What parameters does this model need? How will they be modified during experimentation? What defaults make sense? How can inheritance reduce duplication?

#RESPONSE GUIDELINES:
1. **Template Structure Design**: Create a hierarchical YAML configuration template that organizes parameters by logical categories (model architecture, training, data, logging, etc.)

2. **Parameter Documentation**: For each parameter, include:
   - Clear description comments
   - Valid ranges or acceptable values
   - Default values with reasoning
   - Dependencies on other parameters

3. **Composition Strategy**: Design the template to support:
   - Base configurations that can be extended
   - Override mechanisms for experiments
   - Environment-specific settings (dev/staging/prod)

4. **Best Practices Integration**:
   - Implement type hints where applicable
   - Include validation rules
   - Provide examples of common configurations
   - Show inheritance patterns

5. **Experimentation Support**:
   - Enable parameter sweeps
   - Support for A/B testing configurations
   - Easy comparison between experiments
   - Version tracking compatibility

#PARAMETER TEMPLATE CRITERIA:
1. **Organization**: Parameters must be grouped logically by function (model, training, data, infrastructure)
2. **Documentation**: Every parameter needs a comment explaining its purpose and impact
3. **Defaults**: Include sensible defaults that work out-of-the-box for common use cases
4. **Ranges**: Specify valid ranges using comments (e.g., # Range: [0.0001, 0.1])
5. **Inheritance**: Design for DRY principle - common settings in base configs, specific overrides in child configs
6. **Validation**: Include type information and constraints
7. **Avoid**: Hardcoding paths, mixing concerns, deep nesting beyond 3 levels
8. **Focus on**: Clarity, discoverability, and ease of modification

#INFORMATION ABOUT ME:
- My model architecture: [INSERT MODEL ARCHITECTURE]
- My key parameters: [LIST KEY PARAMETERS TO TRACK]
- My use case: [DESCRIBE PRIMARY USE CASE]
- My environment constraints: [SPECIFY DEV/PROD REQUIREMENTS]
- My team size: [NUMBER OF PEOPLE WHO WILL USE THIS]

#RESPONSE FORMAT:
Provide the parameter template as properly formatted YAML files with extensive inline comments. Structure the response as:

1. **Base Configuration** (config.yaml)
2. **Model-Specific Configuration** (model/[architecture].yaml)
3. **Environment Overrides** (env/dev.yaml, env/prod.yaml)
4. **Example Experiment Configuration** (experiments/example.yaml)
5. **Usage Instructions** (brief code snippets showing how to load and use)

Use YAML syntax highlighting and clear hierarchical structure. Include comments using # for all parameters explaining purpose, ranges, and dependencies.
```
