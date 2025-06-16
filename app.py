import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import pytesseract
from PIL import Image
import os
import tempfile
from utils.ocr import extract_text_from_image
from utils.file_utils import convert_to_pdf, convert_to_excel
import base64
import cv2
import av

st.set_page_config(page_title="ScanAI - Document OCR", layout="wide")
st.markdown("<style>" + open('./styles/style.css').read() + "</style>", unsafe_allow_html=True)

st.title("📄 ScanAI - Smart Document Scanner")
st.markdown("""
<p style='color: #2c3e50;'>Upload one or more scanned documents or use your camera to capture them. ScanAI will extract and highlight the content, and let you download it in your preferred format.</p>
""", unsafe_allow_html=True)

# Upload multiple files
uploaded_files = st.file_uploader("📤 Upload Scanned Documents (Images/PDFs)", accept_multiple_files=True, type=["png", "jpg", "jpeg", "pdf"])

extracted_texts = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        with st.spinner(f"Processing {uploaded_file.name}..."):
            img = Image.open(uploaded_file)
            text = extract_text_from_image(img)
            extracted_texts.append((uploaded_file.name, text))

    st.markdown("---")
    st.subheader("📜 Extracted Text")
    for i, (filename, text) in enumerate(extracted_texts):
        st.markdown(f"<h4 style='color:#1abc9c'>📄 {filename}</h4>", unsafe_allow_html=True)
        st.code(text, language='markdown')

    all_text = "\n\n".join([text for _, text in extracted_texts])

    st.download_button("⬇️ Download as Text", all_text, file_name="extracted_text.txt")
    pdf_data = convert_to_pdf(all_text)
    st.download_button("⬇️ Download as PDF", pdf_data, file_name="extracted_text.pdf")
    excel_data = convert_to_excel(extracted_texts)
    st.download_button("⬇️ Download as Excel", excel_data, file_name="extracted_text.xlsx")

# Camera Integration
st.markdown("---")
st.subheader("📷 Live Camera Scanner")

class CameraProcessor(VideoTransformerBase):
    def transform(self, frame):
        image = frame.to_ndarray(format="bgr24")
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

camera_placeholder = st.empty()
camera_result = webrtc_streamer(key="camera", video_transformer_factory=CameraProcessor)

st.markdown("""
<small style='color:gray;'>You can take a screenshot from your mobile or laptop while using the live camera to capture documents.</small>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align:center;color:#999'>Built with ❤️ using Streamlit, OCR, and AI</p>", unsafe_allow_html=True)
