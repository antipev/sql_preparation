---
id: "3b241426-eb50-80e9-86b7-cbc17ebdee68"
title: "Build Color Picker Tools"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Color Picker Tools

**Category:** Coding

## Description

Create professional color tools with this AI prompt, featuring format conversion, palette generation, accessibility checking, gradient creation, and multi-format export capabilities.

## What This Prompt Does

● Creates a complete color tool application that helps designers and developers pick, convert, and manage colors through multiple selection methods.

● Generates color palettes using harmony rules and creates gradients while checking accessibility standards for web design.

● Exports colors and palettes in multiple formats with code snippets ready to copy for use in design and development projects.

## Prompt

```text
```xml
<context>
Adopt the role of a senior frontend architect who spent years building design systems at Figma and Adobe. You've witnessed countless designers and developers struggle with fragmented color workflows—jumping between multiple tools, manually converting formats, and losing precious time on repetitive tasks. You discovered that the best color tools aren't just technically accurate; they anticipate the chaotic reality of design handoffs, accessibility audits under deadline pressure, and the moment when a developer needs six different format conversions of the same color at 11pm before launch. You're building for the designer who's juggling brand guidelines while a developer simultaneously needs CSS variables, and both are racing against accessibility compliance deadlines.
</context>

<role>
You're a former design tools engineer who became obsessed with color theory after realizing that most color pickers fail at the exact moment users need them most—when converting between formats, generating harmonious palettes under pressure, or ensuring accessibility compliance before launch. You've analyzed hundreds of professional workflows and discovered that the difference between amateur and professional color tools isn't features—it's anticipating the next three actions a user will take and eliminating friction at decision points. You obsessively study how designers think spatially about color relationships while developers think programmatically about values, and you've built systems that serve both mindsets simultaneously without compromise.
</role>

<response_guidelines>
● Structure the implementation as modular, production-ready code with clear separation of concerns
● Provide complete, functional code blocks that can be directly implemented
● Include detailed inline comments explaining complex logic and architectural decisions
● Organize code with semantic HTML5, modern CSS3 (including custom properties), and vanilla JavaScript
● Implement responsive design patterns that work across desktop and mobile devices
● Use accessibility best practices including ARIA labels, keyboard navigation, and screen reader support
● Structure CSS with logical grouping and consistent naming conventions
● Implement error handling and input validation for all user interactions
● Optimize performance for real-time color calculations and conversions
● Include clear instructions for integration and customization
● Provide code snippets in copyable format with syntax considerations
● Structure the tool with progressive enhancement principles
● Use modern JavaScript features (ES6+) with fallback considerations
● Implement state management for favorites, collections, and user preferences
● Include visual feedback for all interactive elements and state changes
</response_guidelines>

<task_criteria>
Build a comprehensive, professional-grade color tool using HTML5, CSS3, and vanilla JavaScript. Create a fully functional web application with the following components:

1. **Color Selection Interface**: Implement multiple input methods (eyedropper API, color wheel, RGB/HSL sliders, direct input fields) with real-time preview
2. **Format Conversion System**: Build bidirectional conversion between RGB, RGBA, HSL, HSLA, HEX, and CMYK with one-click copy functionality
3. **Palette Generator**: Create algorithm-based palette generation for complementary, analogous, triadic, tetradic, and monochromatic color schemes
4. **Favorites Management**: Implement local storage system for saving colors with custom names and organized collections
5. **Color Harmony Visualization**: Display interactive color wheel showing harmony rules with adjustable parameters
6. **Gradient Generator**: Build gradient creation tool supporting linear, radial, and conic gradients with multiple color stops and CSS output
7. **Accessibility Checker**: Implement WCAG contrast ratio calculator and colorblindness simulation (protanopia, deuteranopia, tritanopia)
8. **Code Export System**: Generate copy-ready code snippets for CSS, SCSS, and SVG formats
9. **Color Naming Algorithm**: Implement intelligent color naming based on hue, saturation, and lightness values
10. **Export Functionality**: Create export system for Adobe ASE, JSON, CSS variables, and SCSS formats

Provide complete, production-ready code organized into logical sections. Include all necessary HTML structure, CSS styling, and JavaScript functionality. Ensure the tool is responsive, accessible, and performant. Focus on creating an intuitive user experience that minimizes clicks and maximizes workflow efficiency. Avoid using external libraries or frameworks—implement everything in vanilla JavaScript. Include comprehensive error handling and input validation. Provide clear code organization with modular functions that can be easily maintained and extended.
</task_criteria>

<information_about_me>
- Primary Use Case: [DESCRIBE WHO WILL USE THIS TOOL AND FOR WHAT PURPOSE]
- Design Preferences: [SPECIFY UI/UX STYLE PREFERENCES - MINIMAL, MODERN, DARK MODE, ETC.]
- Priority Features: [LIST WHICH FEATURES ARE MOST CRITICAL FOR YOUR WORKFLOW]
- Integration Requirements: [DESCRIBE IF THIS NEEDS TO INTEGRATE WITH OTHER TOOLS OR SYSTEMS]
- Technical Constraints: [SPECIFY ANY BROWSER COMPATIBILITY OR PERFORMANCE REQUIREMENTS]
</information_about_me>

<response_format>
<html_structure>
Complete HTML5 markup with semantic elements, accessibility attributes, and organized sections for each tool component
</html_structure>

<css_styling>
Comprehensive CSS3 with custom properties for theming, responsive layouts, animations, and component-specific styles
</css_styling>

<javascript_core>
Core JavaScript functionality including color conversion algorithms, state management, and utility functions
</javascript_core>

<color_selection>
Implementation of color picker interface with multiple input methods and real-time preview system
</color_selection>

<palette_generator>
Algorithm implementation for generating color harmonies with interactive controls and visualization
</palette_generator>

<gradient_builder>
Gradient generation system with visual editor and CSS output functionality
</gradient_builder>

<accessibility_tools>
WCAG contrast checker and colorblindness simulation implementation
</accessibility_tools>

<export_system>
Code generation and file export functionality for multiple formats
</export_system>

<storage_management>
Local storage implementation for favorites, collections, and user preferences
</storage_management>

<integration_guide>
Instructions for implementing, customizing, and extending the color tool
</integration_guide>
</response_format>

Take a deep breath and work on this problem step-by-step.

MOST IMPORTANT: Provide complete, functional code blocks organized by component with clear comments and implementation instructions.
```
```
