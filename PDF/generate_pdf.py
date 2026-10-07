import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
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
            self.drawString(54, 11 * 72 - 36, "AI-POWERED ADAPTIVE UEBA — PROJECT PRESENTATION & VIVA PREPARATION")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 11 * 72 - 42, 8.5 * 72 - 54, 11 * 72 - 42)
            
        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * 72 - 54, 36, footer_text)
        self.drawString(54, 36, "CONFIDENTIAL & PROPRIETARY — M.TECH DISSERTATION PREPARATION")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 8.5 * 72 - 54, 48)
        self.restoreState()

def build_pdf(filename="Adaptive_UEBA_Project_Presentation_Viva_Preparation.pdf"):
    pdf_path = os.path.join(os.path.dirname(__file__), filename)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    PRIMARY = colors.HexColor("#0F172A")    # Dark Slate
    SECONDARY = colors.HexColor("#1E3A8A")  # Deep Blue
    ACCENT = colors.HexColor("#2563EB")     # Royal Blue
    TEXT_DARK = colors.HexColor("#1E293B")  # Off-black
    BG_LIGHT = colors.HexColor("#F8FAFC")   # Soft Grey
    BORDER_COLOR = colors.HexColor("#E2E8F0")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=PRIMARY,
        spaceAfter=8
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=SECONDARY,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=SECONDARY,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=0
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=TEXT_DARK
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0F172A")
    )

    story = []

    # Title Block
    story.append(Paragraph("AI-Powered Adaptive UEBA for Insider Threat Detection", title_style))
    story.append(Paragraph("<b>Comprehensive Project Understanding, Presentation Guide & Viva Question Bank</b>", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceBefore=0, spaceAfter=15))

    # Meta Table
    meta_data = [
        [Paragraph("<b>Academic Context:</b> M.Tech in CSE", table_cell_style), Paragraph("<b>Student:</b> Mr. Chetan Shrikant Lokhande (25PCS009)", table_cell_style)],
        [Paragraph("<b>Institution:</b> D.K.T.E. Society's TEI, Ichalkaranji", table_cell_style), Paragraph("<b>Guide:</b> Prof. S. R. Patil", table_cell_style)],
        [Paragraph("<b>Affiliation:</b> Shivaji University, Kolhapur", table_cell_style), Paragraph("<b>Dataset:</b> CMU CERT Insider Threat Dataset r5.2", table_cell_style)],
        [Paragraph("<b>Registration:</b> July 2026", table_cell_style), Paragraph("<b>Expected Completion:</b> June 2027", table_cell_style)]
    ]
    t_meta = Table(meta_data, colWidths=[250, 254])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 15))

    # SECTION 1
    story.append(Paragraph("SECTION 1 — PROJECT IN ONE PAGE", h1_style))
    story.append(Paragraph("<b>1. Problem Statement:</b> Adaptive User and Entity Behavior Analytics (UEBA) systems dynamically adjust profiles to reflect changing user roles. However, this introduces a critical vulnerability: <i>slow-escalation baseline poisoning</i>. A patient insider escalating anomalous activity by ~5% per month causes an ungoverned model to quietly absorb the attack as normal, causing detection rates to drop from 94% down to 22%.", body_style))
    story.append(Paragraph("<b>2. Proposed Solution:</b> A 4-layer architecture combining 44 continuous behavioral features on CMU CERT r5.2, a 4-stage baseline update governance engine with peer-group anchors, hybrid risk fusion (XGBoost + SMOTE, SVM, Isolation Forest), exact TreeSHAP attributions, and an evidence-grounded Claude 3.5 Sonnet LLM chatbot.", body_style))
    story.append(Paragraph("<b>3. Research Contribution:</b> The 4-stage baseline governance engine. It mathematically separates legitimate role transfers from unilateral attack drift, sustaining a ~93% detection rate under 6-month poisoning attacks where ungoverned baselines fail.", body_style))
    story.append(Paragraph("<b>4. Key Experimental Results:</b>", body_style))
    
    res_summary = [
        [Paragraph("<b>Metric / Benchmark</b>", table_header_style), Paragraph("<b>Empirical Result</b>", table_header_style), Paragraph("<b>Operational Significance</b>", table_header_style)],
        [Paragraph("Model Fusion (E1)", table_cell_style), Paragraph("AUC 0.9782, F1 0.9412", table_cell_style), Paragraph("Outperforms SVM (0.8842) & XGBoost (0.9415)", table_cell_style)],
        [Paragraph("Full Test Scale (130k)", table_cell_style), Paragraph("Recall 99.78%, Precision 100%", table_cell_style), Paragraph("3,705 / 3,713 threats caught with 0 False Alarms", table_cell_style)],
        [Paragraph("Ungoverned Poisoning (E2)", table_cell_style), Paragraph("Detection drops 94% -> 22%", table_cell_style), Paragraph("Proves ungoverned baseline collapse", table_cell_style)],
        [Paragraph("Governed Defense (E3)", table_cell_style), Paragraph("Sustains ~93.0% Detection", table_cell_style), Paragraph("Suppresses 19 poisoned baseline updates", table_cell_style)],
        [Paragraph("Drift Disambiguation (E4)", table_cell_style), Paragraph("94.00% Acc, 4.00% FSR", table_cell_style), Paragraph("Distinguishes role changes from attacks", table_cell_style)],
        [Paragraph("LLM Faithfulness (E5)", table_cell_style), Paragraph("Score 0.9555 (FaithLens)", table_cell_style), Paragraph("Factuality 97.17%, zero hallucinated claims", table_cell_style)],
    ]
    t_res = Table(res_summary, colWidths=[120, 150, 234])
    t_res.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_res)
    story.append(Spacer(1, 10))

    # Timed Explanations
    story.append(Paragraph("<b>Explain Project in 30 Seconds:</b><br/><i>'My M.Tech project addresses slow-escalation baseline poisoning in User and Entity Behavior Analytics (UEBA). While dynamic baselines accommodate work changes, an insider can slowly escalate activity by 5% per month to train ungoverned models to ignore them. I developed a novel 4-stage baseline governance engine with peer-group anchors that prevents poisoning, maintaining a 93% detection rate on the CMU CERT dataset where ungoverned models collapse to 22%. Combined with a hybrid XGBoost-SVM-Isolation Forest risk fusion model and SHAP-grounded Claude LLM explanations scoring 0.9555 on FaithLens, the system delivers an end-to-end SOC command center.'</i>", body_style))
    story.append(Spacer(1, 10))

    # SECTION 2
    story.append(Paragraph("SECTION 2 — COMPLETE PROJECT UNDERSTANDING", h1_style))
    story.append(Paragraph("• <b>UEBA:</b> Analyzes multi-channel telemetry (logon, USB, email, file, HTTP) to establish normal behavioral profiles and flag threat deviations.", bullet_style))
    story.append(Paragraph("• <b>Insider Threat:</b> Malicious activity originating from authenticated entities with legitimate access privileges.", bullet_style))
    story.append(Paragraph("• <b>Why Perimeter Fails:</b> Firewalls and IDS defend external borders; insiders use authorized credentials inside trust boundaries.", bullet_style))
    story.append(Paragraph("• <b>Adaptive Baselines:</b> Automatically update user profiles over time to accommodate benign workflow shifts.", bullet_style))
    story.append(Paragraph("• <b>Slow-Escalation Poisoning:</b> Adversaries deliberately increment exfiltration by small deltas (e.g., +5%/month) so ungoverned sliding windows absorb the malicious trajectory as normal.", bullet_style))

    # SECTION 3
    story.append(Paragraph("SECTION 3 — RESEARCH GAP AND NOVELTY", h1_style))
    story.append(Paragraph("<b>Research Gap:</b> Prior literature on CMU CERT r5.2 (BRITD, MambaITD, Evidential Clustering) focuses purely on instantaneous classification metrics and statistical thresholding without defending against slow-rate baseline manipulation.", body_style))
    story.append(Paragraph("<b>Novelty & Contribution:</b> The 4-stage governance engine with role-matched peer anchors. It evaluates drift acceleration, peer divergence, and 7-day monotonic trends to gate updates, sustaining 93% detection fidelity.", body_style))

    # SECTION 4 & 5
    story.append(Paragraph("SECTION 4 — SYSTEM ARCHITECTURE & DATASET", h1_style))
    story.append(Paragraph("The system follows a 4-layer architecture: Data Layer (CERT r5.2 ingestion & 44 features), Intelligence Layer (Hybrid ML fusion & 4-stage governance), Backend Layer (Django REST, Celery async queues, Redis broker, PostgreSQL), and Presentation Layer (React 18 analyst dashboard).", body_style))
    story.append(Paragraph("<b>Dataset:</b> CMU CERT Insider Threat Dataset r5.2 containing 692,645 continuous daily feature vectors across 6 CSV log modalities (logon, device, email, file, http, psychometric), partitioned into an 80% train split (562,594 rows) and a 20% held-out test split (130,051 rows).", body_style))

    # SECTION 8 & 9
    story.append(Paragraph("SECTION 8 & 9 — ML MODELS & 4-STAGE GOVERNANCE", h1_style))
    story.append(Paragraph("<b>Risk Fusion Equation:</b>", h2_style))
    story.append(Paragraph("<b>RiskScore = (0.35 * P_xgb + 0.25 * S_IF + 0.20 * D_peer + 0.15 * D_user + 0.05 * D_drift) * 100</b>", code_style))
    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>4-Stage Governance Gates:</b>", h2_style))
    story.append(Paragraph("1. <i>Stage 1 (Drift Acceleration S_1):</i> Evaluates mean differential r_bar. Pass if S_1 < 0.50.<br/>2. <i>Stage 2 (Peer Divergence S_2):</i> Evaluates Delta_peer = max(0, D_user - D_peer). Pass if S_2 < 0.45.<br/>3. <i>Stage 3 (Monotonic Trend S_3):</i> Evaluates 7-day directional step ratio mu. Pass if S_3 < 0.75.<br/>4. <i>Stage 4 (Composite Gating S_drift):</i> S_drift = 0.35*S_1 + 0.40*S_2 + 0.25*S_3. If S_drift >= 0.60, update is SUPPRESSED and baseline is frozen.", body_style))

    # SECTION 16
    story.append(Paragraph("SECTION 16 — EXPERIMENTAL RESULTS", h1_style))
    story.append(Paragraph("In Experiment E2, an ungoverned baseline's detection rate collapsed from <b>94.0% to 22.0%</b> by Month 6 under 5%/month poisoning. In Experiment E3, our governed baseline sustained a <b>~93.0% detection rate</b> across all 6 months. In Experiment E4, drift classification achieved <b>94.00% accuracy</b> with only a <b>4.00% False Suppression Rate</b>. In Experiment E5, LLM explanations achieved an overall FaithLens score of <b>0.9555</b>.", body_style))

    # SECTION 20 & 23
    story.append(Paragraph("SECTION 20 & 23 — VIVA QUESTIONS & RAPID REVISION", h1_style))
    story.append(Paragraph("<b>Top Viva Question 1: How do you prevent data leakage?</b><br/><i>Answer: We enforce a strict chronological train/test split (80% train / 20% test). We never use random k-fold cross validation, which would cause future telemetry to leak into past training vectors.</i>", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Top Viva Question 2: How does the governance engine distinguish job promotions from attacks?</b><br/><i>Answer: Stage 2 checks peer divergence. In a promotion, the user's vector shifts toward their new role's peer centroid, keeping peer divergence low. In an attack, the user drifts unilaterally away from peers, triggering suppression.</i>", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Top Viva Question 3: How do you prevent LLM hallucinations?</b><br/><i>Answer: We build immutable JSON Evidence Objects containing TreeSHAP attributions and 7-day risk trajectories, passing them to Claude under strict prompt constraints. Tested on the FaithLens rubric, our summaries achieved 97.17% factuality and a 0.9555 overall score.</i>", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully generated: {pdf_path}")

if __name__ == "__main__":
    build_pdf()
