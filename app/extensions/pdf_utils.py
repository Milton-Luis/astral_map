import os
from io import BytesIO
from typing import List

from dynaconf import settings
from pypdf import PdfReader
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer


class CreatePDF:
    def __init__(self, titles:List[str], texts:List[str]):
        self.titles = titles
        self.texts = texts
        self.buffer = BytesIO()
        self.styles = getSampleStyleSheet()

    def create_pdf(self):
        story = []

        for title, text in zip(self.titles, self.texts):
            if text.startswith(title):
                text = text[len(title) :].lstrip()
            story.append(Paragraph(title, self.title_style()))
            paragraphs = text.strip().split("\n\n")
            for paragraph in paragraphs:
                story.append(
                    Paragraph(paragraph.strip().replace("\n", " "), self.text_style())
                )
                story.append(Spacer(1, 12))
            story.append(PageBreak())

        self.make_simple_doc_template().build(story)
        self.buffer.seek(0)
        return self.buffer

    def make_simple_doc_template(self):
        document = SimpleDocTemplate(
            self.buffer,
            pagesize=A4,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50,
            title=settings.PDF_TITLE,
            author="pessoa 1",
            creator="Astral Map System",
        )
        return document

    def title_style(self):
        style = ParagraphStyle(
            name="Header",
            parent=self.styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=14,
            spaceAfter=14,
            firstLineIndent=10 * mm,
        )
        return style

    def text_style(self):
        justified_style = ParagraphStyle(
            name="Justified",
            parent=self.styles["Normal"],
            alignment=TA_JUSTIFY,
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            spaceAfter=12,
            firstLineIndent=10 * mm,
        )
        return justified_style


class ReadPDF: ...


def open_pdf(resource_path: str, filename: str):
    base_path = os.path.abspath(resource_path)
    file_path = os.path.join(base_path, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not Found: {file_path}")

    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text(
                extraction_mode="layout", layout_mode_scale_weight=1.0
            )
            if text:
                full_text += text
        return full_text
