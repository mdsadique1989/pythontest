from gtts import gTTS
from PyPDF2 import PdfReader

def pdf_to_text(pdf_file):
    text = ""  # Initialize text variable
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text() or ""  # Safely handle None if no text is extracted
    return text

def text_to_audio(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)

# Example usage:
pdf_file = "/workspaces/pythontest/Essay.pdf"
output_audio_file = "/workspaces/pythontest/Essay_audio.mp3"
text = pdf_to_text(pdf_file)

# Check if text extraction is successful
if text.strip():  # Ensure there's some text to convert
    text_to_audio(text, output_audio_file)
    print("Audio file saved as:", output_audio_file)
else:
    print("No text found in the PDF.")
