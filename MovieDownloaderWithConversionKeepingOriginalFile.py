import os, requests, subprocess, time
from tqdm import tqdm

def download(url, dest):
    print("--- Downloading: " + dest)
    r = requests.get(url, stream=True)
    r.raise_for_status()
    total = int(r.headers.get('content-length', 0))
    with open(dest, 'wb') as f, tqdm(total=total, unit='B', unit_scale=True, desc=dest) as bar:
        for chunk in r.iter_content(8192):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                bar.update(len(chunk))
    return True

def shrink(input_f):
    print("--- Compressing ---")
    start = time.time()
    os.makedirs('shrunk', exist_ok=True)
    out = os.path.join('shrunk', 'shrunk_' + input_f)
    # Using ffmpeg to compress
    cmd = ['ffmpeg', '-y', '-i', input_f, '-vcodec', 'libx264', '-crf', '28', '-vf', 'scale=-2:720', out]
    subprocess.run(cmd, check=True)
    
    end = time.time()
    s1 = os.path.getsize(input_f) / 1024 / 1024
    s2 = os.path.getsize(out) / 1024 / 1024
    
    print("[DONE] Took " + str(round(end-start, 1)) + " seconds")
    print("Original: " + str(round(s1, 2)) + " MB")
    print("Shrunk:   " + str(round(s2, 2)) + " MB")

if __name__ == "__main__":
    u = input('Enter Movie URL: ').strip()
    if u:
        # Extract filename from URL
        filename = u.split('/')[-1].split('?')[0] or 'movie.mp4'
        if download(u, filename):
            shrink(filename)
            