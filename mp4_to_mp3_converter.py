import os
from moviepy.editor import VideoFileClip
from pathlib import Path
import argparse
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def setup_argparse():
    """Set up command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Convert MP4 videos to MP3 audio files."
    )
    parser.add_argument("input_dir", type=str, help="Directory containing MP4 files")
    parser.add_argument(
        "-o",
        "--output_dir",
        type=str,
        help="Output directory for MP3 files (default: input_dir/converted_mp3)",
        default=None,
    )
    return parser


def convert_mp4_to_mp3(video_path, output_path):
    """
    Convert a single MP4 file to MP3.

    Args:
        video_path (str): Path to input MP4 file
        output_path (str): Path to output MP3 file

    Returns:
        bool: True if conversion successful, False otherwise
    """
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        if audio is None:
            logger.error(f"No audio track found in {video_path}")
            return False

        audio.write_audiofile(output_path)
        audio.close()
        video.close()
        logger.info(f"Successfully converted {video_path} to {output_path}")
        return True

    except Exception as e:
        logger.error(f"Error converting {video_path}: {str(e)}")
        return False


def process_directory(input_dir, output_dir=None):
    """
    Process all MP4 files in the input directory.

    Args:
        input_dir (str): Input directory path
        output_dir (str, optional): Output directory path
    """
    # Create Path objects
    input_path = Path(input_dir)
    if output_dir is None:
        output_path = input_path / "converted_mp3"
    else:
        output_path = Path(output_dir)

    # Create output directory if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)

    # Get all MP4 files
    mp4_files = list(input_path.glob("*.mp4"))
    total_files = len(mp4_files)

    if total_files == 0:
        logger.warning(f"No MP4 files found in {input_dir}")
        return

    logger.info(f"Found {total_files} MP4 files to convert")

    # Track conversion statistics
    successful = 0
    failed = 0

    # Process each file
    for mp4_file in mp4_files:
        output_file = output_path / f"{mp4_file.stem}.mp3"

        if convert_mp4_to_mp3(str(mp4_file), str(output_file)):
            successful += 1
        else:
            failed += 1

    # Print summary
    logger.info("\nConversion Summary:")
    logger.info(f"Total files processed: {total_files}")
    logger.info(f"Successfully converted: {successful}")
    logger.info(f"Failed conversions: {failed}")


def main():
    """Main function to run the converter."""
    parser = setup_argparse()
    args = parser.parse_args()

    # Validate input directory
    if not os.path.isdir(args.input_dir):
        logger.error(f"Input directory '{args.input_dir}' does not exist!")
        return

    # Process the directory
    process_directory(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
