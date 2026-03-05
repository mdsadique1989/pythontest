import os, requests, subprocess, time
from tqdm import tqdm

def download(url, dest):
    print("--- Downloading: " + dest)
    r = requests.get(url, stream=True)
    r.raise_for_status()
    total = int(r.headers.get('content-length', 0))
    with open(dest, 'wb') as f, tqdm(total=total, unit='B', unit_scale=True, desc=dest) as bar:
        for chunk in r.iter_content(8192):
            f.write(chunk)
            bar.update(len(chunk))
    return True

def shrink(input_f, is_trim):
    print("\n--- Compressing ---")
    start = time.time()
    os.makedirs('shrunk', exist_ok=True)
    
    out_name = "test_trim.mp4" if is_trim else "full_movie.mp4"
    out_path = os.path.join('shrunk', out_name)
    
    # Base command
    cmd = [
        'ffmpeg', '-y', '-i', input_f, 
        '-vcodec', 'libx264', 
        '-preset', 'superfast', 
        '-crf', '28', 
        '-vf', 'scale=-2:720', 
        '-c:a', 'aac'
    ]

    # Add Trim parameters if requested (First 5 minutes)
    if is_trim:
        print("⚠️ Mode: 5-Minute Test Trim")
        cmd += ['-t', '00:05:00']
    
    cmd.append(out_path)
    
    # Run the process
    subprocess.run(cmd, check=True)
    
    end = time.time()
    s2 = os.path.getsize(out_path) / 1024 / 1024
    
    print(f"\n[DONE] Took {round((end-start)/60, 2)} minutes")
    print(f"Finished Size: {round(s2, 2)} MB")
    
    codespace_name = os.getenv('CODESPACE_NAME')
    if codespace_name:
        print("\n🚀 VIEW YOUR VIDEO HERE:")
        print(f"https://{codespace_name}-8000.app.github.dev/shrunk/{out_name}")

if __name__ == '__main__':
    u = input('Enter Movie URL: ').strip()
    if u:
        trim_choice = input('Do you want to test only the first 5 mins? (y/n): ').lower().strip()
        is_trim = True if trim_choice == 'y' else False
        
        temp_name = "original_download.tmp"
        if download(u, temp_name):
            shrink(temp_name, is_trim)
            
            # Clean up logic
            if not is_trim: # Keep original if just a test, or delete if full? 
                os.remove(temp_name)
                print(f"--- Deleted original {temp_name} ---")