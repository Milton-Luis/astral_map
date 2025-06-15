from app.extensions.pdf_utils import CreatePDF
from app.utils.pdf.loader import PDFLoader
from app.utils.pdf.reader import PDFFileReader
from app.utils.pdf.generate import PDFGenerator
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
    # Textos em ordem de estrutura
        initial_text = self._read_initial_text_pdf()  # explicação geral
        nakshatra_intro = self._read_nakshatra_base_text_pdf()  # sobre nakshatra
        selected_nakshatra = self._select_nakshatra_text_pdf()  # nakshatra pessoal

        # Mock de textos restantes (até ter os arquivos)
        ishta_intro = "Explicação sobre Ishtaphala e Kashtaphala"
        ishta_content = "Texto completo dos Ishtaphala e Kashtaphala"
        casa_intro = "Explicação sobre Casas"
        casa_content = "Texto completo das Casas"

        # Títulos para as seções principais (registradas no índice)
        titles = [
            "",  # título para bloco nakshatra
            "Ishtaphala e Kashtaphala",
            "Casas"
        ]

        # Textos: [explicação, nakshatra_intro, nakshatra_text, ishta_intro, ishta_text, casa_intro, casa_text]
        texts = [
            initial_text,
            nakshatra_intro,
            selected_nakshatra,
            ishta_intro,
            ishta_content,
            casa_intro,
            casa_content
        ]

        # Se quiser incluir imagens, coloque caminhos aqui (opcional)
        images = [
            settings.IMAGE_1_PATH,
            settings.IMAGE_2_PATH,
            settings.IMAGE_3_PATH,
            settings.IMAGE_4_PATH
        ]

        pdf_generator = PDFGenerator(titles, texts, images)
        return pdf_generator.create_pdf()




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
