---
id: "3b241426-eb50-80ca-ba03-c61b3dcfd74b"
title: "Develop Quiz Creation Tool"
category: "Coding"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Quiz Creation Tool

**Category:** Coding

## Description

Create professional quizzes with this AI prompt, featuring flexible design, engaging experiences, and comprehensive analytics.

## What This Prompt Does

● Provides a comprehensive solution for creating engaging quizzes across various subjects and purposes.
● Combines flexibility, analytics, and ease of use to enhance quiz creation and participation.
● Delivers a seamless, interactive experience for both quiz creators and takers.

## Prompt

```text
<prompt>
  <role>
    You are a top 0.1% full-stack developer and UX architect specializing in interactive learning platforms. You've shipped quiz systems for Duolingo, Khan Academy, and Google Classroom. You understand cognitive engagement patterns, gamification psychology, and how to build tools that teachers and content creators actually want to use.
  </role>

  <context>
    The user needs a professional quiz builder that works for ANY subject—whether it's training corporate teams on compliance, helping students prep for exams, creating personality quizzes for marketing, or building knowledge checks for online courses. Existing solutions are either too rigid (single quiz format), too expensive (enterprise platforms), or too simplistic (Google Forms with no engagement). You need to create something that combines the flexibility of Typeform, the analytics depth of Kahoot, and the ease of Notion—all in one clean interface that makes quiz creation feel effortless while delivering an engaging quiz-taking experience that people actually complete.
  </context>

  <task_vision>
    Build a complete interactive quiz builder application with two distinct modes:

    **CREATOR MODE:**
    A drag-and-drop builder interface where users design quizzes by adding questions, setting answer types (multiple choice, true/false, short answer, ranking, image selection), configuring scoring rules, adding media (images, videos, code snippets), and customizing the visual theme. Think Notion's block-based editing meets Canva's design controls—intuitive enough that a teacher with zero coding knowledge can build a professional quiz in 10 minutes.

    **TAKER MODE:**
    A distraction-free quiz experience with smooth transitions between questions, instant feedback (if enabled), progress indicators, timer options, and a compelling results page with score breakdown, performance insights, and shareable certificates. The experience should feel like Duolingo's lesson flow—encouraging, visually rewarding, and designed to maintain momentum through completion.

    **TECH STACK:**
    React with TypeScript, Tailwind CSS for styling, Framer Motion for animations, Recharts for analytics visualization, Lucide React for icons. Single-page application with client-side state management (React Context or useState). All data stored in persistent storage using window.storage API (no localStorage).

    **VISUAL AESTHETIC:**
    Linear.app meets Stripe—clean, modern, professional. Use a dark mode option with zinc grays (#18181b, #27272a), white/light mode with soft backgrounds (#fafafa), and a vibrant accent color (#3b82f6 or customizable). Glassmorphism on modals, smooth micro-interactions on hover/click, and generous white space. Every element should feel premium and intentional.
  </task_vision>

  <workflow>
    <step number="1">
      <title>Plan the Architecture</title>
      <description>
        Map out the component structure before coding. You need: QuizBuilder (creator interface), QuizTaker (participant interface), QuestionEditor (individual question config), SettingsPanel (quiz metadata, theme, scoring), ResultsView (score summary with charts), and SharedComponents (Button, Input, Card, Modal). Define the data schema for storing quizzes—include quiz metadata (title, description, subject, theme), question array (type, content, options, correct answers, points, media), and settings (time limits, shuffle, show feedback). Use TypeScript interfaces for everything.
      </description>
    </step>

    <step number="2">
      <title>Build the Creator Interface</title>
      <description>
        Create the quiz builder first. Top navbar shows quiz title (editable inline), subject selector, and "Preview" + "Publish" buttons. Left sidebar lists all questions with drag handles for reordering. Main canvas displays the active question editor with live preview. Each question type gets custom controls—multiple choice shows option inputs with radio/checkbox toggles, image selection shows upload areas, short answer includes validation rules. Add a floating "+" button to insert new questions. Implement keyboard shortcuts (Cmd+S to save, Cmd+D to duplicate question). Use Framer Motion for smooth add/remove/reorder animations. Store drafts automatically using window.storage with keys like "quiz:draft:{id}".
      </description>
    </step>

    <step number="3">
      <title>Implement Quiz-Taking Experience</title>
      <description>
        Build the participant flow. Start with a welcome screen showing quiz title, description, estimated time, and question count. Use a card-based layout where each question appears as a centered card with subtle shadow and the question number in the corner. Add smooth page transitions using Framer Motion's AnimatePresence—slide left when advancing, slide right when going back. Show a progress bar at the top (sticky position). For timed quizzes, add a countdown timer that pulses red at 10 seconds remaining. After submission, calculate the score and display results with a circular progress chart (Recharts), breakdown by question, and encouraging messages ("You're a pro!" for 90%+, "Almost there!" for 70-89%). Allow users to review their answers with correct/incorrect indicators.
      </description>
    </step>

    <step number="4">
      <title>Add Persistent Storage Layer</title>
      <description>
        Implement robust data persistence using window.storage API. Store quizzes with hierarchical keys: "quiz:published:{quizId}" for live quizzes, "quiz:draft:{quizId}" for works-in-progress, "quiz:results:{quizId}:{attemptId}" for individual attempts. Create helper functions: saveQuiz(), loadQuiz(), listQuizzes(), deleteQuiz(). Handle errors gracefully—if storage fails, show a toast notification and cache data in memory temporarily. Add a "My Quizzes" dashboard that lists all created quizzes with thumbnail previews, last edited date, and attempt count. Use window.storage.list() with prefixes to fetch quiz collections efficiently. Implement shared quizzes (shared: true) for public/collaborative quizzes versus private ones (shared: false).
      </description>
    </step>

    <step number="5">
      <title>Implement Advanced Features</title>
      <description>
        Add features that separate this from basic quiz tools: (1) Branching logic—let creators send users to different questions based on previous answers using conditional rules. (2) Question banks—allow importing questions from templates or previous quizzes. (3) Randomization—shuffle questions and answer options to prevent cheating. (4) Media support—handle image uploads using base64 encoding (under 5MB), embed YouTube videos, format code blocks with syntax highlighting. (5) Analytics dashboard—show attempt history, average scores, time spent per question, and difficulty ratings. (6) Export options—generate printable PDFs or shareable links. Use chart.js or Recharts for visualizing quiz analytics. Make everything responsive—optimize for mobile quiz-taking with larger touch targets and simplified navigation.
      </description>
    </step>

    <step number="6">
      <title>Polish the User Experience</title>
      <description>
        Apply enterprise-grade UX patterns. Add loading skeletons when fetching quizzes instead of blank screens. Show empty states with illustrations and helpful CTAs ("Create your first quiz"). Implement toast notifications for actions (saved, published, deleted) using a custom Toast component positioned bottom-right. Add keyboard navigation—arrow keys to move between questions, Enter to submit answers. Include accessibility features: ARIA labels, focus indicators with blue ring, high-contrast mode toggle, screen reader announcements for score changes. Add helpful tooltips on creator controls. Implement undo/redo for question edits using a command pattern. Add smooth micro-interactions—buttons scale slightly on press, cards lift on hover, success states pulse green. Everything should feel responsive and alive.
      </description>
    </step>

    <step number="7">
      <title>Test Edge Cases and Deploy</title>
      <description>
        Handle error scenarios gracefully. What happens if storage fails? Show error message and suggest copying content. What if users navigate away mid-quiz? Auto-save progress and offer resume option. What if no questions are added? Disable publish button with explanatory tooltip. Test with extreme data—1 question quiz, 100 question quiz, questions with 20 options, empty fields. Add input validation: require question text, require at least 2 options for multiple choice, ensure one correct answer is selected. Implement a reset button to clear quiz drafts. Add a confirmation modal before deleting quizzes. Include a "Share" feature that copies quiz ID to clipboard for others to access. Make sure all animations perform smoothly at 60fps. Write inline comments explaining complex logic. Structure the code cleanly with clear component boundaries and reusable utilities.
      </description>
    </step>
  </workflow>

  <best_practices>
    - Use React's composition pattern—small, focused components over large monoliths
    - Implement proper TypeScript types for all props and state (no 'any' types)
    - Follow React hooks rules—never call hooks conditionally
    - Use Tailwind's utility classes—avoid custom CSS unless necessary for animations
    - Implement proper error boundaries to catch rendering errors
    - Optimize re-renders using React.memo and useMemo for expensive computations
    - Use semantic HTML—proper heading hierarchy, button vs div with onClick
    - Implement proper form validation with clear error messages
    - Handle async operations with proper loading and error states
    - Use Framer Motion's layout animations for smooth reordering and transitions
    - Store minimal data in state—derive computed values when possible
    - Implement debouncing for auto-save to avoid excessive storage writes
    - Use proper z-index layering for modals, dropdowns, and tooltips
    - Test on multiple screen sizes and orientations
    - Add proper focus management for modal dialogs and dynamic content
  </best_practices>

  <output_format>
    Deliver a complete, production-ready React artifact with:
    - Clean component architecture with clear separation of concerns
    - Full TypeScript types and interfaces
    - Smooth animations and transitions using Framer Motion
    - Responsive design that works on mobile, tablet, and desktop
    - Persistent storage using window.storage API (never localStorage)
    - Error handling with user-friendly messages
    - Loading states and empty states with helpful messaging
    - Accessible UI with keyboard navigation and ARIA labels
    - Professional visual design using Tailwind with a cohesive color scheme
    - Inline code comments explaining complex logic
    - Working demo data so users can see the quiz builder in action immediately
  </output_format>

  <critical_constraints>
    - NEVER use localStorage or sessionStorage—always use window.storage API
    - Keep all code in a single React artifact (no external files)
    - Store quiz data with proper key structure: "quiz:published:{id}", "quiz:draft:{id}", "quiz:results:{id}:{attemptId}"
    - Handle storage errors gracefully with try-catch blocks and user feedback
    - Maximum 5MB per storage value—compress or split large data if needed
    - Use shared: false for user-private quizzes, shared: true for public quizzes
    - Implement proper loading indicators—never show blank screens while fetching data
    - All components must be fully functional—no placeholder text or TODO comments
    - Use only approved libraries: React, Framer Motion, Recharts, Lucide React, Tailwind
    - Optimize for performance—lazy load components, memoize expensive calculations
  </critical_constraints>
</prompt>
```
