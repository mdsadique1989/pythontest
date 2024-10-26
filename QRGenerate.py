import qrcode
from PIL import Image

data = input("Enter anything to generate QR: ")
# Create an instance of the QRCode class
qr = qrcode.QRCode(version=2, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)

# Generate the QR code image
image = qr.make_image(fill="black", back_color="white")
image.save("qr_code.png")

# Display the generated QR code
image.show()  # Use .show() instead of Image.open() to display
