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
import pytesseract
import cv2
import numpy as np

def extract_text_from_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to clean the image
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Apply noise removal
    processed_img = cv2.medianBlur(thresh, 3)

    # Extract text
    text = pytesseract.image_to_string(processed_img, lang='eng')
    import cv2
import numpy as np
from PIL import Image
import easyocr

def extract_text_from_image(uploaded_img):
    if uploaded_img is None:
        return "No image uploaded."

    try:
        # Read image using PIL then convert to OpenCV format
        image = Image.open(uploaded_img)
        image = image.convert("RGB")
        open_cv_image = np.array(image)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
        
        reader = easyocr.Reader(['en'])
        result = reader.readtext(open_cv_image, detail=0)

        return "\n".join(result)

    except Exception as e:
        return f"Error processing image: {e}"


    return text
