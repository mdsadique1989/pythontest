from rembg import remove
from PIL import Image
import io

# Define input and output paths
input_path = "/workspaces/pythontest/cl.PNG"
output_path = "/workspaces/pythontest/cl.PNG"

# Open the input image
input_image = Image.open(input_path)

# Remove the background from the input image
output_image = remove(input_image)  # This directly gives you a PIL Image

# Save the output image
output_image.save(output_path)

print("Output image saved as:", output_path)
