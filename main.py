# from downloader.instagram import download_instagram_video
# from uploader.upload import get_upload_url, upload_video, create_post
import instaloader
from downloader.instagram import download_instagram_video
from uploader.upload import upload_video_to_server

from utils.file_monitor import monitor_directory

def main():
    # Example usage
    token = "<YOUR_TOKEN>"
    video_url = "<INSTAGRAM_VIDEO_URL>"
    output_path = "./videos/insta_video.mp4"

    # Step 1: Download Video
    download_instagram_video(video_url, output_path)

    # Step 2: Get Upload URL
    upload_info = get_upload_url(token)
    upload_url = upload_info.get("url")
    hash_value = upload_info.get("hash")

    # Step 3: Upload Video
    if upload_video(output_path, upload_url):
        print("Video uploaded successfully!")

        # Step 4: Create Post
        post_response = create_post(token, "Example Title", hash_value, 1)
        print("Post Created:", post_response)
    else:
        print("Failed to upload video.")

    # Step 5: Monitor directory for new videos
    monitor_directory("./videos")

if __name__ == "__main__":
    main()
