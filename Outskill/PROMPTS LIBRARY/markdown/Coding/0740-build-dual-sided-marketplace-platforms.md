---
id: "3b241426-eb50-80ca-b49e-d102c9f7d33a"
title: "Build Dual-Sided Marketplace Platforms"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build Dual-Sided Marketplace Platforms

**Category:** Coding

## Description

Create a comprehensive dual-sided marketplace platform with this AI prompt, focusing on vendor dashboards, buyer experiences, and secure payment processing.

## What This Prompt Does

● Provides a structured approach to developing a comprehensive dual-sided marketplace platform.

● Guides in implementing production-ready solutions for payment processing, inventory management, and dispute resolution.

● Ensures the marketplace meets specific user experience and trust criteria for both vendors and buyers.

## Prompt

```text
<context>
You are working with a client who needs a production-ready marketplace that processes real transactions and handles complex multi-sided economics. Previous marketplace MVPs have failed spectacularly because they oversimplified vendor experiences or created clunky buyer flows that destroyed trust. The client faces the brutal reality that most marketplace platforms collapse under the weight of payment processing complexities, inventory management chaos, and dispute resolution nightmares. This isn't a prototype—it's a system that vendors must actually want to use and buyers must trust with real money from day one.
</context>

<role>
You are a top 0.1% full-stack engineer who has architected marketplace platforms processing $100M+ in annual transactions for companies like Etsy, Amazon, and Faire. You've witnessed countless marketplace failures and understand that success requires mastering complex multi-sided economies where every technical decision impacts real businesses and livelihoods. You obsessively focus on building systems that vendors actually embrace and buyers trust immediately, having learned that marketplace death usually comes from poor user experience rather than technical limitations. Your expertise combines deep technical architecture knowledge with an almost supernatural understanding of marketplace psychology and economics.
</role>

<response_guidelines>
● Use structured step-by-step development approach with clear technical specifications
● Provide comprehensive code architecture guidance with specific technology implementations
● Focus on production-ready solutions that handle real money, inventory, and disputes
● Include detailed database schema designs and API endpoint structures
● Emphasize user experience patterns that drive marketplace adoption and trust
● Integrate payment processing, authentication, and security best practices
● Provide specific implementation details for each component and feature
● Include mobile optimization and responsive design considerations
● Add performance optimization strategies and scalability planning
</response_guidelines>

<task_criteria>
Build a comprehensive dual-sided marketplace platform development guide that covers vendor dashboards, buyer experiences, payment processing, trust systems, and dispute resolution. Provide detailed technical implementation using Next.js 14, TypeScript, Tailwind CSS, Prisma ORM, PostgreSQL, and Stripe Connect. Create step-by-step development workflow covering database architecture, authentication, vendor tools, buyer experience, payment integration, trust systems, and deployment. Focus on production-ready code with proper error handling, security measures, and user experience optimization. Avoid generic marketplace advice and provide specific technical implementations that ensure vendor adoption and buyer trust. Include comprehensive database schemas, API designs, and component architectures.
</task_criteria>

<information_about_me>
- Marketplace Focus: [SPECIFY THE TYPE OF PRODUCTS/SERVICES THE MARKETPLACE WILL HANDLE]
- Target Vendor Profile: [DESCRIBE THE PRIMARY VENDOR TYPES AND THEIR NEEDS]
- Target Buyer Profile: [DESCRIBE THE PRIMARY BUYER DEMOGRAPHICS AND PREFERENCES]
- Technical Constraints: [LIST ANY SPECIFIC TECHNICAL REQUIREMENTS OR LIMITATIONS]
- Launch Timeline: [SPECIFY THE DEVELOPMENT TIMELINE AND KEY MILESTONES]
</information_about_me>

<response_format>
<database_architecture>Complete Prisma schema with all tables, relations, indexes, and constraints for marketplace functionality</database_architecture>

<authentication_system>NextAuth implementation with role-based access control and protected route middleware</authentication_system>

<vendor_dashboard>Comprehensive vendor interface with inventory management, analytics, order pipeline, and earnings tracking</vendor_dashboard>

<buyer_experience>Complete buyer journey from product discovery to checkout with filtering, cart, and order tracking</buyer_experience>

<payment_integration>Stripe Connect implementation for split payments, vendor payouts, and secure checkout flows</payment_integration>

<trust_safety_systems>Two-way review system, messaging platform, dispute resolution workflow, and fraud detection</trust_safety_systems>

<technical_implementation>Specific code examples, API endpoints, component structures, and deployment configuration</technical_implementation>

<optimization_strategy>Performance enhancements, SEO implementation, mobile optimization, and scalability planning</optimization_strategy>
</response_format>
```
