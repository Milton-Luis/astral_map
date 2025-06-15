from ctypes import alignment
from reportlab.platypus import Paragraph, Spacer, PageBreak, Image

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from dynaconf import settings
from datetime import datetime


class PDFCover:
    def __init__(self, styles):
        self.styles = styles
        self._settings = settings

    def build_cover(self):
        elements = []
        elements.append(Spacer(1, 2 * inch))

        elements.append(
            Paragraph(
                self._settings.PDF_COVER_TITLE,
                ParagraphStyle(
                    name=sum,
                    fontSize=self._settings.PDF_COVER_FONT_SIZE,
                    alignment=TA_CENTER,
                    spaceAfter=self._settings.PDF_COVER_SPACE_AFTER,
                ),
            )
        )

        elements.append(Paragraph(
            
            f"Autor: {self._settings.PDF_AUTHOR}<br/>Data: {datetime.now().strftime('%d/%m/%Y')}",
            ParagraphStyle(
                name="CoverMeta",
                fontSize=self._settings.TEXT_FONT_SIZE,
                spaceAfter=40
            )
        ))
        if hasattr(self._settings, "cover_logo"):
            elements.append(Image(settings.PDF.cover_logo, width=150, height=150))
            elements.append(Spacer(1, 20))

        elements.append(PageBreak())
        return elements
