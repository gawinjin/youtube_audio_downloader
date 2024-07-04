# youtube_audio_downloader
# Download highest audio quality from YouTube

1. First, we import the necessary libraries:
   - os for file and path operations
   - pytube for YouTube video downloading
   - re for regular expressions (used in filename sanitization)

2. We define a sanitize_filename function to remove invalid characters from the video title when using it as a filename.

3. The download_audio function:
   - Creates a YouTube object from the URL
   - Filters for audio-only streams and selects the highest quality
   - Prepares the output filename (video title + .mp3 extension)
   - Downloads the audio stream and saves it as an MP3 file

4. The main functions
   - Sets the default download path to the user's Desktop
   - Runs in a loop, allowing multiple downloads
   - Prompts for YouTube URL and output path (using default if not specified)
   - Calls the download_audio function for each URL

To use this script:

1. Install the required library:
pip install pytube

2. Save the script to a file (e.g., youtube_audio_downloader.py)
3. Run the script:
python youtube_audio_downloader.py

4. Enter a YouTube URL when prompted. Press Enter to use the default download location (Desktop) or enter a custom path.
5. Repeat for multiple downloads, or enter 'q' to quit.
