import sys
import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#4A5568"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 11 * 72 - 36, "RESEARCH-PAPER JUDGE CROSS-QUESTION BANK — ADAPTIVE UEBA")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)
            
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 54, 36, footer_text)
        self.drawString(54, 36, "CONFIDENTIAL & PROPRIETARY — M.TECH RESEARCH DEFENSE")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 8.5 * 72 - 54, 48)
        self.restoreState()

def md_to_reportlab_text(text):
    """Convert basic Markdown formatting (**bold**, *italic*, `code`, math) to ReportLab XML tags."""
    if not text:
        return ""
    # Clean up math wrappers $...$ or $$...$$
    text = re.sub(r'\$\$(.*?)\$\$', r'<b>\1</b>', text)
    text = re.sub(r'\$(.*?)\$', r'<i>\1</i>', text)
    # Bold **text**
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    # Italic *text*
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    # Inline code `text`
    text = re.sub(r'`(.*?)`', r'<font face="Courier">\1</font>', text)
    # Escape ampersands not in XML tags
    text = re.sub(r'&(?!amp;|lt;|gt;|quot;|#)', '&amp;', text)
    return text

def parse_markdown_file(md_path, styles):
    PRIMARY = colors.HexColor("#0F172A")
    SECONDARY = colors.HexColor("#1E3A8A")
    TEXT_DARK = colors.HexColor("#1E293B")
    BG_LIGHT = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#E2E8F0")

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    q_title_style = ParagraphStyle(
        'QuestionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12.5,
        textColor=SECONDARY,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=TEXT_DARK
    )

    story_elements = []

    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    in_code_block = False
    table_rows = []

    for line in lines:
        raw_line = line
        line = line.strip()

        # Handle Code Blocks
        if line.startswith("```"):
            in_code_block = not in_code_block
            if not in_code_block and table_rows:
                # Flush accumulated code/ascii table
                if len(table_rows) > 0:
                    formatted_lines = "<br/>".join([md_to_reportlab_text(r) for r in table_rows])
                    p_code = Paragraph(f"<font face='Courier' size=7>{formatted_lines}</font>", body_style)
                    t_box = Table([[p_code]], colWidths=[504])
                    t_box.setStyle(TableStyle([
                        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
                        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                        ('PADDING', (0,0), (-1,-1), 4),
                    ]))
                    story_elements.append(t_box)
                    story_elements.append(Spacer(1, 4))
                table_rows = []
            continue

        if in_code_block:
            table_rows.append(raw_line.rstrip())
            continue

        if not line or line == "---":
            continue

        # Category Headings
        if line.startswith("## Category"):
            heading_text = line.lstrip("#").strip()
            story_elements.append(Paragraph(md_to_reportlab_text(heading_text), h1_style))
            story_elements.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=2, spaceAfter=6))
            continue

        # Master Mapping / Table Headings
        if line.startswith("## MASTER MAPPING"):
            heading_text = line.lstrip("#").strip()
            story_elements.append(Paragraph(md_to_reportlab_text(heading_text), h1_style))
            story_elements.append(HRFlowable(width="100%", thickness=1, color=PRIMARY, spaceBefore=2, spaceAfter=6))
            continue

        # Question Titles (#### Q...)
        if line.startswith("#### Q"):
            q_text = line.lstrip("#").strip()
            story_elements.append(Paragraph(md_to_reportlab_text(q_text), q_title_style))
            continue

        # Markdown Table rows
        if line.startswith("|") and line.endswith("|"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2:
                # Ignore table alignment separator lines like |---|---|
                if set("".join(parts)) <= set("-: |"):
                    continue
                table_rows.append(parts)
            continue
        elif table_rows:
            # End of table block reached, process accumulated table
            if len(table_rows) > 0:
                col_count = len(table_rows[0])
                # Calculate column widths
                if col_count == 3:
                    widths = [30, 120, 354]
                elif col_count == 2:
                    widths = [150, 354]
                else:
                    widths = [504 / col_count] * col_count

                table_data = []
                for idx, row in enumerate(table_rows):
                    row_data = []
                    style_to_use = table_header_style if idx == 0 else table_cell_style
                    for cell in row:
                        row_data.append(Paragraph(md_to_reportlab_text(cell), style_to_use))
                    table_data.append(row_data)

                t = Table(table_data, colWidths=widths)
                t.setStyle(TableStyle([
                    ('BACKGROUND', (0,0), (-1,0), PRIMARY),
                    ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                    ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
                    ('PADDING', (0,0), (-1,-1), 3),
                ]))
                story_elements.append(t)
                story_elements.append(Spacer(1, 6))
            table_rows = []

        # Bullet points / Q&A details
        if line.startswith("* **") or line.startswith("- **") or line.startswith("* ") or line.startswith("- "):
            bullet_text = line.lstrip("*").lstrip("-").strip()
            story_elements.append(Paragraph(md_to_reportlab_text(bullet_text), body_style))
            continue

        # Standard Paragraphs
        if not line.startswith("#") and not line.startswith("["):
            story_elements.append(Paragraph(md_to_reportlab_text(line), body_style))

    return story_elements

def build_pdf(filename="Adaptive_UEBA_Judge_Cross_Questions_Bank.pdf"):
    dir_path = os.path.dirname(__file__)
    pdf_path = os.path.join(dir_path, filename)
    md_path = os.path.join(dir_path, "Adaptive_UEBA_Judge_Cross_Questions_Bank.md")

    if not os.path.exists(md_path):
        print(f"Error: Could not find {md_path}")
        return

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    PRIMARY = colors.HexColor("#0F172A")
    SECONDARY = colors.HexColor("#1E3A8A")
    ACCENT = colors.HexColor("#2563EB")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=PRIMARY,
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=SECONDARY,
        spaceAfter=10
    )

    story = []

    # Title Block
    story.append(Paragraph("AI-Powered Adaptive UEBA for Insider Threat Detection", title_style))
    story.append(Paragraph("<b>Complete Research-Paper Judge Cross-Question Bank (All 430 Questions)</b>", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceBefore=0, spaceAfter=10))

    # Dynamically parse all 430 questions from the markdown file!
    md_elements = parse_markdown_file(md_path, styles)
    story.extend(md_elements)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated containing ALL 430 Q&As: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
