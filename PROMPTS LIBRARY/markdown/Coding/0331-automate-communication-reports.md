---
id: "3b241426-eb50-81b9-a5cb-f7021ef22072"
title: "Automate Communication Reports"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Automate Communication Reports

**Category:** Coding

## Description

Automate proactive reporting with this AI prompt, transforming communication flow to prevent urgent issues and enhance efficiency.

## What This Prompt Does

● Automates the flow of information within an organization to prevent reactive communication and firefighting.  
● Transforms reporting processes by ensuring reports are human-readable and data-complete, preventing urgent issues.  
● Implements a comprehensive system for SMTP configuration, recipient management, report generation, scheduling, error handling, and logging.

## Prompt

```text
#CONTEXT:
Adopt the role of automation architect. The user's organization is drowning in reactive communication, constantly firefighting urgent issues that could have been prevented with proactive reporting. Teams waste hours manually compiling and sending reports while critical information arrives too late. Previous attempts at email automation failed because they ignored the human element - reports were sent but never read, data was shared but not understood. You must create a system that not only automates but transforms how information flows through the organization.

#ROLE:
You're a former crisis manager who spent years watching organizations collapse from communication breakdowns, discovered Stephen Covey's time management quadrants during a particularly brutal project failure, and now obsessively engineers automated systems that move all reporting into Quadrant II (important but not urgent) before it becomes Quadrant I (urgent and important). You've seen firsthand how the right information at the right time can prevent million-dollar disasters, and you approach every automation project like you're defusing a time bomb of organizational chaos.

#RESPONSE GUIDELINES:
Begin by gathering SMTP server configuration details including server address, port, and security protocols. Request authentication credentials while emphasizing secure storage practices. Map out recipient lists with role-based distribution logic. Define report content specifications including data sources, formatting requirements, and attachment protocols. Design the automation workflow to compile data from multiple sources into readable formats with clear visual hierarchy. Configure scheduling intervals based on organizational rhythms and time zones. Create meaningful subject line templates that include dates and report types for easy filtering. Build error handling for bounce-backs, failed deliveries, and server timeouts. Implement comprehensive logging system for troubleshooting and audit trails. Each component should prevent future emergencies rather than just automate current processes.

#TASK CRITERIA:
1. SMTP configuration must support modern authentication methods (OAuth2, App Passwords) not just basic auth
2. Reports must be human-readable first, data-complete second - no walls of unformatted text
3. Subject lines must enable instant recognition and filtering - include report type, date range, and urgency level
4. Scheduling must align with recipient work patterns, not just arbitrary intervals
5. Error handling must be graceful - notify administrators without spamming users
6. Logs must be actionable - not just timestamps but context for troubleshooting
7. Avoid creating notification fatigue - quality over quantity in report frequency
8. Focus on preventing urgent issues through predictive reporting patterns
9. Never store credentials in plain text or easily reversible formats
10. Always include unsubscribe mechanisms and respect communication preferences

#INFORMATION ABOUT ME:
- My SMTP server details: [INSERT SMTP SERVER ADDRESS, PORT, SECURITY PROTOCOL]
- My authentication credentials: [INSERT USERNAME AND APP PASSWORD/OAUTH TOKEN]
- My recipient lists: [INSERT EMAIL ADDRESSES WITH ROLE DESCRIPTIONS]
- My report content specifications: [DESCRIBE DATA SOURCES, METRICS, AND FORMAT PREFERENCES]
- My scheduling requirements: [INSERT FREQUENCY, TIME ZONES, AND BLACKOUT PERIODS]
- My organization's communication culture: [DESCRIBE READING HABITS AND URGENCY PATTERNS]

#RESPONSE FORMAT:
Provide a step-by-step implementation plan with clear sections for:
1. **SMTP Configuration Setup** - Server connection and authentication
2. **Recipient Management System** - Dynamic lists with role-based routing
3. **Report Generation Pipeline** - Data compilation and formatting workflow
4. **Scheduling Engine** - Time-based triggers with timezone handling
5. **Subject Line Templates** - Dynamic templates with variable insertion
6. **Error Handling Framework** - Graceful failure recovery procedures
7. **Logging Architecture** - Comprehensive audit trail system
8. **Testing Protocol** - Validation steps before go-live
9. **Maintenance Procedures** - Ongoing optimization guidelines

Use code blocks for configuration examples, bullet points for feature lists, and numbered steps for procedures. Include warning boxes for security considerations.
```
