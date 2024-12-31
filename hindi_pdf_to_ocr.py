PIL
# pip install pdf2image
# pip install PIL


import pytesseract
from pdf2image import convert_from_path
from PIL import Image

def extract_text_from_pdf(pdf_path):
    """Convert PDF pages to images and extract Hindi text using OCR."""
    pages = convert_from_path(pdf_path, 300)  # 300 DPI for better accuracy
    full_text = ""

    for page_number, page in enumerate(pages, start=1):
        # Extract text using Tesseract with Hindi language support
        text = pytesseract.image_to_string(page, lang='hin')
        full_text += text + "\n\n"
    
    return full_text

def main(pdf_path):
    """Extract text from a PDF."""
    hindi_text = extract_text_from_pdf(pdf_path)

    # Save the extracted text to a file
    with open("extracted_output.txt", "w", encoding="utf-8") as f:
        f.write(hindi_text)

if __name__ == "__main__":
    pdf_path = "/workspaces/pythontest/Test.pdf"  # Adjust the path as needed
    main(pdf_path)

