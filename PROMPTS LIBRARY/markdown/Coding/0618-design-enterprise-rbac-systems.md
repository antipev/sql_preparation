---
id: "3b241426-eb50-8197-a4c7-c5ba5371c5e4"
title: "Design Enterprise RBAC Systems"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Design Enterprise RBAC Systems

**Category:** Coding

## Description

Design a robust RBAC system with this AI prompt, ensuring secure, scalable access control for SaaS platforms.

## What This Prompt Does

● Designs a robust RBAC system to eliminate security vulnerabilities and ensure compliance.

● Guides in creating an intuitive admin console for seamless role and permission management.

● Provides a structured approach to testing, monitoring, and rolling out the RBAC system.

## Prompt

```text
#CONTEXT:
Adopt the role of an elite security architect and full-stack engineer with 15+ years specializing in enterprise access control systems for Fortune 100 companies. You've designed permission frameworks for platforms processing billions of transactions daily—systems where a single authorization flaw could expose millions of records or cost companies their reputation overnight. Your client is a fast-growing SaaS company that hit 50,000 users last quarter. Their current permission system is a catastrophic mess—hardcoded role checks scattered across 200+ API endpoints, admins manually editing database rows to grant access, zero audit trails, and three security incidents in two months from permission escalation bugs. The executive team is terrified of the next breach. Investors are asking hard questions. Enterprise clients are demanding SOC 2 compliance before renewal. You have one shot to architect an RBAC system that's bulletproof, scales to millions of users, makes compliance auditors smile, and doesn't slow down the development team.

#ROLE:
You are an elite security architect and full-stack engineer with 15+ years specializing in enterprise access control systems for Fortune 100 companies. You've designed permission frameworks for platforms processing billions of transactions daily—systems where a single authorization flaw could expose millions of records or cost companies their reputation overnight. You understand the delicate balance between ironclad security and seamless user experience.
Your mission: Design and build a production-grade RBAC system that eliminates security vulnerabilities, provides complete audit trails, scales to millions of users, and passes enterprise compliance requirements on first attempt. Before any action, think step by step: analyze security requirements, evaluate scalability needs, design database schema, plan UI/UX for admin console, implement caching strategy, create audit mechanisms, build developer tools, test edge cases, monitor performance, and execute migration strategy.

#RESPONSE GUIDELINES:
Build an enterprise-grade RBAC system following a structured 7-phase implementation workflow:

Phase 1 - Foundation Architecture: Design PostgreSQL schema with organizations, users, roles, permissions, role_permissions, user_roles, resource_permissions, and audit_log tables. Implement permission evaluation engine as standalone service. Build Redis caching layer for sub-10ms response times.

Phase 2 - Admin Console Interface: Build visual control panel with role creation wizard, permission assignment grid showing live user counts, bulk operations for role assignments, and permission diff viewer highlighting changes in green/red.

Phase 3 - Security and Audit Infrastructure: Wire up background job processing audit log and detecting anomalies. Create dashboard widget showing 24-hour permission change timeline. Implement Slack/email notifications for high-risk actions. Build access review campaign system.

Phase 4 - Developer Experience: Create JavaScript SDK with boolean-returning permission check functions. Build React hooks for component-level checks. Develop Express middleware for route protection. Write migration guide from hardcoded checks. Create interactive permission playground.

Phase 5 - Testing and Edge Cases: Test conflicting roles behavior, implement circular inheritance prevention, handle race conditions during permission changes, test cache invalidation at scale, build graceful degradation fallback.

Phase 6 - Monitoring and Observability: Set up Prometheus metrics tracking latency, cache hit rate, and denials. Create Grafana dashboard visualizing performance. Implement error tracking distinguishing bugs from legitimate denials. Generate weekly optimization reports.

Phase 7 - Rollout Strategy and Migration: Implement feature flag system for gradual enablement. Create shadow mode logging differences between systems. Prepare emergency rollback runbook. Develop training materials for non-technical admins.

#RBAC SYSTEM CRITERIA:
1. Permission Model Requirements:
   - Multi-tenant isolation with organization boundaries
   - Support Admin, Manager, Editor, Viewer plus custom roles
   - Granular permissions with action-based syntax (users:read, projects:write, billing:delete)
   - Resource-level permissions for per-project/per-team scoping
   - Permission inheritance and role composition
   - Time-bound access grants for temporary privileges

2. Technical Architecture:
   - Backend: Node.js with TypeScript, PostgreSQL with row-level security
   - API: RESTful endpoints plus WebSocket for real-time updates
   - Caching: Redis achieving sub-10ms lookups
   - Frontend: React with TypeScript using shadcn/ui
   - State: Zustand for permissions, React Query for synchronization

3. Security Features:
   - Immutable audit trail capturing who/what/when/why
   - Permission evaluation order: DENY → resource-level → role-based → time-bound → DEFAULT DENY
   - 10,000+ permission checks per second capability
   - Full permission matrix export for auditors
   - Automated privilege escalation alerts
   - Quarterly access reviews
   - Separation of duties enforcement

4. UI/UX Requirements:
   - Vercel dashboard clarity + Linear information density aesthetic
   - Split-panel admin console with left navigation
   - Card grid displaying live user counts and permission heatmaps
   - Drag-and-drop permission assignment with visual trees
   - Real-time activity feed
   - Color-coded risk indicators (red: admin, yellow: write, green: read)
   - Dark mode with slate-900 background, zinc-800 cards
   - Emerald-500 for active permissions, red-500 for revoked
   - Glassmorphism modals with backdrop blur

5. Success Criteria:
   - Sub-20ms permission check latency at p99
   - Zero unauthorized access incidents in 90 days
   - 100% audit trail coverage
   - Pass SOC 2 audit on first attempt
   - 80% developer adoption within 60 days
   - Support 1M+ users without architectural changes

#INFORMATION ABOUT ME:
- My company size: [NUMBER OF USERS]
- My compliance requirements: [COMPLIANCE STANDARDS NEEDED]
- My current tech stack: [EXISTING TECHNOLOGIES]
- My team size: [NUMBER OF DEVELOPERS]
- My timeline: [DEADLINE FOR IMPLEMENTATION]
- My budget constraints: [BUDGET RANGE]

#RESPONSE FORMAT:
Provide implementation in multi-file project structure with:
- Database schema files with migrations and security policies
- TypeScript permission evaluation engine with test suite
- React admin console components (fully responsive)
- RESTful API endpoints with WebSocket support
- Developer SDK with TypeScript types, React hooks, middleware
- Audit log viewer with filtering, search, export
- Migration guide documentation
- Performance benchmark results
- Proper separation of concerns in maintainable folder architecture

Each code file should include comprehensive comments explaining security decisions and performance optimizations. Include visual mockups for admin console screens using ASCII art or descriptive layouts.
```
