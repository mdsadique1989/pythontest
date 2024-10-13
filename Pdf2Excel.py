import os
from PyPDF2 import PdfReader
import pandas as pd

def pdf_to_text(pdf_file):
    text = ""  # Initialize text variable
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            if page_text:  # Check if the page text is not None
                text += page_text  # Append the extracted text
    return text

def pdf_to_excel(pdf_file, output_file):
    text = pdf_to_text(pdf_file)  # Pass pdf_file as an argument
    lines = text.split('\n')  # Split the text into lines
    df = pd.DataFrame(lines)  # Create a DataFrame from the lines
    df.to_excel(output_file, index=False, header=False)  # Save DataFrame to Excel

# Example usage:
pdf_file = "/workspaces/pythontest/Monthly Marksheet.pdf"
output_excel_file = "/workspaces/pythontest/output_excel.xlsx"
pdf_to_excel(pdf_file, output_excel_file)
print("Excel file created:", output_excel_file)
