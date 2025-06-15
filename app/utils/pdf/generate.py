from io import BytesIO
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from app.utils.pdf.content import PDFContent
from app.utils.pdf.styles import PDFStyle
from app.utils.pdf.toc import PDFToc
from app.utils.pdf.image import PDFImage
from app.utils.pdf.cover import PDFCover
from reportlab.platypus import Paragraph
from dynaconf import settings

class PDFGenerator:
    def __init__(self, titles, texts, images=None):
        self._buffer = BytesIO()
        self._pdf_styles = PDFStyle()
        self._pdf_cover = PDFCover(self._pdf_styles)
        self._pdf_toc = PDFToc()
        self._images = images or []

        # Texto separado por blocos
        self.explanation_text = texts[0]
        self.nakshatra_intro = texts[1]
        self.nakshatra_text = texts[2]
        self.ishtaphala_intro = texts[3]
        self.ishtaphala_text = texts[4]
        self.casa_intro = texts[5]
        self.casa_text = texts[6]

        self.nakshatra_title = titles[0]
        self.ishtaphala_title = titles[1]
        self.casa_title = titles[2]

    def create_pdf(self):
        document = SimpleDocTemplate(
            self._buffer,
            pagesize=A4,
            rightMargin=50,
            leftMargin=50,
            topMargin=50,
            bottomMargin=50,
            title=settings.PDF_TITLE,
            author=settings.PDF_AUTHOR,
            creator=settings.PDF_SYSTEM_CREATOR,
        )

        story = []

        # 1. Capa
        story += self._pdf_cover.build_cover()

        # 2. Imagem 1
        story += PDFImage([self._images[0]]).build_images()

        # 3. Explicação inicial
        story += self._build_paragraph_block("Sobre o mapa astral védico", self.explanation_text)

        # 4. Imagem 2
        story += PDFImage([self._images[1]]).build_images()

        # 5. Índice (gerado automaticamente)
        story += self._pdf_toc.build_toc()

        # 6. Texto sobre Nakshatra (introdução)
        story += self._build_paragraph_block("Nakshatras", self.nakshatra_intro)

        # 7. Texto dos Nakshatras (com título registrado no TOC)
        story += self._build_paragraph_block(self.nakshatra_title, self.nakshatra_text, toc_level=0)

        # 8. Imagem 3
        story += PDFImage([self._images[2]]).build_images()

        # 9. Texto sobre Ishtaphala e Kashtaphala
        story += self._build_paragraph_block("Ishtaphala e Kashtaphala", self.ishtaphala_intro)

        # 10. Texto dos Ishtaphala e Kashtaphala
        story += self._build_paragraph_block(self.ishtaphala_title, self.ishtaphala_text, toc_level=0)

        # 11. Imagem 4
        story += PDFImage([self._images[3]]).build_images()

        # 12. Texto sobre Casas
        story += self._build_paragraph_block("Casas", self.casa_intro)

        # 13. Texto das Casas
        story += self._build_paragraph_block(self.casa_title, self.casa_text, toc_level=0)

        # Build PDF with TOC entries captured
        document.build(story, onFirstPage=self._register_toc, onLaterPages=self._register_toc)
        self._buffer.seek(0)
        return self._buffer

    def _register_toc(self, canvas, doc):
        def capture_toc_entry(flowable):
            if isinstance(flowable, Paragraph) and flowable.style.name == "Header":
                self._pdf_toc.get_toc().notify('TOCEntry', (0, flowable.getPlainText(), doc.page))

        doc.afterFlowable = capture_toc_entry

    def _build_paragraph_block(self, title, text, toc_level=None):
        from reportlab.platypus import Paragraph, Spacer, PageBreak
        story = []

        # Título com estilo
        paragraph = Paragraph(title, self._pdf_styles.title_style())
        story.append(paragraph)

        if toc_level is not None:
            self._pdf_toc.get_toc().notify('TOCEntry', (toc_level, title, None))

        # Texto formatado
        for paragraph in text.strip().split("\n\n"):
            story.append(Paragraph(paragraph.strip().replace("\n", " "), self._pdf_styles.text_style()))
            story.append(Spacer(1, 12))

        story.append(PageBreak())
        return story
