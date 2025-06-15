from app.utils.pdf.styles import PDFStyle
from reportlab.platypus import PageBreak, Paragraph, Spacer


class PDFContent:
    def __init__(self, titles: str, texts: str, styles: PDFStyle):
        self._titles = titles
        self._texts = texts
        self._styles = styles

    def build_story(self):
        story = []

        for title, text in zip(self._titles, self._texts):
            if text.startswith(title):
                text = text[len(title) :].lstrip()

            story.append(Paragraph(title, self._styles.title_style()))
            paragraphs = text.strip().split("\n\n")

            for paragraph in paragraphs:
                story.append(
                    Paragraph(
                        paragraph.strip().replace("\n", " "), self._styles.text_style()
                    )
                )
                story.append(Spacer(1, 12))
            story.append(PageBreak())

        return story
