"""
Generates glossary_AI.pdf — a short English glossary of Artificial
Intelligence / Machine Learning terms. This is the source document
required by the assignment ("Take a glossary in english in pdf format
related to a specific context").
"""
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

GLOSSARY = [
    ("Artificial Intelligence", "The simulation of human intelligence processes by computer systems."),
    ("Machine Learning", "A subset of AI where systems learn patterns from data instead of explicit rules."),
    ("Deep Learning", "A branch of machine learning based on multi-layer artificial neural networks."),
    ("Neural Network", "A computing model of connected nodes loosely inspired by the human brain."),
    ("Dataset", "A structured collection of data used to train or evaluate a model."),
    ("Algorithm", "A defined sequence of steps used to solve a problem or perform a computation."),
    ("Model", "The trained mathematical representation that maps inputs to outputs."),
    ("Training", "The process of adjusting a model's parameters using data."),
    ("Prediction", "The output a trained model produces for new, unseen input."),
    ("Natural Language Processing", "The field of AI concerned with understanding and generating human language."),
    ("Computer Vision", "The field of AI that enables machines to interpret images and video."),
    ("Chatbot", "A software application that simulates human conversation."),
]

doc = SimpleDocTemplate("glossary_AI.pdf", pagesize=A4,
                         topMargin=0.9 * inch, bottomMargin=0.8 * inch,
                         leftMargin=0.8 * inch, rightMargin=0.8 * inch)
styles = getSampleStyleSheet()
title_style = ParagraphStyle("GTitle", parent=styles["Title"], fontSize=20, spaceAfter=4)
sub_style = ParagraphStyle("GSub", parent=styles["Normal"], fontSize=11, textColor=colors.grey, spaceAfter=18)
term_style = ParagraphStyle("Term", parent=styles["Normal"], fontSize=11, leading=14)
def_style = ParagraphStyle("Def", parent=styles["Normal"], fontSize=10, leading=13, textColor=colors.HexColor("#333333"))

story = [
    Paragraph("Glossary of Artificial Intelligence Terms", title_style),
    Paragraph("Context: Artificial Intelligence &amp; Machine Learning — English source glossary", sub_style),
]

data = [[Paragraph("<b>Term</b>", term_style), Paragraph("<b>Definition</b>", term_style)]]
for term, defn in GLOSSARY:
    data.append([Paragraph(term, term_style), Paragraph(defn, def_style)])

table = Table(data, colWidths=[1.8 * inch, 4.1 * inch], repeatRows=1)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1E2761")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F2F4FA")]),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
]))
story.append(table)

doc.build(story)
print("Wrote glossary_AI.pdf with", len(GLOSSARY), "terms")
