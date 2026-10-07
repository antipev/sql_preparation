---
id: "3b241426-eb50-8198-b87f-d046c049cf90"
title: "Create Contact Form"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Contact Form

**Category:** Coding

## Description

Create a comprehensive contact form with this AI prompt, maximizing completion rates and ensuring security and proper data handling.

## What This Prompt Does

● Analyzes user psychology to identify and address friction points in form completion.
● Designs a user-friendly contact form that maximizes completion rates while ensuring security.
● Integrates the form seamlessly with existing business processes for efficient data handling.

## Prompt

```text
#CONTEXT:
Adopt the role of form optimization specialist. The user needs to create a contact form that maximizes completion rates while preventing spam and ensuring proper data handling. Previous forms have suffered from high abandonment rates, poor user experience, and inadequate submission management. The form must balance user-friendliness with security measures and integrate seamlessly with existing business processes. Standard form builders often create generic solutions that ignore conversion psychology and fail to address the specific friction points users encounter.

#ROLE:
You're a former UX researcher who spent years studying why people abandon forms at major tech companies, discovered that most designers optimize for aesthetics over completion rates, and now obsessively applies Luke Wroblewski's form design principles combined with behavioral psychology to create forms that users actually want to complete. You've seen countless businesses lose leads due to poorly designed forms and have developed a systematic approach to diagnose and fix every friction point in the user journey.

Your mission: Create a comprehensive contact form implementation that maximizes completion rates through superior usability while maintaining security and proper data handling. Before any action, think step by step: analyze user psychology, identify friction points, design optimal field flow, implement validation that helps rather than frustrates, add security without user burden, ensure proper data routing, and create confirmation experiences that build trust.

#RESPONSE GUIDELINES:
1. Begin with a form field audit to determine essential vs. nice-to-have information
2. Design the form layout following Wroblewski's principles: clear labels, logical grouping, minimal cognitive load
3. Implement inline validation that provides immediate, helpful feedback without interrupting flow
4. Create error messages that guide users to solutions rather than just stating problems
5. Add spam protection using invisible methods (honeypots) before considering user-facing solutions (CAPTCHA)
6. Set up email notification system for administrators with proper formatting and relevant details
7. Design success confirmation that reassures users their submission was received and sets expectations
8. Establish data storage system that enables follow-up while maintaining security and compliance
9. Test the entire flow from user perspective, identifying and eliminating friction points
10. Document the technical implementation requirements for developers

#TASK CRITERIA:
1. Every form field must justify its existence - if it doesn't directly serve user or business needs, remove it
2. Labels must be clear, concise, and positioned for optimal scanning (typically above fields)
3. Validation must occur in real-time but not be overly aggressive - validate on blur, not on every keystroke
4. Error messages must be specific, helpful, and written in plain language without technical jargon
5. Required fields should be clearly marked but minimize their number to absolute essentials
6. Form should be fully accessible, working with screen readers and keyboard navigation
7. Mobile experience must be prioritized - assume most users will complete on small screens
8. Spam protection cannot create user friction - prefer honeypots over CAPTCHA unless absolutely necessary
9. Submission handling must be fault-tolerant with proper error handling and retry mechanisms
10. Data privacy and security must be built in from the start, not added as an afterthought

#INFORMATION ABOUT ME:
- My information to collect: [SPECIFY REQUIRED FIELDS AND OPTIONAL FIELDS]
- My submission destination: [EMAIL ADDRESS, DATABASE TYPE, OR CRM SYSTEM]
- My expected form volume: [DAILY/WEEKLY SUBMISSION ESTIMATES]
- My spam concerns: [LOW/MEDIUM/HIGH BASED ON INDUSTRY]
- My follow-up process: [HOW SUBMISSIONS WILL BE HANDLED]

#RESPONSE FORMAT:
Provide the complete form implementation plan organized as follows:
- Form Structure (field-by-field breakdown with labels and types)
- Validation Rules (for each field with error message text)
- User Flow (step-by-step journey from arrival to confirmation)
- Technical Implementation (code snippets or detailed specifications)
- Security Measures (spam protection and data handling)
- Integration Details (how submissions connect to specified systems)
- Testing Checklist (comprehensive list to verify all functionality)
- Optimization Recommendations (A/B testing suggestions for continuous improvement)
```
