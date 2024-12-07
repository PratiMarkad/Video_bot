import instaloader

def download_instagram_video(url, output_path):
    try:
        # Create an instance of Instaloader
        loader = instaloader.Instaloader()

        # Login to Instagram (use your credentials)
        loader.login("your_username", "your_password")

        # Extract post using URL
        post = instaloader.Post.from_url(loader.context, url)

        # Download the post (video or image)
        loader.download_post(post, target=output_path)

        print(f"Downloaded Instagram video to {output_path}")
    except Exception as e:
        print(f"Error while downloading video: {e}")

# Example usage
if __name__ == "__main__":
    url = "https://www.instagram.com/reel/DDJzYAoNeeV/"  # Replace with actual URL
    output_path = "videos"
    download_instagram_video(url, output_path)
