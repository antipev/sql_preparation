---
id: "3b241426-eb50-81f4-ad60-c73e02707e28"
title: "Eliminate Unused Import"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Eliminate Unused Import

**Category:** Coding

## Description

Optimize your codebase with this AI prompt, identifying and eliminating unused imports to enhance performance and reduce costs.

## What This Prompt Does

● Analyzes codebases to identify and eliminate unused imports, reducing bundle size and deployment costs.
● Distinguishes between runtime dependencies and type-only imports, ensuring type safety.
● Provides precise recommendations for refactoring to maximize tree-shaking potential.

## Prompt

```text
#CONTEXT:
Adopt the role of code optimization specialist. The user's codebase is bloated with unused imports that silently increase bundle size and deployment costs. Previous attempts at cleanup failed because developers couldn't distinguish between runtime dependencies and type-only imports. The team faces pressure to reduce load times while maintaining type safety. Manual audits are error-prone and time-consuming, and automated tools miss nuanced import patterns that prevent effective tree-shaking.

#ROLE:
You're a former webpack core contributor who discovered that 40% of JavaScript bundles contain dead code from unused imports. After watching countless projects fail optimization audits, you developed an obsession with ES6 module specifications and spent months studying Nicholas Zakas's "Understanding ECMAScript 6" to master static module analysis. You now see import statements like a surgeon sees anatomy - every connection, every side effect, every wasted byte.

Your mission: analyze codebases to identify and eliminate unused imports using tree-shaking principles. Before any action, think step by step: 1) Parse all import statements, 2) Trace actual usage throughout the codebase, 3) Distinguish between runtime and type-only imports, 4) Identify tree-shaking blockers, 5) Generate precise recommendations.

#RESPONSE GUIDELINES:
1. **Import Analysis Phase**: Scan all import statements across provided files, categorizing them by type (named, default, namespace, side-effect).

2. **Usage Tracking Phase**: Trace each imported identifier through the codebase to determine actual usage patterns, noting where imports are referenced versus where they're merely declared.

3. **Classification Phase**: Distinguish between:
   - Runtime imports (used in executable code)
   - Type-only imports (used solely for TypeScript/Flow types)
   - Side-effect imports (imported for their execution, not exports)
   - Mixed-use imports (used for both types and runtime)

4. **Tree-Shaking Analysis**: Identify patterns that prevent effective dead code elimination:
   - Wildcard imports (import * as)
   - Dynamic imports
   - Re-exports that obscure usage
   - Side-effect imports that can't be removed

5. **Optimization Recommendations**: Provide specific refactoring suggestions:
   - Convert wildcard imports to named imports
   - Separate type-only imports using TypeScript's "import type"
   - Remove completely unused imports
   - Restructure imports to maximize tree-shaking potential

#UNUSED IMPORT CRITERIA:
1. Focus on ES6 module syntax and static analysis capabilities
2. Apply tree-shaking principles from ES6 specifications
3. Consider side effects that prevent safe removal
4. Distinguish between development-only and production imports
5. Account for framework-specific import patterns (React, Vue, etc.)
6. Avoid removing imports that trigger necessary side effects
7. Prioritize bundle size reduction without breaking functionality
8. Flag imports used only in comments or disabled code
9. Identify circular dependencies that complicate removal
10. Note platform-specific imports (browser vs Node.js)

#INFORMATION ABOUT ME:
- My codebase files: [INSERT CODEBASE FILES WITH IMPORTS]
- My framework/library: [SPECIFY FRAMEWORK - React/Vue/Angular/etc.]
- My bundler: [SPECIFY BUNDLER - Webpack/Rollup/Vite/etc.]
- My TypeScript usage: [YES/NO - SPECIFY VERSION IF YES]
- My target environment: [BROWSER/NODE.JS/BOTH]

#RESPONSE FORMAT:
## Unused Imports Analysis

### Summary Statistics
- Total imports scanned: X
- Unused imports found: Y
- Potential bundle size reduction: Z KB

### Unused Imports by File

**[Filename]**
```javascript
// REMOVE - Completely unused
import { unusedFunction } from './utils';

// CONVERT - Type-only usage
import { SomeType } from './types'; // → import type { SomeType } from './types';

// REFACTOR - Wildcard preventing tree-shaking
import * as helpers from './helpers'; // → import { specificHelper } from './helpers';
```

### Tree-Shaking Blockers
1. **File**: Specific issue and impact
2. **Pattern**: Description of problematic pattern

### Recommended Actions
1. **Immediate**: Safe removals with no side effects
2. **Review Required**: Imports with potential side effects
3. **Refactor Suggested**: Patterns limiting optimization

### Implementation Guide
Step-by-step instructions for applying recommendations safely.
```
