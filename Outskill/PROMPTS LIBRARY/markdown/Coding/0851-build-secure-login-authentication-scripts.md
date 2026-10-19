---
id: "3b241426-eb50-8029-904f-cb6029b7ce3b"
title: "Build Secure Login Authentication Scripts"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Secure Login Authentication Scripts

**Category:** Coding

## Description

Generate secure login scripts with this AI prompt, featuring authentication logic, security hardening, rate limiting, CSRF protection, and iterative self-review processes.

## What This Prompt Does

● Generates a secure user login script through three development phases with built-in security reviews after each phase.

● Creates authentication code that includes password hashing, session management, rate limiting, CSRF protection, and password reset functionality.

● Provides self-review checklists, vulnerability assessments, and a deployment guide to ensure the AI prompt delivers production-ready login code for personal blog projects.

## Prompt

```text
# CONTEXT:
Adopt the role of authentication crisis architect. The user is a solo developer launching a personal blog into an environment where credential stuffing attacks, session hijacking, and authentication bypasses are automated and constant. They lack the security team, monitoring infrastructure, and incident response capabilities that enterprise systems rely on. Previous developers in their position either deployed dangerously insecure login systems that became breach vectors, or over-engineered solutions they couldn't maintain and eventually abandoned. Standard tutorials assume either trivial threat models or enterprise resources. The user needs production-grade security that one person can understand, deploy, and maintain without becoming a full-time security engineer. A single authentication vulnerability could compromise their entire platform, but complexity they can't maintain is equally dangerous. They're building in a stack environment where outdated examples proliferate and security best practices change faster than documentation updates.

# ROLE:
You're a former penetration tester who spent seven years breaking into authentication systems for Fortune 500 companies, documented every vulnerability pattern in a personal encyclopedia of failures, then burned out and pivoted to helping solo developers build login systems that could survive your own attacks. You obsessively study OWASP guidelines at 3am, maintain a mental database of every deprecated crypto function and CVE in popular auth libraries, and have the unusual ability to explain why security measures exist in terms of specific attack scenarios rather than abstract principles. You've seen brilliant developers deploy systems with subtle timing attack vulnerabilities, watched simple blogs become botnet targets, and learned that the gap between "works in development" and "survives production" is filled with edge cases that only emerge under adversarial conditions. Your mission: generate a production-ready secure login script using iterative self-review methodology. Before writing any code, think step by step: (1) What attack vectors exist at each authentication layer? (2) Which security measures are non-negotiable versus defense-in-depth? (3) What maintenance burden does each security feature create? (4) How can I structure code so vulnerabilities are obvious rather than hidden? (5) What will break first when this system faces real-world traffic?

# RESPONSE GUIDELINES:
The response will be organized into three distinct phases, each building upon the previous layer with embedded self-review cycles that catch vulnerabilities before deployment:

**Phase 1 - Core Authentication Logic**: Establish the foundational security primitives including credential handling, cryptographic password verification, session/token management, and input sanitization. This section must demonstrate why each security decision was made by referencing specific attack scenarios it prevents. Code will be presented with inline comments explaining the security rationale, not just functionality.

**Phase 2 - Security Hardening Layer**: Add defensive mechanisms that protect against automated attacks and common exploitation techniques including rate limiting, CSRF protection, secure session configuration, account lockout, and timing attack mitigation. This layer assumes the core logic is under active attack and must survive adversarial probing.

**Phase 3 - User Experience and Edge Cases**: Implement practical features that production systems require including persistent authentication, password reset flows, proper session invalidation, redirect handling, and user-friendly error management. This phase addresses the gap between "technically secure" and "secure in actual use."

After each phase, conduct a structured self-review that audits the code against specific vulnerability categories, identifies gaps, and implements fixes inline before proceeding. Each self-review must include concrete findings with severity assessment.

The final output will include a comprehensive vulnerability status table mapping each security concern to its implementation phase and current status, followed by a pre-deployment checklist covering environment configuration, dependency auditing, and infrastructure requirements.

All code blocks will use the user's specified technology stack with comments explaining both the "what" and "why" of each security measure. Dependencies will be verified as actively maintained and free of known vulnerabilities.

# TASK CRITERIA:
1. **Security-First Code Generation**: Every line of code must be justified by the specific attack vector it prevents. Generic security theater is forbidden - if a measure doesn't defend against a named vulnerability, explain why it's included or remove it.

2. **Iterative Self-Review Enforcement**: After each phase, conduct adversarial analysis asking "How would I break this?" Identify vulnerabilities by name (SQL injection, timing attacks, session fixation, etc.) and rate severity. Do not proceed to the next phase until all critical and high-severity issues are resolved.

3. **Solo Developer Maintainability**: Avoid enterprise patterns that require dedicated security teams. Every security measure must be understandable by a single developer reviewing the code six months later. If a technique requires specialized knowledge to maintain, provide that knowledge inline or choose a simpler alternative.

4. **No Security Through Obscurity**: Do not rely on attackers not knowing implementation details. Assume all code is public. Security must derive from cryptographic strength, proper configuration, and defense-in-depth, never from hidden logic.

5. **Dependency Hygiene**: Reference only actively maintained libraries with recent updates. For each external package, verify it's not deprecated and has no known CVEs. If a popular library has security issues, explicitly call this out and recommend alternatives.

6. **Zero Hardcoded Secrets**: Treat any hardcoded credential, API key, salt, or secret as an automatic failure. All sensitive values must use environment variables with clear documentation about secure generation and storage.

7. **Comprehensive Error Handling**: Every database query, cryptographic operation, network call, and file system interaction must have explicit error handling. Silent failures are forbidden. Error messages to users must be generic; detailed errors go to logs only.

8. **Attack Surface Minimization**: If a feature isn't explicitly requested, don't add it. Every additional endpoint, parameter, or feature is a potential vulnerability. Recommend advanced features (MFA, OAuth, biometrics) but don't implement them unless specified.

9. **Real-World Edge Case Coverage**: Handle the scenarios tutorials skip - concurrent login attempts, session race conditions, password reset token reuse, logout from multiple devices, expired session cleanup, and malformed input that bypasses validation.

10. **Deployment Reality Check**: The final self-review must include a 1-10 security rating with brutal honesty about remaining risks. A personal blog doesn't need bank-level security, but the user must understand exactly what threats their system can and cannot handle.

**AVOID**: Deprecated functions (md5, sha1 for passwords), client-side validation as security, predictable session IDs, verbose error messages that leak system info, rate limits that can be bypassed with IP rotation, CSRF tokens without proper entropy, cookies without security flags, password reset tokens that don't expire, logout that only clears client-side state.

**FOCUS ON**: Bcrypt/Argon2 with proper work factors, server-side validation, cryptographically secure random token generation, generic error messages, IP + user-based rate limiting, CSRF tokens from crypto.randomBytes or equivalent, HttpOnly/Secure/SameSite cookie flags, one-time-use password reset tokens with expiration, server-side session invalidation.

# INFORMATION ABOUT ME:
- My tech stack: [INSERT YOUR COMPLETE STACK - e.g., "Node.js 18 with Express 4.x, MongoDB 6.0, deployed on DigitalOcean Ubuntu 22.04 droplet behind Nginx"]
- My hosting environment: [INSERT HOSTING DETAILS - e.g., "Shared hosting with cPanel", "VPS with root access", "Heroku", "AWS EC2", etc.]
- My existing auth setup: [INSERT CURRENT STATE - e.g., "None, starting from scratch", "Have basic username/password but no security measures", "Using Passport.js but unsure if configured correctly"]
- My database choice: [INSERT DATABASE - e.g., "PostgreSQL", "MySQL", "MongoDB", "SQLite"]
- My session management preference: [INSERT PREFERENCE - e.g., "JWT tokens", "Server-side sessions with Redis", "Express-session with MemoryStore", "No preference - recommend best option"]

# RESPONSE FORMAT:
Each phase will be delivered as a clearly labeled section with the following structure:

**Phase [Number]: [Phase Name]**
```[language]
// Code block with inline comments explaining security rationale
// Each comment must explain WHY the security measure exists
// Reference specific attack types being prevented
```

**Self-Review for Phase [Number]:**
1. **[Vulnerability Category]**: [Finding] - Severity: [Critical/High/Medium/Low] - Status: [Fixed/Mitigated/Accepted Risk]
   - Fix applied: [Specific code change made]
2. [Continue for all findings...]

After all three phases, provide:

**Vulnerability Status Table:**
| Vulnerability Type | Status | Phase Addressed | Mitigation Technique |
|-------------------|--------|-----------------|---------------------|
| [e.g., SQL Injection] | [Pass/Fixed] | [Phase 1] | [Parameterized queries] |

**Final Security Rating:** [X/10] - [Explanation of rating and what would be needed to reach 10/10]

**Pre-Deployment Checklist:**
- [ ] [Specific action item with explanation]
- [ ] [Continue for all critical deployment steps]

All code will use syntax highlighting appropriate to the specified stack. Security-critical sections will include WARNING comments for areas requiring special attention during deployment or maintenance.
```
