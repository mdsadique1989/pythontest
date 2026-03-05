import os
import requests
from tqdm import tqdm

def download_file(url, destination):
    # Add a User-Agent so the server thinks this is a standard web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        # 1. Get the total file size using GET with stream=True (Bypasses the 405 HEAD error)
        with requests.get(url, headers=headers, stream=True, allow_redirects=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
        
        # 2. Check local file to determine if we need to resume
        initial_pos = 0
        mode = 'wb' # Default to writing binary (overwrite)
        
        if os.path.exists(destination):
            initial_pos = os.path.getsize(destination)
            if initial_pos == total_size and total_size != 0:
                print(f"File already fully downloaded: {destination}")
                return
            elif initial_pos > total_size:
                print("Local file is larger than the remote file. Restarting download.")
                initial_pos = 0
            else:
                mode = 'ab'  # Append binary (resume)
        
        # 3. Add the Range header if we are resuming a partial download
        req_headers = headers.copy()
        if initial_pos > 0:
            req_headers['Range'] = f'bytes={initial_pos}-'

        # 4. Initiate the actual download request
        response = requests.get(url, headers=req_headers, stream=True, allow_redirects=True)
        response.raise_for_status()

        # Fallback: If server ignores the Range request, it returns 200 OK instead of 206 Partial Content
        if response.status_code == 200 and initial_pos > 0:
            print("Server does not support resuming downloads. Starting from scratch.")
            initial_pos = 0
            mode = 'wb'

        # 5. Write to file and update progress bar
        with open(destination, mode) as file:
            with tqdm(
                total=total_size,
                initial=initial_pos,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
                desc=destination
            ) as bar:
                for data in response.iter_content(chunk_size=8192):
                    if data:
                        bar.update(len(data))
                        file.write(data)

        print(f'\nDownload completed: {destination}')

    except Exception as e:
        print(f'\nError: {e}')
        


if __name__ == '__main__':
    # Your requested URL
    file_url = "https://cdn01.foxitsoftware.com/product/reader/desktop/win/2025.3.0/FoxitPDFReader20253_L10N_Setup_Prom_x64.exe"
    
    # Automatically extract the filename from the URL
    default_filename = file_url.split('/')[-1]
    
    print(f"Target URL: {file_url}")
    
    # Allow user to press Enter to accept the default filename
    destination_file = input(f"Enter destination filename (Press Enter for '{default_filename}'): ")
    if not destination_file.strip():
        destination_file = default_filename

    download_file(file_url, destination_file)
    