import os
from typing import List

from pypdf import PdfReader


def open_file(resource_path: str, filename: str = ""):
    base_path = os.path.abspath(resource_path)
    file_path = os.path.join(base_path, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not Found: {file_path}")

    with open(file_path, "rb") as file:
        reader = PdfReader(file)
        full_text = ""
        for page in reader.pages:
            text = page.extract_text(extraction_mode="layout",  layout_mode_scale_weight=1.0)
            if text:
                full_text += text
        return full_text


def extract_text_by_title(pdf_path: str, filename: str, title: str, title_list: List[str]):
    full_text = open_file(pdf_path, filename)

    if title.upper() not in title_list:
        return f"Título '{title}' não encontrado na lista."

    initial_index = full_text.find(title.upper())
    if initial_index == -1:
        return f"Título '{title}' não encontrado no texto."

    endless_index = len(full_text)
    remaining_titles = title_list[title_list.index(title.upper()) + 1:]
    for next in remaining_titles:
        next_title = full_text.find(next, initial_index + 1)
        if next_title != -1:
            endless_index = next_title
            break

    return full_text[initial_index:endless_index].strip()




    """def gerar_pdf_em_memoria(titulos, textos):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50,
    )

    story = []
    styles = getSampleStyleSheet()

    justified_style = ParagraphStyle(
        name="Justificado",
        parent=styles["Normal"],
        alignment=TA_JUSTIFY,
        fontName="Helvetica",
        fontSize=11,
        leading=14,
        spaceAfter=12,
        firstLineIndent=10 * mm,
    )

    title_style = ParagraphStyle(
        name="Titulo",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        spaceAfter=14,
    )

    for titulo, texto in zip(titulos, textos):
        if texto.startswith(titulo):
            texto = texto[len(titulo) :].lstrip()
        story.append(Paragraph(titulo, title_style))

        # Separar por parágrafos (duas quebras de linha = novo parágrafo)
        paragrafos = texto.strip().split("\n\n")
        for paragrafo in paragrafos:
            story.append(
                Paragraph(paragrafo.strip().replace("\n", " "), justified_style)
            )
            story.append(Spacer(1, 12))  # Espaço entre parágrafos

        story.append(PageBreak())

    doc.build(story)
    buffer.seek(0)
    return buffer
 
 Keyword arguments:
 argument -- description
 Return: return_description
 """
 