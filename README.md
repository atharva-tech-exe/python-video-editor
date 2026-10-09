# Video Splitter

A simple Python script that automatically splits a video into multiple **30-second clips** using FFmpeg.

## Features
- Automatically detects the video duration.
- Splits the video into 30-second clips.
- Handles the remaining video even if it is shorter than 30 seconds.
- Saves all clips in a separate `clips` folder.
- Exports clips in MP4 format.

## Requirements

Install the required libraries:

```bash
pip install imageio-ffmpeg moviepy
```

## Usage

1. Place your video file in the same folder as the Python script.
2. Set the input filename in `VIDEO_FILE`.
3. Adjust `CLIP_DURATION` if needed.
4. Run the script:

```bash
python video_splitter.py
```

## Output

The generated clips will be saved in the `clips` folder:

```text
clips/
├── clip_01.mp4
├── clip_02.mp4
├── clip_03.mp4
└── ...
```

## Technologies Used
- Python
- FFmpeg
- MoviePy
- ImageIO-FFmpeg

## Use Cases
Useful for splitting long videos into short clips for social media, content creation, and video editing.
