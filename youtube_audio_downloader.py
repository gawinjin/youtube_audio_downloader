import os
from pytube import YouTube
import re

def sanitize_filename(title):
    """Remove invalid characters from the filename."""
    return re.sub(r'[\\/*?:"<>|]', "", title)

def download_audio(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        if not audio_stream:
            print("No audio stream found for this video.")
            return

        # Prepare the output filename
        file_name = sanitize_filename(yt.title) + '.mp3'
        file_path = os.path.join(output_path, file_name)

        # Download the audio
        print(f"Downloading audio: {yt.title}")
        audio_stream.download(output_path=output_path, filename=file_name)

        print(f"Download complete! Saved to: {file_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    print("YouTube Audio Downloader")
    print("========================")

    # Set default download path to Desktop
    default_path = os.path.join(os.path.expanduser("~"), "Desktop")
    print(f"Default download location: {default_path}")

    while True:
        url = input("\nEnter the YouTube video URL (or 'q' to quit): ")
        
        if url.lower() == 'q':
            break

        output_path = input("Enter the output path (press Enter for default): ").strip()
        if not output_path:
            output_path = default_path

        if not os.path.exists(output_path):
            print(f"The path {output_path} does not exist. Using default path.")
            output_path = default_path

        download_audio(url, output_path)

if __name__ == "__main__":
    main()