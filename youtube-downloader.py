from pytube import YouTube

def download_video(url, save_path='./'):
    try:
        # Creating a YouTube object using the URL
        yt = YouTube(url)

        # Choosing the best stream based on resolution
        video_stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")
        video_stream.download(output_path=save_path)
        print(f"Download completed! Video saved to: {save_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Get URL input from the user
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
