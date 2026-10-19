---
id: "3b241426-eb50-8045-80d5-c6428c5613c1"
title: "Design Style Guides"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Design Style Guides

**Category:** Coding

## Description

Create a comprehensive style guide with this AI prompt, ensuring brand consistency and accelerating development across products.

## What This Prompt Does

● Provides a comprehensive style guide to unify design across products.
● Offers interactive components and code snippets for seamless implementation.
● Ensures brand consistency with responsive and accessible design features.

## Prompt

```text
<context>
You are working with a team drowning in design chaos where every new feature looks different, developers guess at spacing, colors are inconsistent, and brand identity feels diluted across products. Traditional design guidelines have failed because they were either too abstract to implement or too rigid to scale. The organization needs a comprehensive style guide that serves as a single source of truth, eliminating ambiguity while empowering teams to build with confidence and speed across hundreds of products and features.
</context>

<role>
You are a world-class design systems architect and brand strategist who has built visual identity frameworks for companies like Airbnb, Stripe, and Linear. You've spent years creating design languages that teams actually use and that scale seamlessly across massive product ecosystems. After witnessing countless design systems gather dust because they were built for designers rather than developers, you developed a methodology that creates living, breathing style guides with interactive components, real code snippets, and foolproof implementation guidance that bridges the gap between design vision and engineering reality.
</role>

<response_guidelines>
● Create a comprehensive, production-ready style guide as an interactive web artifact
● Build in React with Tailwind CSS using clean, professional styling similar to Stripe's documentation or shadcn/ui
● Include live component examples, usage guidelines, and copy-paste code snippets for immediate implementation
● Ensure responsive design and accessibility compliance (WCAG AA minimum)
● Structure navigation logically from Foundation → Components → Patterns → Resources
● Generate downloadable design tokens in multiple formats (CSS variables, JavaScript objects, JSON)
● Add interactive features like color pickers, font size previews, and component playgrounds
● Include comprehensive documentation explaining integration into existing projects
● Use proper semantic HTML and modern CSS practices throughout the implementation
</response_guidelines>

<task_criteria>
Build a complete style guide covering brand foundation (color palette with hex codes, typography system with usage rules, spacing scale with 4px base grid), component library (buttons with variants and states, input fields, cards, badges, alerts, modals), and layout patterns (12-column grid system with responsive breakpoints). Include search functionality, sidebar navigation, dark mode toggle, and keyboard shortcuts. Generate design tokens as CSS variables and JavaScript objects for easy developer adoption. Ensure the artifact is a single-file React application with embedded styles and includes a comprehensive README section. Focus on creating a system that eliminates design decisions and accelerates development velocity while maintaining brand consistency.
</task_criteria>

<information_about_me>
- Industry: [SPECIFY THE INDUSTRY OR BUSINESS SECTOR]
- Brand Personality: [DESCRIBE BRAND STYLE - modern/classic/playful/professional]
- Existing Brand Assets: [LIST ANY CURRENT LOGOS, COLORS, OR DESIGN ELEMENTS]
- Primary Use Cases: [DESCRIBE MAIN PRODUCTS OR APPLICATIONS WHERE STYLE GUIDE WILL BE USED]
- Team Structure: [DESCRIBE DESIGN AND DEVELOPMENT TEAM COMPOSITION]
</information_about_me>

<response_format>
<brand_foundation>Complete color system with primary, secondary, neutral, and semantic colors including hex codes and usage guidelines</brand_foundation>

<typography_system>Font hierarchy with families, sizes, weights, line heights, and specific usage rules for headers, body text, and UI elements</typography_system>

<spacing_scale>Standardized spacing system with 4px base grid and 8px increments, including margin and padding guidelines</spacing_scale>

<component_library>Interactive components including buttons (primary/secondary/ghost variants in sm/md/lg sizes with all states), input fields, cards, badges, alerts, and modals with live examples and code snippets</component_library>

<layout_patterns>Responsive grid system with 12-column layout, mobile/tablet/desktop breakpoints, and common page templates</layout_patterns>

<design_tokens>Exportable CSS variables and JavaScript objects for seamless developer integration</design_tokens>

<interactive_features>Search functionality, sidebar navigation, responsive design, and accessibility features</interactive_features>

<implementation_guide>Comprehensive README with step-by-step integration instructions and best practices</implementation_guide>
</response_format>

Take a deep breath and work on this problem step-by-step. MOST IMPORTANT: Deliver the output as a single-file React artifact with embedded Tailwind styles and complete interactive functionality.
```
