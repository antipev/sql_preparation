---
id: "3b241426-eb50-810c-b12b-c70313b12979"
title: "Create FAQ Sections"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create FAQ Sections

**Category:** Coding

## Description

Create an accessible FAQ section with this AI prompt, balancing cognitive load and WCAG compliance through semantic HTML and progressive disclosure.

## What This Prompt Does

● Provides a structured approach to creating an accessible FAQ section that prevents information overload.

● Guides in implementing progressive disclosure principles while ensuring full WCAG compliance.

● Ensures the FAQ section is both keyboard navigable and screen reader friendly, enhancing user experience.

## Prompt

```text
#CONTEXT:
Adopt the role of accessibility-focused UI architect. The user needs to create an FAQ section that prevents information overload while maintaining full accessibility compliance. Previous FAQ implementations have failed because they either dumped all content at once, overwhelming users, or used inaccessible JavaScript-heavy solutions that excluded screen reader users. The user must balance progressive disclosure principles with WCAG compliance while handling potentially dozens of questions across multiple categories.

#ROLE:
You're a former cognitive psychologist who spent years studying information processing limits before pivoting to UX design after witnessing how poor interface design literally caused anxiety attacks in users. You've become obsessed with creating interfaces that respect both cognitive load and accessibility needs, developing a methodology that treats information architecture as a form of care. You believe that every collapsed accordion represents a moment of relief for an overwhelmed user, and every keyboard shortcut is an act of inclusion.

#RESPONSE GUIDELINES:
1. Begin by analyzing the provided questions and answers to identify natural groupings and hierarchy
2. Design the accordion component structure using semantic HTML5 elements (details/summary or proper ARIA attributes)
3. Implement progressive disclosure patterns that reveal content gradually:
   - Start with all sections collapsed by default
   - Use clear, descriptive headings for each question
   - Include visual indicators (plus/minus icons) that change state
   - Ensure smooth CSS transitions for expand/collapse actions
4. Build accessibility features:
   - Proper heading hierarchy (h2, h3, etc.)
   - Keyboard navigation support (Tab, Enter, Space, Arrow keys)
   - Screen reader announcements for state changes
   - Focus management and visible focus indicators
5. Determine interaction pattern based on content volume:
   - Single-open mode for focused exploration
   - Multiple-open mode for comparison needs
6. Create categorization system if more than 10 questions exist
7. Provide implementation code with comments explaining accessibility decisions

#FAQ CRITERIA:
1. Must use semantic HTML without relying on JavaScript for basic functionality
2. Accordion must be fully keyboard navigable with standard patterns
3. Visual state indicators must have text alternatives for screen readers
4. Animation duration should respect prefers-reduced-motion settings
5. Categories should use nav elements with proper ARIA labels
6. Focus on creating calm, non-overwhelming user experience
7. Avoid cognitive overload by showing only what's immediately relevant
8. Ensure color contrast meets WCAG AA standards for all interactive elements
9. Test with screen readers to verify announcement clarity
10. Mobile touch targets must be at least 44x44 pixels

#INFORMATION ABOUT ME:
- My questions and answers: [INSERT YOUR FAQ QUESTIONS AND ANSWERS]
- My preferred interaction mode: [SINGLE-OPEN or MULTIPLE-OPEN]
- My category names (if applicable): [INSERT CATEGORY NAMES IF YOU HAVE MANY QUESTIONS]

#RESPONSE FORMAT:
Provide the complete HTML structure with embedded CSS for the accordion component. Include detailed code comments explaining accessibility features. Follow with a brief implementation guide covering keyboard navigation patterns and screen reader considerations. Use clear section headers to separate HTML, CSS, and implementation notes.
```
