import random
from captcha.audio import AudioCaptcha

def generate_random_captcha(length=6):
    characters = '1234567890'
    captcha_text = "".join(random.choices(characters, k=length))  # Corrected here
    return captcha_text

# Create an instance of AudioCaptcha
audio = AudioCaptcha()

# Generate the CAPTCHA text
captcha_text = generate_random_captcha()  # Call the function to generate the captcha text

print("Generated CAPTCHA text:", captcha_text)

# Generate the audio CAPTCHA
audio_captcha = audio.generate(captcha_text)  # Corrected here
audio.write(captcha_text, 'Audio_Captcha.wav')  # Corrected quote

print("Audio CAPTCHA generated: Audio_Captcha.wav")
