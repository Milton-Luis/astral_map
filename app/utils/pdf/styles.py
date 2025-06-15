from dynaconf import settings
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm


class PDFStyle:
    """
    PDFStyle provides utility methods to generate custom paragraph styles for PDF generation.

    Attributes:
        _styles (StyleSheet1): A collection of default styles from ReportLab's sample style sheet.

    Methods:
        title_style():
            Returns a ParagraphStyle for titles, based on Heading2, with custom font and spacing as defined in settings.

        text_style():
            Returns a ParagraphStyle for body text, justified alignment, custom font, leading, spacing, and first line indent as defined in settings.
    """
    def __init__(self):
        self._styles = getSampleStyleSheet()

    def title_style(self):
        style = ParagraphStyle(
            name="Header",
            parent=self._styles["Heading2"],
            fontName=settings.TITLE_FONT_NAME,
            fontSize=settings.TITLE_FONT_SIZE,
            spaceAfter=14,
        )
        return style

    def text_style(self):
        justified_style = ParagraphStyle(
            name="Justified",
            parent=self._styles["Normal"],
            alignment=TA_JUSTIFY,
            fontName=settings.TEXT_FONT_NAME,
            fontSize=settings.TEXT_FONT_SIZE,
            leading=14,
            spaceAfter=12,
            firstLineIndent=settings.FIRST_LETTER_INDENT_MM * mm,
        )
        return justified_style
