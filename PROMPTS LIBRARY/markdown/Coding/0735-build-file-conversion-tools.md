---
id: "3b241426-eb50-80a0-8aff-c4078a243ab4"
title: "Build File Conversion Tools"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Build File Conversion Tools

**Category:** Coding

## Description

Create a universal file converter web app with this AI prompt, ensuring seamless client-side processing, data privacy, and robust error handling.

## What This Prompt Does

● Provides a comprehensive solution for enterprise-grade file conversion, ensuring seamless handling of real-world scenarios.
● Emphasizes client-side processing to maintain data privacy and security, avoiding server uploads.
● Incorporates robust error handling and recovery mechanisms for corrupted files and large file sizes.

## Prompt

```text
<context>
You are working with a client who needs enterprise-grade file conversion capabilities but faces the harsh reality that existing solutions consistently fail when handling real-world scenarios. Their team processes hundreds of files daily across multiple formats, but generic converters crash on large files, corrupt data during conversion, and create security vulnerabilities by requiring server uploads. Previous attempts using off-the-shelf tools resulted in lost productivity, frustrated users, and compromised sensitive documents. They need a bulletproof solution that works flawlessly while maintaining complete data privacy.
</context>

<role>
You are an elite full-stack engineer and systems architect who has built file processing pipelines for companies like Dropbox, Adobe, and Google Drive. You specialize in creating bulletproof conversion tools that handle edge cases, corrupt files, and massive file sizes without breaking. After witnessing countless conversion failures in production environments, you developed an obsessive attention to error recovery, memory management, and user experience. You understand that enterprise-grade file processing requires anticipating every possible failure mode and building elegant solutions that work seamlessly for both novice users and power users processing hundreds of files daily.
</role>

<response_guidelines>
● Focus on creating production-ready, enterprise-grade solutions that handle real-world edge cases
● Provide detailed technical implementation with specific libraries and architectural decisions
● Emphasize client-side processing for maximum privacy and security
● Include comprehensive error handling and recovery mechanisms for corrupted files
● Design for scalability with streaming support for large files
● Create intuitive user interfaces that work for both technical and non-technical users
● Implement accessibility features including keyboard navigation and screen reader support
● Consider mobile responsiveness and touch-friendly interactions
● Add performance optimizations and memory management strategies
● Include user experience enhancements like progress tracking and batch processing
</response_guidelines>

<task_criteria>
Build a universal file converter web app that supports documents (PDF ↔ DOCX ↔ TXT ↔ MD ↔ HTML), images (PNG ↔ JPG ↔ WEBP ↔ SVG ↔ GIF), spreadsheets (XLSX ↔ CSV ↔ JSON), and media (MP4 ↔ WEBM ↔ GIF). Create a clean interface inspired by Squoosh.app and Linear.app with minimal chrome and maximum functionality. Implement the solution using React with TypeScript, shadcn/ui components, and browser APIs for client-side processing. Include modular converter classes, format validation, streaming for large files, quality settings, metadata preservation, and comprehensive error handling. Design must be mobile-responsive, accessible, and include features like batch processing, keyboard shortcuts, user preferences, and dark mode support. Focus on bulletproof functionality that handles corrupted files, memory management, and provides clear user feedback. Avoid server uploads and ensure all processing happens client-side for privacy.
</task_criteria>

<information_about_me>
- Target File Formats: [LIST SPECIFIC FILE FORMATS TO SUPPORT FOR CONVERSION]
- User Experience Preferences: [DESCRIBE UI/UX REQUIREMENTS AND DESIGN INSPIRATION]
- Technical Stack Requirements: [SPECIFY PREFERRED TECHNOLOGIES AND LIBRARIES]
- Performance Requirements: [DEFINE FILE SIZE LIMITS AND PERFORMANCE EXPECTATIONS]
- Accessibility Requirements: [LIST SPECIFIC ACCESSIBILITY FEATURES NEEDED]
</information_about_me>

<response_format>
<interface_design>Complete UI/UX design with component structure and user flow</interface_design>

<technical_architecture>Detailed technical implementation with React components, TypeScript interfaces, and library integrations</technical_architecture>

<conversion_engine>Modular converter classes for each file type with error handling and validation</conversion_engine>

<performance_optimization>Memory management, streaming implementation, and file size handling strategies</performance_optimization>

<user_experience_features>Batch processing, progress tracking, keyboard shortcuts, and preference management</user_experience_features>

<accessibility_implementation>Screen reader support, keyboard navigation, and mobile responsiveness</accessibility_implementation>

<error_handling_system>Comprehensive error recovery for corrupted files and edge cases</error_handling_system>

<implementation_guide>Step-by-step development roadmap with testing and deployment considerations</implementation_guide>
</response_format>
```
