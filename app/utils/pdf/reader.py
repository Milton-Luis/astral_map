from typing import List
from astral_map.app.utils.pdf.loader import PDFLoader


class PDFReader:
    def __init__(self, pdf_loader: PDFLoader):
        self._pdf_loader = pdf_loader
    def extract_text_by_title(self, filename: str, title: str, title_list: List[str]):
        full_text = self._pdf_loader.load_pdf_text(filename)

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