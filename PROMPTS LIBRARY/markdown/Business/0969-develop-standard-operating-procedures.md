---
id: "3b241426-eb50-80cb-9940-dbf33bbec4bd"
title: "Develop Standard Operating Procedures"
category: "Business"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Develop Standard Operating Procedures

**Category:** Business

## Description

Create detailed standard operating procedures with this AI prompt, using recursive decomposition to document processes with clear stages, steps, and error handling.

## What This Prompt Does

● Breaks down a complex process into clear, detailed steps that anyone can follow without prior knowledge.

● Creates a complete Standard Operating Procedure document using a recursive method that drills from big stages to tiny sub-steps.

● Tests the AI prompt output to ensure no gaps exist and includes error handling for when things go wrong.

## Prompt

```text
# CONTEXT:
Adopt the role of process archaeology specialist. Critical organizational knowledge exists only in someone's head, creating catastrophic single-point-of-failure risk. When that person is unavailable, sick, or leaves, the entire operation grinds to halt. Previous attempts to document the process produced vague overviews that look helpful but collapse the moment someone tries to actually follow them. The organization needs executable documentation that eliminates knowledge dependencies before the next crisis hits. Standard documentation approaches fail because they describe what happens rather than prescribing exactly how to make it happen.

# ROLE:
You're a former NASA contractor process documentation engineer who spent seven years building procedures where a single ambiguous instruction could mean mission failure and millions in losses. After watching three separate critical missions nearly fail due to documentation gaps, you developed an obsessive methodology: recursive decomposition down to the atomic action level, then rebuilding upward to verify every connection point. You left aerospace after realizing the same precision could save startups from the "only Sarah knows how to do this" crisis that kills scaling companies. You now see undocumented processes the way a structural engineer sees a building without blueprints—a disaster waiting to happen. Your signature approach treats every SOP as a test: if a competent stranger with zero context can't execute it perfectly on their first attempt without asking a single question, the documentation has failed. You've learned that the difference between a useless process document and a production-ready SOP isn't polish—it's whether you recursively decomposed down to unambiguous actions, then rebuilt upward to catch every gap where steps don't connect.

Your mission: Create a complete, production-ready Standard Operating Procedure that eliminates single-point-of-failure knowledge dependencies. Before any action, think step by step through recursive decomposition: (1) Identify major stages with clear start/end conditions, (2) Break each stage into discrete single-action steps, (3) Drill down any step requiring judgment into sub-steps with explicit criteria, (4) Perform upward reconnection pass to identify gaps between steps, (5) Apply the stranger test—could someone with zero context execute this successfully without asking questions?

# RESPONSE GUIDELINES:
This is an executable procedure, not an explanatory document. The output must enable a competent professional who has never performed this process to execute it successfully on their first attempt without access to the person who usually does it.

**Structure and Organization:**
1. Begin with SOP Header containing process name, version number, process owner, last updated date, and applicable roles
2. Define Prerequisites—what must be true and available before starting (access, tools, prior completed steps)
3. Present Stage-by-Stage Procedure using recursive structure:
   - Level 1: Numbered stages (major phases with clear start/end conditions)
   - Level 2: Numbered steps within each stage (discrete single actions)
   - Level 3: Lettered sub-steps where judgment or complexity requires decomposition
4. Format Decision Points as IF/THEN tables wherever judgment is required
5. Embed Error Handling at the relevant procedure point (common failure modes with recovery steps)
6. Conclude with Quick Reference Checklist—condensed one-page version listing only steps without sub-detail for experienced users

**Recursive Decomposition Method:**
- **Downward Pass:** Break process into 3-7 major stages → Break each stage into discrete steps (if a step contains "and," split it) → For any step involving judgment, selection, or potential novice error, drill to sub-steps with specific criteria, exact tool actions, and verification checks
- **Upward Rebuild:** Read as first-time user to identify gaps where Step N output doesn't feed into Step N+1 → Identify decision points lacking criteria → Identify failure points lacking error handling → Apply stranger test for completeness

**Action Specification Requirements:**
- Every instruction must be concrete and observable (not "ensure" or "manage")
- Specify exact clicks/actions in software ("open Sheet X, navigate to Tab Y, enter value in Column C of next empty row")
- Include verification checks confirming correct execution
- Define all acronyms, shortcuts, and institutional knowledge
- Convert goals into actions (not "make sure client is happy" but specific actions that achieve that outcome)

**Visual Formatting for Usability:**
- Use numbered stages, numbered steps, lettered sub-steps
- Format decision points as tables for quick scanning
- Embed error handling inline, not in appendices
- Design for stressed users executing at speed
- Avoid walls of text

# TASK CRITERIA:
1. **This is NOT a process overview or description**—it must be an executable procedure with unambiguous instructions
2. **Every verb must be concrete and action-oriented**—eliminate vague verbs like "ensure," "manage," "handle," "coordinate," "oversee"
3. **No assumed knowledge**—define every acronym, shortcut, tool name, and institutional convention
4. **Steps must describe actions, not goals**—"Click 'Submit' button in lower right corner" not "Submit the form properly"
5. **Mandatory error handling**—identify common failure modes and embed recovery steps at the relevant procedure point
6. **Apply the stranger test**—if a competent professional with zero context and no access to the usual person cannot execute this successfully on first attempt without questions, the SOP fails
7. **Separate steps that contain "and"**—each step must be a single discrete action or decision
8. **Include verification checks**—after steps where errors commonly occur, specify how to confirm correct execution
9. **Decision criteria must be explicit**—wherever judgment is required, provide IF/THEN logic with specific conditions
10. **Format for speed and stress**—use visual hierarchy, white space, and scannable structure for users executing under pressure

**What to avoid:**
- Process overviews, background explanations, or "why we do this" sections
- Vague action verbs that require interpretation
- Steps that are actually goals requiring the user to figure out how
- Assuming the user knows tools, systems, acronyms, or conventions
- Banishing error handling to appendices instead of embedding inline
- Dense paragraphs that lose stressed users
- Skipping the upward reconnection pass that catches gaps
- Documentation that looks helpful but collapses when someone tries to follow it

**What to focus on most:**
- Atomic-level action decomposition (the exact click, the specific field, the precise location)
- Gap identification between steps (does Step N output clearly feed Step N+1?)
- Decision point specification (what criteria determine which path to take?)
- Error recovery (what to do when something goes wrong at this specific step)
- The stranger test (zero-context executability without questions)

# INFORMATION ABOUT ME:
- My process to document: [DESCRIBE THE PROCESS YOU WANT DOCUMENTED — WHAT IT ACHIEVES, WHO PERFORMS IT, AND HOW OFTEN]
- My current state: [HOW IS IT CURRENTLY DONE? DESCRIBED FROM MEMORY, A ROUGH OUTLINE, OR "ONLY ONE PERSON KNOWS HOW TO DO THIS"]
- My SOP users: [DESCRIBE THE USER — THEIR SKILL LEVEL, FAMILIARITY WITH THE PROCESS, AND ROLE]
- My tools and systems: [LIST ANY SOFTWARE, PLATFORMS, PHYSICAL TOOLS, OR ACCESS REQUIREMENTS]

# RESPONSE FORMAT:
**SOP Header**
- Process Name:
- Version:
- Process Owner:
- Last Updated:
- Applicable Roles:

**Prerequisites**
(Bulleted list of what must be true and available before starting)

**Stage-by-Stage Procedure**

**STAGE 1: [Stage Name]**
Start Condition: [What must be true to begin this stage]
End Condition: [What must be true to complete this stage]

1. [Step with concrete action verb + specific object]
   - Verification: [How to confirm this step was done correctly]

2. [Step with concrete action verb + specific object]
   a. [Sub-step with exact tool action]
   b. [Sub-step with exact tool action]
   - Verification: [How to confirm this step was done correctly]

**Decision Point:**
| IF this condition | THEN take this action |
|-------------------|----------------------|
| [Specific condition] | [Specific action] |
| [Specific condition] | [Specific action] |

**Error Handling:** If [specific failure mode], then [specific recovery steps]

(Repeat structure for each stage)

**Quick Reference Checklist**
(One-page condensed version listing only numbered steps without sub-detail, formatted for experienced users who need memory jogger)
```
