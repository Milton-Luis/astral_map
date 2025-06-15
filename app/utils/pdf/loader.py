import os

from dynaconf import settings
from pypdf import PdfReader


class PDFLoader:
    """
    PDFLoader is a utility class for loading and extracting text from PDF files.

    Attributes:
        _file_path (str): The base directory path where PDF resources are stored.

    Methods:
        __init__():
            Initializes the PDFLoader instance and sets the resource path from settings.

        load_pdf_text(filename: str) -> str:
            Loads and extracts text from the specified PDF file.

            Args:
                filename (str): The name of the PDF file to load.

            Returns:
                str: The extracted text content from the PDF file.

            Raises:
                FileNotFoundError: If the specified PDF file does not exist.
    """

    def __init__(self):
        self._file_path = settings.RESOURCES_PATH

    def load_pdf_text(self, filename: str):
        base_path = os.path.abspath(self._file_path)
        file_path = os.path.join(base_path, filename)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not Found: {file_path}")

        with open(file_path, "rb") as file:
            reader = PdfReader(file)
            full_text = ""
            for page in reader.pages:
                text = page.extract_text(
                    extraction_mode="layout", layout_mode_scale_weight=1.0
                )
                if text:
                    full_text += text
            return full_text
