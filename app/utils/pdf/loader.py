import os

from pypdf import PdfReader
from dynaconf import settings

class PDFLoader:

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
                text = page.extract_text(extraction_mode="layout",  layout_mode_scale_weight=1.0)
                if text:
                    full_text += text
            return full_text