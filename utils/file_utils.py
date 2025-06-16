from io import BytesIO
from reportlab.pdfgen import canvas
import openpyxl

def convert_to_pdf(text: str):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)
    for i, line in enumerate(text.splitlines(), start=1):
        c.drawString(30, 800 - 15*i, line)
    c.save()
    buffer.seek(0)
    return buffer

def convert_to_excel(text_list):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Filename", "Extracted Text"])
    for name, text in text_list:
        ws.append([name, text])
    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer
