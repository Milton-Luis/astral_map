from reportlab.platypus import Paragraph, Spacer, PageBreak
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.lib.styles import ParagraphStyle
from dynaconf import settings

class PDFToc:
    def __init__(self):
        self._toc = TableOfContents()
        self._settings = settings
        self._toc.levelStyles = [
            ParagraphStyle(
                fontName = self._settings.TITLE_FONT_NAME,
                fontSize = self._settings.TEXT_FONT_SIZE,
                name="TOCHeading1",
                leftIndent=20,
                firstLineIndent=-20,
                spaceBefore=5
            )
        ]

    def build_toc(self):
        return [
            Paragraph(self._settings.PDF_INDEX_TITLE, ParagraphStyle(
                name="TOCTitle", fontSize=18, spaceAfter=20)), self._toc, PageBreak()]
    
    def get_toc(self):
        return self._toc

