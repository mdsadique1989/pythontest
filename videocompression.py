import os
import subprocess

# --- CONFIGURATION ---
# The crf value: Lower is better quality. 
# 22 is visually lossless. 24 is smaller file size.
CRF_VALUE = 22 

# Preset: 'medium' is standard. 'veryfast' is recommended for Cloud/CPUs.
PRESET = "veryfast" 

# Output folder name
OUTPUT_DIR = "Output_Compressed"
# ---------------------

# 1. Create Output Directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 2. Define supported formats
video_extensions = ('.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv', '.webm', '.ts', '.mpg', '.m4v', '.3gp')

# 3. Scan and Compress
files = [f for f in os.listdir('.') if f.lower().endswith(video_extensions)]

if not files:
    print("No video files found in the current directory.")
else:
    print(f"Found {len(files)} videos. Starting compression...")

    for filename in files:
        # Construct input and output paths
        input_path = filename
        name_without_ext = os.path.splitext(filename)[0]
        output_filename = f"{name_without_ext}_hevc.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)

        print(f"-> Processing: {filename}...")

        # 4. Build the FFmpeg Command
        # This matches the "Option B" (Speed Boost) logic
        command = [
            "ffmpeg",
            "-v", "error",          # Hide junk output
            "-stats",               # Show progress bar
            "-i", input_path,       # Input file
            "-c:v", "libx265",      # Video Codec: H.265
            "-crf", str(CRF_VALUE), # Quality Level
            "-preset", PRESET,      # Speed setting
            "-c:a", "aac",          # Audio Codec: AAC (Universal)
            "-b:a", "192k",         # Audio Quality: 192kbps
            output_path             # Output file
        ]

        # 5. Execute the command
        try:
            subprocess.run(command, check=True)
            print(f"   [DONE] Saved to: {output_path}")
        except subprocess.CalledProcessError as e:
            print(f"   [ERROR] Failed to convert {filename}")

print("\nAll tasks finished.")