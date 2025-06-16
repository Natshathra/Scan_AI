import pytesseract
from PIL import Image
import cv2

# 👇 Add this line to explicitly set the path to tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extract_text_from_image(img: Image.Image) -> str:
    gray_img = img.convert('L')
    return pytesseract.image_to_string(gray_img)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
