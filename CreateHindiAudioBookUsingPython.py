# Install the barcode library if not already installed
# pip install gTTS

from gtts import gTTS
import os

def create_audiobook(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
         text = file.read()

    tts = gTTS(text=text, lang='hi')
    tts.save(output_file)

text_file = "/workspaces/pythontest/AudioBookHindi.txt" 
# Ensure this file exists and contains text
output_file = "/workspaces/pythontest/AudioBookHindi.mp3"

create_audiobook(text_file, output_file)
print(f"Audiobook saved as {output_file}")

# To play the file, use an appropriate command based on the OS
if os.name == 'nt':  # Windows
    os.system(f"start {output_file}")
elif os.name == 'posix':  # macOS or Linux
    os.system(f"xdg-open {output_file}")
