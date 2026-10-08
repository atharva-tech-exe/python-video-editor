import os
import subprocess
import imageio_ffmpeg


# ==============================
# SETTINGS
# ==============================

VIDEO_FILE = "VID-20231014-WA0053.mp4"
OUTPUT_FOLDER = "clips"
CLIP_DURATION = 30


# ==============================
# CREATE OUTPUT FOLDER
# ==============================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ==============================
# GET VIDEO DURATION
# ==============================

ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

# Get duration using ffprobe is more complicated,
# so we use MoviePy only to read the duration.
from moviepy import VideoFileClip

video = VideoFileClip(VIDEO_FILE)
total_duration = video.duration
video.close()

print(f"Video duration: {total_duration:.2f} seconds")


# ==============================
# SPLIT VIDEO
# ==============================

clip_number = 1
start_time = 0

while start_time < total_duration:

    end_time = min(start_time + CLIP_DURATION, total_duration)
    duration = end_time - start_time

    output_file = os.path.join(
        OUTPUT_FOLDER,
        f"clip_{clip_number:02d}.mp4"
    )

    print(
        f"Creating Clip {clip_number}: "
        f"{start_time:.2f}s → {end_time:.2f}s"
    )

    command = [
        ffmpeg,

        "-ss", str(start_time),
        "-i", VIDEO_FILE,

        "-t", str(duration),

        "-c:v", "libx264",
        "-c:a", "aac",

        "-y",
        output_file
    ]

    subprocess.run(command, check=True)

    print(f"Saved: {output_file}")

    clip_number += 1
    start_time += CLIP_DURATION


# ==============================
# DONE
# ==============================

print("\nDone!")
print(f"Created {clip_number - 1} clips.")
print(f"Clips saved in: {OUTPUT_FOLDER}")