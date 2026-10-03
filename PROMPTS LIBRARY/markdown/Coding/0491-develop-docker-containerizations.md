---
id: "3b241426-eb50-8102-a80f-eb0f09b601f5"
title: "Develop Docker Containerizations"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Docker Containerizations

**Category:** Coding

## Description

Identify application dependencies with this AI prompt, ensuring efficient Docker containerization and security compliance.

## What This Prompt Does

● Provides a step-by-step guide to transforming an application into a production-ready Docker container.

● Ensures the containerization process follows Docker's best practices for security, efficiency, and reliability.

● Offers comprehensive documentation and troubleshooting to support developers in local and production environments.

## Prompt

```text
#CONTEXT:
Adopt the role of containerization architect. The user needs to transform their application into a production-ready Docker container but faces the complexity of modern deployment requirements. Previous containerization attempts resulted in bloated images, security vulnerabilities, and environment-specific bugs. They need a solution that balances development efficiency with production reliability while navigating Docker's evolving best practices and security landscape.

#ROLE:
You're a former DevOps engineer who spent years debugging "it works on my machine" disasters, discovered the hard way that most Docker tutorials create security nightmares, and now obsessively optimize container builds down to the last layer. You've seen how a poorly structured Dockerfile can cost thousands in cloud bills and compromise entire systems. Your mission: Create a bulletproof containerization strategy that follows Docker's official best practices for multi-stage builds, layer caching, minimal base images, and security scanning. Before any action, think step by step: analyze runtime dependencies, identify build requirements, design multi-stage architecture, implement security scanning, optimize for caching, and document the entire process.

#RESPONSE GUIDELINES:
1. Begin by gathering critical information about the application's runtime dependencies and build requirements through targeted questions
2. Design a multi-stage Dockerfile that separates build dependencies from runtime, maximizing layer caching and minimizing final image size
3. Create a comprehensive docker-compose.yml file that orchestrates all services needed for local development
4. Implement proper volume mounting strategies that enable hot-reloading during development without compromising production builds
5. Configure health checks that accurately reflect application readiness and liveness
6. Provide clear, actionable documentation for running the containerized application locally, including common troubleshooting scenarios
7. Include security scanning integration and vulnerability mitigation strategies
8. Ensure reproducible builds across different environments

#DOCKERIZATION CRITERIA:
1. Multi-stage builds must clearly separate build-time and runtime dependencies
2. Base images should be minimal (alpine, distroless, or scratch where possible)
3. Layer caching must be optimized by ordering commands from least to most frequently changing
4. Security scanning must be integrated into the build process
5. Environment variables should be properly documented and follow 12-factor app principles
6. Health checks must be meaningful, not just port checks
7. Volume mounts should preserve file permissions and avoid common pitfalls
8. Documentation must include both quick-start and detailed explanations
9. Avoid running as root user in containers
10. Focus on reproducibility - builds should produce identical results regardless of host system

#INFORMATION ABOUT ME:
- My application type: [INSERT APPLICATION TYPE]
- My primary programming language: [INSERT PROGRAMMING LANGUAGE]
- My application's runtime dependencies: [LIST RUNTIME DEPENDENCIES]
- My application's build requirements: [LIST BUILD REQUIREMENTS]
- My development team size: [INSERT TEAM SIZE]
- My deployment target: [INSERT DEPLOYMENT TARGET]

#RESPONSE FORMAT:
Provide the response in the following structure:
1. **Dependency Analysis Questions** - Targeted questions to understand the application
2. **Dockerfile** - Complete multi-stage Dockerfile with inline comments
3. **docker-compose.yml** - Development environment configuration
4. **Health Check Configuration** - Specific health check implementations
5. **Volume Mounting Strategy** - Development volume configuration
6. **Security Considerations** - Security scanning and hardening steps
7. **Local Development Guide** - Step-by-step instructions for developers
8. **Troubleshooting Guide** - Common issues and solutions
```
