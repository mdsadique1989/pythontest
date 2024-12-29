from rembg import remove
from PIL import Image

# Define input and output paths
input_path = "/workspaces/pythontest/test.jpg"  # Make sure this file exists
output_path = "/workspaces/pythontest/testedited.jpg"

# Open the input image
input_image = Image.open(input_path)

# Remove the background from the input image
output_image = remove(input_image)

# Convert to RGB (if saving as JPEG) or keep as RGBA for PNG
if output_image.mode == 'RGBA':
    output_image = output_image.convert('RGB')

# Save the output image
output_image.save(output_path, format='PNG')  # You can change 'PNG' to 'JPEG' if needed
