# MP4 to MP3 Converter

Simple Python script to convert MP4 videos to MP3 audio files in bulk.

## Quick Setup (macOS)

1. **Install FFmpeg** (if not already installed):
```bash
brew install ffmpeg
```

2. **Set up Python environment**:
```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Usage

```bash
# Basic usage (creates 'converted_mp3' folder in input directory)
python mp4_to_mp3_converter.py /path/to/your/videos

# Or specify output directory
python mp4_to_mp3_converter.py /path/to/your/videos -o /path/to/output
```

## When Done

```bash
deactivate
```

## Troubleshooting

If you encounter errors:
- Ensure FFmpeg is installed: `brew install ffmpeg`
- Check file permissions
- Verify videos have audio tracks
