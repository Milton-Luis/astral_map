from typing import List

from app.utils.pdf.loader import PDFLoader


class PDFFileReader:
    """
    A class for extracting text sections from a PDF file based on section titles.
    Args:
        pdf_loader (PDFLoader): An instance responsible for loading PDF text.
    Methods:
        extract_text_by_title(filename: str, title: str, title_list: List[str]) -> str:
            Extracts and returns the text from the PDF file starting at the specified title up to the next title in the provided list.
            If the title is not found in the list or in the text, returns an appropriate message.
            Args:
                filename (str): The path to the PDF file.
                title (str): The title of the section to extract.
                title_list (List[str]): A list of all possible section titles in uppercase.
            Returns:
                str: The extracted text for the section, or an error message if the title is not found.
    """

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
        remaining_titles = title_list[title_list.index(title.upper()) + 1 :]

        for next in remaining_titles:
            next_title = full_text.find(next, initial_index + 1)
            if next_title != -1:
                endless_index = next_title
                break

        return full_text[initial_index:endless_index].strip()
