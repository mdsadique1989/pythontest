# Install the barcode library if not already installed
# pip install python-barcode

from barcode import Code128  # Import the specific barcode type
from barcode.writer import ImageWriter  # To save as an image file

# Define a function to generate a barcode
def generate_barcode(data):
    # Create a Code128 barcode object with the given data
    code = Code128(data, writer=ImageWriter())  # Use ImageWriter to save as an image
    # Save the barcode as an image file
    code.save("barcode")
    print("Barcode generated and saved as 'barcode.png'.")

# Main execution
data = "1234-5678-9101"
generate_barcode(data)
