"""Generate the Jobber Senior Business Intelligence Engineer cover letter (.docx).

Letter body lives in LETTER (a list of paragraphs) so the text and the Word
document can never drift apart. Each paragraph is a list of (text, url) tuples:
url=None renders plain text, otherwise the segment becomes an inline hyperlink.
"""

from docx import Document
from docx.shared import Pt, Inches
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT

OUTPUT = "Maksim_Antipev_Jobber_Cover_Letter.docx"

# --- Portfolio links (validated against the repo / LinkedIn assets file) ---
PROJECT_1 = "https://github.com/antipev/sql_preparation/blob/main/Project_Portfolio/Project%201/Project_1.md"
PROJECT_OVERVIEW = "https://github.com/antipev/analytics-engineering/blob/main/PROJECT_OVERVIEW.md"
DAGSTER_UI = "https://analytics-dagster-bolcwt6srq-nn.a.run.app/runs"
DBT_DOCS = "https://analytics-dagster-bolcwt6srq-nn.a.run.app/dbt-docs/"
MALLOY = "https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app"
LINKEDIN = "https://www.linkedin.com/in/maksimantipev"
PORTFOLIO = "https://antipev.github.io/analytics-engineering"

CONTACT = [
    ("Winnipeg, MB | 204-396-0983 | maxantipev@gmail.com | ", None),
    ("linkedin.com/in/maksimantipev", LINKEDIN),
    (" | ", None),
    ("antipev.github.io/analytics-engineering", PORTFOLIO),
]

LETTER = [
    # 1. Location + hook (text as written in CV.md).
    [
        ("I'm based in Winnipeg, and I know this role is posted as hybrid across Toronto, Edmonton, and Vancouver. "
         "I'm reaching out anyway because the work your BI team is doing — governed semantic layers, scalable data "
         "models, and a trusted self-serve analytics environment — is exactly what I've spent the last six years "
         "building at SkipTheDishes. Jobber already has remote data engineering roles, so I'm confident the right "
         "conversation here is about impact, not postal codes.", None),
    ],
    # 2. Team mandate quote + semantic layer proof.
    [
        ("Your team is responsible for \"building core data models, governed semantic layers, and data pipelines "
         "necessary for enterprise-level reporting.\" That's been my daily focus. I deployed a Looker semantic layer "
         "for the Customer Service domain in two months using Unified Star Schema modeling, resolving fan-out and "
         "chasm-trap issues that had been blocking consistent metrics. I also spearheaded department-wide dbt layering "
         "standards and built Claude Code AI agent skills to keep SQL scalable and trustworthy — the same "
         "governance-first mindset your team needs. A working example of my SQL and semantic-modeling work is here: ", None),
        ("Project 1", PROJECT_1),
        (", with the full stack documented in my ", None),
        ("project overview", PROJECT_OVERVIEW),
        (".", None),
    ],
    # 3. Expert SQL + dbt pipelines + measurable outcomes + live demo links.
    [
        ("When you ask for \"expert-level SQL\" and \"data pipelines using DBT,\" I bring both plus a track record of "
         "measurable outcomes. At Skip, I managed the transition from manual contact-volume forecasting to a "
         "bi-directional ML pipeline that improved forecast precision by 5% and reduced manual execution by 50%. I also "
         "built 18+ high-integrity datasets and 30+ core KPIs for Customer Services, achieving 80%+ adoption — not "
         "because the dashboards were pretty, but because I listened to stakeholders and translated their needs into "
         "semantic models. You can see the live architecture in action here: ", None),
        ("Dagster UI", DAGSTER_UI),
        (", ", None),
        ("dbt docs", DBT_DOCS),
        (", and the ", None),
        ("Malloy semantic layer", MALLOY),
        (".", None),
    ],
    # 4. Plum profile + culture fit.
    [
        ("My Plum profile reflects this balance: top talents in Innovation (abstract problem-solving, flexible "
         "thinking), Embracing Diversity (adapting to different people), and Execution (accuracy and follow-through). "
         "I'm also described as \"humble, considerate, cooperative, and analytical\" — qualities that map well to "
         "Jobber's culture of \"transparency, inclusivity, collaboration, and innovation.\"", None),
    ],
    # 5. Close.
    [
        ("If a distributed arrangement works for this role the way it does for your data engineering team, I'd welcome "
         "the chance to talk. If an onsite cadence is essential, I'm also open to discussing a practical rhythm that "
         "keeps me connected to the team. Thank you for your time and consideration.", None),
    ],
]


def add_hyperlink(paragraph, text, url, color="0563C1", underline=True):
    """Add a clickable hyperlink to a paragraph."""
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    if color:
        c = OxmlElement("w:color")
        c.set(qn("w:val"), color)
        rPr.append(c)
    if underline:
        u = OxmlElement("w:u")
        u.set(qn("w:val"), "single")
        rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def add_paragraph_with_links(doc, segments, space_after=6):
    """segments: list of (text, url_or_None)."""
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    for text, url in segments:
        if url:
            add_hyperlink(p, text, url)
        else:
            p.add_run(text)
    return p


def add_horizontal_rule(doc):
    hr = doc.add_paragraph()
    pPr = hr._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    pBdr.append(bottom)
    pPr.append(pBdr)


doc = Document()

section = doc.sections[0]
section.top_margin = Inches(0.9)
section.bottom_margin = Inches(0.9)
section.left_margin = Inches(1)
section.right_margin = Inches(1)

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)
style.paragraph_format.line_spacing = 1.0

# --- Header ---
header = doc.add_paragraph()
header.paragraph_format.space_after = Pt(2)
run = header.add_run("MAKSIM ANTIPEV")
run.bold = True
run.font.size = Pt(14)

add_paragraph_with_links(doc, CONTACT, space_after=6)
add_horizontal_rule(doc)

# --- Date / addressee block ---
doc.add_paragraph("November 5, 2026").paragraph_format.space_after = Pt(8)

to_line = doc.add_paragraph()
to_line.paragraph_format.space_after = Pt(0)
to_line.add_run("To: ").bold = True
to_line.add_run("Kavindu Narathota, Technical Product Leader, Data & Platform Strategy")

company_line = doc.add_paragraph()
company_line.paragraph_format.space_after = Pt(0)
company_line.add_run("Company: ").bold = True
company_line.add_run("Jobber")

re_line = doc.add_paragraph()
re_line.paragraph_format.space_after = Pt(10)
re_line.add_run("Re: ").bold = True
re_line.add_run("Senior Business Intelligence Engineer")

doc.add_paragraph("Dear Kavindu and the Jobber Hiring Team,").paragraph_format.space_after = Pt(8)

# --- Body ---
for paragraph_segments in LETTER:
    add_paragraph_with_links(doc, paragraph_segments)

# --- Signature ---
close = doc.add_paragraph()
close.paragraph_format.space_before = Pt(4)
close.add_run("Sincerely,")
doc.add_paragraph()
sig = doc.add_paragraph()
sig.add_run("Maksim Antipev").bold = True

# --- Page 2: Plum Profile ---
doc.add_page_break()
placeholder = doc.add_paragraph()
placeholder.alignment = WD_ALIGN_PARAGRAPH.CENTER
placeholder.add_run("[INSERT PLUM PROFILE HERE]").italic = True
doc.add_paragraph("Paste your Plum Profile PDF pages below this line (as images or by printing the PDF to this page).")

doc.save(OUTPUT)
print("Saved:", OUTPUT)
