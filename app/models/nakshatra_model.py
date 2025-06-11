from app.extensions.pdf_utils import CreatePDF
from astral_map.app.utils.helpers.utils import extract_text_by_title, open_file
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

    def __init__(self, lord):
        self._lord = lord
        self._file_path = settings.RESOURCES_PATH

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
        reader = open_file(self._file_path, settings.NAKSHATRA_BASE_TEXT)
        return reader

    def _read_initial_text_pdf(self):
        reader = open_file(
            self._file_path, settings.VEDIC_ASTROLOGY_BASE_TEXT
        )
        return reader

    def _read_capa_pdf(self):
        reader = open_file(self._file_path, settings.CAPA_CONTENT)
        return reader

    def _select_nakshatra_text_pdf(self):
        if self._lord in self.nakshatras:
            extracted_text = extract_text_by_title(
                pdf_path=self._file_path,
                filename=settings.NAKSHATRA_CONTENT,
                title=self._lord,
                title_list=self.nakshatras,
            )
            return extracted_text
        else:
            return "Não encontrado"
