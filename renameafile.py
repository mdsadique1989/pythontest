import os

# Example file path in Google Drive
current_file_name = '/workspaces/pythontest/input.jpg'
new_file_name = '/workspaces/pythontest/input.extension'  # No .jpg extension

# Rename the file
os.rename(current_file_name, new_file_name)

print(f"Renamed '{current_file_name}' to '{new_file_name}'")
