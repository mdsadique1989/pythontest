import os
import requests
import zipfile
from tqdm import tqdm

def download_file(url, destination):
    print("\n--- 1. Starting Download ---")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    try:
        with requests.get(url, headers=headers, stream=True, allow_redirects=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
        initial_pos = 0
        mode = 'wb'
        if os.path.exists(destination):
            initial_pos = os.path.getsize(destination)
            if initial_pos == total_size and total_size != 0:
                print(f"File already fully downloaded: {destination}")
                return True
            elif initial_pos > total_size:
                initial_pos = 0
            else:
                mode = 'ab'
        req_headers = headers.copy()
        if initial_pos > 0:
            req_headers['Range'] = f'bytes={initial_pos}-'
        response = requests.get(url, headers=req_headers, stream=True, allow_redirects=True)
        response.raise_for_status()
        if response.status_code == 200 and initial_pos > 0:
            initial_pos = 0
            mode = 'wb'
        with open(destination, mode) as file:
            with tqdm(
                total=total_size, initial=initial_pos, unit='B',
                unit_scale=True, unit_divisor=1024, desc=destination
            ) as bar:
                for data in response.iter_content(chunk_size=8192):
                    if data:
                        bar.update(len(data))
                        file.write(data)
        print('\nDownload completed successfully!')
        return True
    except Exception as e:
        print(f'\nError during download: {e}')
        return False

def compress_file(file_path):
    print("\n--- 2. Starting Compression ---")
    if not os.path.exists(file_path):
        print(f"Error: Could not find '{file_path}' to compress.")
        return
    zip_path = file_path + ".zip"
    print(f"Compressing '{file_path}' into '{zip_path}'...")
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        original_size = os.path.getsize(file_path) / (1024 * 1024)
        compressed_size = os.path.getsize(zip_path) / (1024 * 1024)
        saved_space = original_size - compressed_size
        print(f"\nSuccess! File is zipped and ready to transfer.")
        print(f"Original Size:   {original_size:.2f} MB")
        print(f"Compressed Size: {compressed_size:.2f} MB")
        print(f"You saved:       {saved_space:.2f} MB of download time!")
    except Exception as e:
        print(f"Error during compression: {e}")

if __name__ == '__main__':
    file_url = input("Enter the URL of the file to download: ").strip()
    if not file_url:
        print("No URL provided. Exiting.")
    else:
        default_filename = file_url.split('/')[-1].split('?')[0]
        if not default_filename:
            default_filename = "downloaded_file.bin"
        destination_file = input(f"Enter destination filename (Press Enter for '{default_filename}'): ").strip()
        if not destination_file:
            destination_file = default_filename
        if download_file(file_url, destination_file):
            compress_file(destination_file)