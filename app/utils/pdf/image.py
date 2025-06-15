from reportlab.platypus import Image, Spacer
from reportlab.lib.units import inch


class PDFImage:
    def __init__(self, image_path: list[str]):
        self._images = image_path

    def build_images(self):
        images = []
        for image_path in self._images:
            images.append(Image(image_path, width=7 * inch, height=10 * inch))
            images.append(Spacer(1, 12))
        return images
