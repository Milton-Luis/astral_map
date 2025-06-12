from app.extensions.pdf_utils import CreatePDF
from app.utils.pdf.loader import PDFLoader
from app.utils.pdf.reader import PDFFileReader
from dynaconf import settings


class Nakshatra:
    nakshatras = [
        "ASHVINI",
        "BHARANI",
        "KRITTIKA",
        "ROHINI",
        "MRIGASHIRA",
        "ARDRA",
        "PUNARVASU",
        "PUSHYA",
        "ASHLESHA",
        "MAGHA",
        "PURVA PHALGUNI",
        "UTTARA PHALGUNI",
        "HASTA",
        "CHITRA",
        "SVATI",
        "VISHAKHA",
        "ANURADHA",
        "JYESHTHA",
        "MULA",
        "PURVA ASHADHA",
        "UTTARA ASHADHA",
        "SHRAVANA",
        "DHANISHTA",
        "SHATABHISHA",
        "PURVA BHADRAPADA",
        "UTTARA BHADRAPADA",
        "REVATI",
    ]

    pdf_loader = PDFLoader()
    pdf_reader = PDFFileReader(pdf_loader)

    def __init__(self, lord):
        self._lord = lord

    def create_nakshatras_complete_text(self):
        texts = [
            self._read_capa_pdf(),
            self._read_initial_text_pdf(),
            self._read_nakshatra_base_text_pdf(),
            self._select_nakshatra_text_pdf(),
        ]
        titles = ["", "Sobre o mapa", "NAKSHATRA LUNAR", self._lord]

        pdf_buffer = CreatePDF(titles, texts)

        return pdf_buffer.create_pdf()

    def _read_nakshatra_base_text_pdf(self):
        return self.pdf_loader.load_pdf_text(settings.NAKSHATRA_BASE_TEXT)

    def _read_initial_text_pdf(self):
        return self.pdf_loader.load_pdf_text(settings.VEDIC_ASTROLOGY_BASE_TEXT)

    def _read_capa_pdf(self):
        return self.pdf_loader.load_pdf_text(settings.CAPA_CONTENT)

    def _select_nakshatra_text_pdf(self):
        if self._lord in self.nakshatras:
            extracted_text = self.pdf_reader.extract_text_by_title(
                filename=settings.NAKSHATRA_CONTENT,
                title=self._lord,
                title_list=self.nakshatras,
            )
            return extracted_text
        else:
            return "Não encontrado"
