import os
import subprocess

# --- CONFIGURATION ---
CRF_VALUE = 22        
PRESET = "veryfast"   
OUTPUT_DIR = "Output_Compressed"
# ---------------------

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

video_extensions = ('.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.ts', '.mpg', '.m4v', '.3gp')
files = [f for f in os.listdir('.') if f.lower().endswith(video_extensions)]

if not files:
    print("No video files found.")
else:
    print(f"Found {len(files)} videos.")

    for filename in files:
        input_path = filename
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}_hevc.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        print(f"\n------------------------------------------------")
        print(f"PROCESSING: {filename}")
        print(f"------------------------------------------------")

        command = [
            "ffmpeg", "-v", "error", "-stats", "-i", input_path,
            "-c:v", "libx265", "-crf", str(CRF_VALUE), "-preset", PRESET,
            "-c:a", "aac", "-b:a", "192k", output_path
        ]

        try:
            # 1. Compress
            subprocess.run(command, check=True)
            print(f"\n[SUCCESS] Compression done. New file is at: {output_path}")
            
            # 2. PAUSE and Ask for Confirmation (The "Download Trigger")
            print(">>> ACTION REQUIRED: Please Download the new file now.")
            user_input = input(f">>> Did you finish downloading '{output_filename}'? Type 'yes' to delete original: ")

            # 3. Check Input and Delete
            if user_input.lower().strip() == 'yes':
                os.remove(input_path)
                print(f"[CLEANUP] Original file '{filename}' deleted.")
            else:
                print(f"[SAFEGUARD] Original file KEPT. Moving to next...")

        except subprocess.CalledProcessError:
            print(f"[ERROR] FFmpeg failed for {filename}. No files deleted.")
            if os.path.exists(output_path): os.remove(output_path)

print("\nAll tasks finished.")