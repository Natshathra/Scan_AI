import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

import cv2
import numpy as np
from PIL import Image

def extract_text_from_image(image):
    img_array = np.array(image)
    gray_img = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray_img)
    return text
