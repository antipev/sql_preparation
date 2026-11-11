from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.shared import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

def add_hyperlink(paragraph, text, url, color="0563C1", underline=True):
    """Add a clickable hyperlink to a paragraph."""
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement('w:hyperlink')
    hyperlink.set(qn('r:id'), r_id)
    new_run = OxmlElement('w:r')
    rPr = OxmlElement('w:rPr')
    if color:
        c = OxmlElement('w:color')
        c.set(qn('w:val'), color)
        rPr.append(c)
    if underline:
        u = OxmlElement('w:u')
        u.set(qn('w:val'), 'single')
        rPr.append(u)
    new_run.append(rPr)
    t = OxmlElement('w:t')
    t.text = text
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)

def add_paragraph_with_links(doc, segments, style=None):
    """segments: list of tuples (text, url_or_None)"""
    p = doc.add_paragraph(style=style)
    for text, url in segments:
        if url:
            add_hyperlink(p, text, url)
        else:
            p.add_run(text)
    return p

doc = Document()

# Page 1: Cover Letter
section = doc.sections[0]
section.top_margin = Inches(1)
section.bottom_margin = Inches(1)
section.left_margin = Inches(1)
section.right_margin = Inches(1)

style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

# Header
header = doc.add_paragraph()
run = header.add_run("MAKSIM ANTIPEV")
run.bold = True
run.font.size = Pt(14)

contact = doc.add_paragraph()
contact.add_run("Winnipeg, MB | 204-396-0983 | maxantipev@gmail.com | ")
add_hyperlink(contact, "linkedin.com/in/maksimantipev", "https://www.linkedin.com/in/maksimantipev")
contact.add_run(" | ")
add_hyperlink(contact, "antipev.github.io/analytics-engineering", "https://antipev.github.io/analytics-engineering")

# Horizontal rule
hr = doc.add_paragraph()
pPr = hr._p.get_or_add_pPr()
pBdr = OxmlElement('w:pBdr')
bottom = OxmlElement('w:bottom')
bottom.set(qn('w:val'), 'single')
bottom.set(qn('w:sz'), '6')
bottom.set(qn('w:space'), '1')
bottom.set(qn('w:color'), '000000')
pBdr.append(bottom)
pPr.append(pBdr)

doc.add_paragraph("November 5, 2026")

to_line = doc.add_paragraph()
to_line.add_run("To: ").bold = True
to_line.add_run("Kavindu Narathota, Technical Product Leader, Data & Platform Strategy")

company_line = doc.add_paragraph()
company_line.add_run("Company: ").bold = True
company_line.add_run("Jobber")

re_line = doc.add_paragraph()
re_line.add_run("Re: ").bold = True
re_line.add_run("Senior Business Intelligence Engineer")

doc.add_paragraph("Dear Kavindu and the Jobber Hiring Team,")

doc.add_paragraph(
    "I'm based in Winnipeg, and I know this role is posted as hybrid across Toronto, Edmonton, and Vancouver. "
    "I'm reaching out anyway because the work your BI team is doing — governed semantic layers, scalable data models, "
    "and a trusted self-serve analytics environment — is exactly what I've spent the last six years building at SkipTheDishes. "
    "Jobber already has remote data engineering roles, so I'm confident the right conversation here is about impact, not postal codes."
)

add_paragraph_with_links(doc, [
    ("Your team is responsible for \"building core data models, governed semantic layers, and data pipelines necessary for enterprise-level reporting.\" "
     "That's been my daily focus. I deployed a Looker semantic layer for the Customer Service domain in two months using Unified Star Schema modeling, "
     "resolving fan-out and chasm-trap issues that had been blocking consistent metrics. I also spearheaded department-wide dbt layering standards and built "
     "Claude Code AI agent skills to keep SQL scalable and trustworthy — the same governance-first mindset your team needs. A working example of my SQL and "
     "semantic-modeling work is here: ", None),
    ("Project 1", "https://github.com/antipev/sql_preparation/blob/main/Project_Portfolio/Project%201/Project_1.md"),
    (", with the full stack documented in my ", None),
    ("project overview", "https://github.com/antipev/analytics-engineering/blob/main/PROJECT_OVERVIEW.md"),
    (".", None),
])

add_paragraph_with_links(doc, [
    ("When you ask for \"expert-level SQL\" and \"data pipelines using DBT,\" I bring both plus a track record of measurable outcomes. "
     "At Skip, I managed the transition from manual contact-volume forecasting to a bi-directional ML pipeline that improved forecast precision by 5% "
     "and reduced manual execution by 50%. I also built 18+ high-integrity datasets and 30+ core KPIs for Customer Services, achieving 80%+ adoption — "
     "not because the dashboards were pretty, but because I listened to stakeholders and translated their needs into semantic models. "
     "You can see the live architecture in action here: ", None),
    ("Dagster UI", "https://analytics-dagster-bolcwt6srq-nn.a.run.app/runs"),
    (", ", None),
    ("dbt docs", "https://analytics-dagster-bolcwt6srq-nn.a.run.app/dbt-docs/"),
    (", and the ", None),
    ("Malloy semantic layer", "https://malloy-publisher-mcp-bolcwt6srq-nn.a.run.app"),
    (".", None),
])

doc.add_paragraph(
    "My Plum profile reflects this balance: top talents in Innovation (abstract problem-solving, flexible thinking), "
    "Embracing Diversity (adapting to different people), and Execution (accuracy and follow-through). "
    "I'm also described as \"humble, considerate, cooperative, and analytical\" — qualities that map well to Jobber's culture of "
    "\"transparency, inclusivity, collaboration, and innovation.\""
)

doc.add_paragraph(
    "If a distributed arrangement works for this role the way it does for your data engineering team, I'd welcome the chance to talk. "
    "If an onsite cadence is essential, I'm also open to discussing a practical rhythm that keeps me connected to the team. "
    "Thank you for your time and consideration."
)

doc.add_paragraph("Sincerely,")
doc.add_paragraph()
sig = doc.add_paragraph()
sig.add_run("Maksim Antipev").bold = True

# Page break for Plum Profile
doc.add_page_break()

# Placeholder for Plum Profile
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("[INSERT PLUM PROFILE HERE]").italic = True
doc.add_paragraph("Paste your Plum Profile PDF pages below this line (as images or by printing the PDF to this page).")

# Save
doc.save("Maksim_Antipev_Jobber_Cover_Letter.docx")
print("Saved: Maksim_Antipev_Jobber_Cover_Letter.docx")