from dynaconf import settings
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm


class PDFStyle:
    def __init__(self):
        self._styles = getSampleStyleSheet()

    def title_style(self):
        style = ParagraphStyle(
            name="Header",
            parent=self.styles["Heading2"],
            fontName=settings.PDF.styles.TITLE_FONT_NAME,
            fontSize=settings.PDF.styles.TITLE_FONT_SIZE,
            spaceAfter=14,
        )
        return style

    def text_style(self):
        justified_style = ParagraphStyle(
            name="Justified",
            parent=self.styles["Normal"],
            alignment=TA_JUSTIFY,
            fontName=settings.PDF.styles.TEXT_FONT_NAME,
            fontSize=settings.PDF.styles.TEXT_FONT_SIZE,
            leading=14,
            spaceAfter=12,
            firstLineIndent=settings.PDF.styles.FIRST_LETTER_INDENT_MM * mm,
        )
        return justified_style
