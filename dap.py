import requests
from tqdm import tqdm

def download_file(url, destination):
    try:
        # Send a GET request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        # Get the total file size from the response headers
        total_size = int(response.headers.get('content-length', 0))

        # Open the destination file in write-binary mode
        with open(destination, 'wb') as file:
            # Use tqdm to create a progress bar
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=destination) as bar:
                for data in response.iter_content(chunk_size=1024):  # Download in chunks
                    bar.update(len(data))  # Update the progress bar
                    file.write(data)  # Write data to the file

        print(f'Download completed: {destination}')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    # Example usage
    file_url = input("Enter the URL of the file to download: ")
    destination_file = input("Enter the destination filename (including path if needed): ")

