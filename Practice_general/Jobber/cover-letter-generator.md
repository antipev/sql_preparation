# Skill: cover-letter-generator

## Purpose
Generate a targeted, human-like cover letter for a specific job posting using a candidate's resume, Plum Profile, portfolio, LinkedIn, and accomplishments. The output must be in .docx format and tailored to the role. The skill must handle location/hybrid constraints honestly and confidently — without apology, without over-explaining, and without asking for a "remote exception" unless the company already has remote roles in the same function. All tenure and date calculations must be verified against the resume. Every sentence must add new information — no restating the same claim twice. Portfolio and demo links must be embedded directly in the body with descriptive anchor text (no raw URLs, no separate P.S. link list).

## Inputs Required
1. **Resume file** (PDF or text) — candidate's full career history.
2. **Plum Profile report** (PDF or text) — top talents, strengths, and professional fit descriptions.
3. **Job posting file** (PDF, DOCX, or text) — full job description, including location, hybrid/remote status, and key responsibilities.
4. **Portfolio links list** — one or more of the following, as provided by the user:
   - Primary portfolio website (e.g., GitHub Pages).
   - Specific project link(s) (e.g., `.../Project_1.md`).
   - Project overview link (e.g., `PROJECT_OVERVIEW.md`).
   - Live demo links (e.g., Dagster UI, dbt docs, Malloy Publisher, Credible workspace).
   - GitHub repo/profile URL.
5. **LinkedIn URL** — professional profile.
6. **Accomplishments URL** — specific achievement post(s) on LinkedIn or elsewhere.
7. **Candidate contact block** — name, location, phone, email, portfolio, LinkedIn.
8. **Hiring manager name** (if available from job posting).
9. **Location stance** — one of: "willing to relocate," "not willing to relocate," "open to discussion."
10. **Remote precedent** (optional but recommended) — whether the company has remote roles in the same function. If true, use this as a confident anchor.
11. **Posting locations** (if multiple) — e.g., "Toronto, Edmonton, Vancouver." Use all of them in the letter to acknowledge the multi-city search.
12. **Length target** — default: 4 paragraphs + closing (approx. 350–450 words). Shortened format embeds links inline and removes the P.S. list.

## Process

### Step 1: Parse and Extract
- From the **resume**: extract top 3–5 relevant roles, skills that match the JD, and quantifiable achievements.
- **Tenure verification (mandatory):** Before writing "X years of experience," calculate the actual duration from the resume's start/end dates for the relevant role(s). Do not round up or guess. If the resume says "July 2020 – Present" and the letter is dated November 2026, write "six years," not "five years." If multiple roles are combined, sum the durations and state the total clearly. Flag any ambiguity in the quality-check step.
- From the **Plum Profile**: extract Top 3 Talents and the "You are:" / "Professionally you are:" descriptions.
- From the **job posting**: extract (a) company mission, (b) team purpose, (c) top 5 required skills, (d) top 3 responsibilities, (e) location/hybrid status and any multiple posting cities, (f) culture keywords.
- From **portfolio/LinkedIn/accomplishments**: note 1–2 unique proof points.
- **Portfolio link rule:** Use the exact URLs the user provides. Embed each link inline with descriptive anchor text (e.g., "[Project 1](URL)", "[project overview](URL)", "[Dagster UI](URL)"). Do NOT append a separate P.S. link list or paste raw URLs.

### Step 2: Handle the Location Constraint — Confidently, Not Defensively
**Core rule:** Do NOT write "I'm not relocating — but I'm also not asking you to compromise." That sentence is self-defeating: it names a limitation and then pre-emptively excuses it. Instead, frame location as context, not a problem.

**If relocating:**
- Open with a direct acknowledgment: "I'm in [City], and this role is [hybrid/on-site] in [Job City]. I'm prepared to relocate and be onsite from day one."
- Do NOT apologize.

**If NOT relocating and the company has remote roles in the same function:**
- Open with a confident, matter-of-fact statement. If there are **multiple posting cities**, acknowledge all of them: "I'm based in [City], and I know this role is posted as [hybrid/on-site] across [City 1], [City 2], and [City 3]."
- Pivot immediately to alignment: "I'm reaching out anyway because [specific alignment]. [Company] already has remote [function] roles, so I'm confident the right conversation here is about impact, not postal codes."
- Use the remote precedent as a **fact**, not a plea.
- Close with a flexible, low-friction offer: "If a distributed arrangement works for this role the way it does for your [function] team, I'd welcome the chance to talk. If an onsite cadence is essential, I'm also open to discussing a practical rhythm that keeps me connected to the team."
- **Tone rule:** Confident, matter-of-fact, no apology.

**If NOT relocating and the company has NO remote precedent:**
- Be direct about the constraint, offer a specific hybrid cadence, and close with respect for their decision.

### Step 3: Build the "You Said / I Did" Bridge (With Embedded Links)
- For each of the top 3 job requirements, create a matching paragraph:
  - **Job requirement** (quote or paraphrase from JD).
  - **Your experience** (specific role, tool, metric, or outcome from resume).
  - **The bridge** (how your experience directly satisfies the requirement).
- Use actual project names and metrics (e.g., "deployed a Looker semantic layer in 2 months," "80%+ adoption," "improved forecast precision by 5%").
- **Embed the most relevant portfolio link in the paragraph where it proves the point.** Example: after describing semantic-layer work, insert "[Project 1](URL)" as a natural reference; after describing pipeline work, insert "[Dagster UI](URL)" and "[dbt docs](URL)".
- **No repetition rule:** Every paragraph must introduce new evidence. Do not restate the opener's tenure claim or re-summarize the same role.

### Step 4: Weave in Plum Talents and Culture Fit
- Insert 1–2 sentences that naturally mention the Plum Top 3 Talents. Do NOT list them mechanically.
- Mirror the company's culture keywords from the JD by connecting them to Plum descriptors.

### Step 5: Link Embedding (Inline Only)
- Embed links directly in the body paragraphs where they serve as evidence.
- Use descriptive anchor text: "[Project 1]", "[project overview]", "[Dagster UI]", "[dbt docs]", "[Malloy semantic layer]".
- Do NOT include a separate P.S. bullet list of links.
- Do NOT include the Credible workspace link unless the user explicitly requests it (it requires sign-in and is not useful to a recruiter).
- Keep all links clickable in the .docx.

### Step 6: Humanize and Shorten the Tone
- Target 4 paragraphs + closing (approx. 350–450 words).
- First-person, conversational phrasing. Avoid corporate jargon.
- Vary sentence length. Use contractions ("I'll," "I'm," "that's").
- Include one moment of personality or humility.
- Do NOT use generic openers like "I am writing to express my interest." Start with a hook.

### Step 7: Output as .docx
- Format in markdown first.
- Convert to .docx using `pandoc` (`pandoc cover-letter.md -o Cover_Letter.docx`) or `python-docx`.
- **File naming:** `[CandidateLastName]_[Company]_Cover_Letter.docx`
- **Formatting:** 1-inch margins, 11pt Calibri/Aptos, single spacing, bold name and headers, horizontal rule under header, "Sincerely," + 3 blank lines + typed name.
- **Subject line rule:** The "Re:" line should contain only the job title. Do NOT append location, work arrangement (e.g., "Hybrid," "Remote"), or employment type.

### Step 8: Quality Checks
- [ ] **Tenure check:** Does every "X years" statement match the resume's calculated duration? (e.g., July 2020 – Nov 2026 = six years, not five.)
- [ ] **Repetition check:** Does any paragraph restate a claim already made? If yes, delete the redundant sentence and replace it with new evidence.
- [ ] **Inline link check:** Are all portfolio/demo links embedded directly in the body with descriptive anchor text? Is there no separate P.S. link list and no raw URLs?
- [ ] **Link relevance check:** Is each link placed in the paragraph where it proves the point (e.g., Project 1 near semantic-layer work, Dagster/dbt docs near pipeline work)?
- [ ] **Sign-in label check:** If a link requires sign-in (e.g., Credible workspace), is it excluded unless explicitly requested?
- [ ] **Length check:** Is the letter approx. 350–450 words (4 paragraphs + closing)?
- [ ] **Multi-location check:** If the posting lists multiple cities, does the opener acknowledge all of them?
- [ ] **Subject line check:** Does the "Re:" line contain only the job title?
- [ ] Does the letter address the location constraint **without self-defeating language**?
- [ ] If the company has remote precedent, is it used as a confident anchor rather than an excuse?
- [ ] Does the letter match at least 3 specific job requirements to specific resume achievements?
- [ ] Does it use at least 2 Plum Talents naturally?
- [ ] Is the tone human, confident, and non-apologetic?
- [ ] Is the .docx properly formatted and saved with the correct filename?

## Example Prompt for the Agent
> "Generate a shortened cover letter for [Candidate] applying to [Company] for the [Role] position. Use my resume, Plum Profile, LinkedIn at [URL], and accomplishments at [URL]. Embed these portfolio links directly in the body with descriptive anchor text: [Project 1 URL], [PROJECT_OVERVIEW.md URL], [Dagster UI URL], [dbt docs URL], [Malloy Publisher URL]. Do not use a separate P.S. link list. The role is hybrid and posted in [City 1], [City 2], and [City 3]; I am in [My City]. I am NOT willing to relocate. Note that [Company] already has remote [function] roles. Address the location conversation confidently. **Verify all tenure calculations against my resume before writing, and eliminate any sentence that repeats a claim already made.** Target 4 paragraphs + closing. Output as a .docx file named [LastName]_[Company]_Cover_Letter.docx."

## Notes
- Always prioritize the candidate's real metrics and project names over generic claims.
- If the job posting includes a hiring manager name, address the letter to them.
- If the Plum Profile is unavailable, use a strengths-based summary from the resume instead.
- **Anti-patterns to avoid:**
  - Naming a limitation and then immediately excusing it in the same breath.
  - Restating a claim the reader just read.
  - Any sentence that could be deleted without losing information.
  - Putting location, "Hybrid," "Remote," or other tags in the "Re:" subject line.
  - Substituting the repo root or general portfolio page for a specific project link the user explicitly provided.
  - Appending a separate P.S. bullet list of links instead of embedding them in the body.
  - Including sign-in-required links unless explicitly requested.
- **Tenure guardrail:** Every "X years" claim must be traceable to a specific date range in the resume.
- **Link guardrail:** Every URL the user provides must appear as an inline, descriptive anchor in the body. No raw URLs, no P.S. link dump.