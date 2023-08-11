import pytesseract
import os

class OCR:
    def __init__(self):
        self.path = r'C:\\Users\\athri\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
        pytesseract.pytesseract.tesseract_cmd = self.path

    def extract(self, filename):
        try:
            text = pytesseract.image_to_string(filename)
            return text
        except Exception as e:
            return str(e)
ocr=OCR()
text=ocr.extract("imagetotext/text1.png")
print(text)




