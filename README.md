# YouTube Downloader

A simple Python script that allows you to download YouTube videos using the `pytube` library. This project is designed to help users easily download YouTube videos by providing the video URL.

## Features

- Downloads the highest resolution available for the video.
- Simple and easy-to-use Python script.
- Uses the `pytube` library to handle video downloading.

## Prerequisites

To use this script, you need to have Python 3 installed on your system. You also need to install the required dependencies, which are listed in the `requirements.txt` file.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
   ```

2. (Optional) Create and activate a virtual environment (recommended):

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python youtube_downloader.py
   ```

2. When prompted, paste the URL of the YouTube video you wish to download.

3. The video will be downloaded to the current directory by default.

### Example:

```bash
Enter the YouTube video URL: https://www.youtube.com/watch?v=abcd1234
Downloading: Example Video Title
Download completed! Video saved to: ./
```

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Please make sure to write tests and documentation for any new features or bug fixes.
