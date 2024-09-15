from ytubeinsight import analyze_channel
import os

# Replace with your actual YouTube Data API key
API_KEY = os.environ.get('YOUTUBE_API_KEY', 'YOUR_API_KEY_HERE')

def main():
    # Example with full channel URL
    channel_url = 'https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw'  # Google Developers channel
    print("Analyzing channel by URL...")
    try:
        result = analyze_channel(channel_url, API_KEY)
        print(f"Videos published in the last year: {result['video_count']}")
        print("\nFirst 5 videos:")
        for video in result['video_data'][:5]:
            print(f"Title: {video['title']}")
            print(f"Published on: {video['published_at']}")
            print(f"URL: {video['url']}")
            print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Example with channel ID
    channel_id = 'UCJFp8uSYCjXOMnkUyb3CQ3Q'  # Tasty channel
    print("\nAnalyzing channel by ID...")
    try:
        result = analyze_channel(channel_id, API_KEY, is_channel_id=True)
        print(f"Videos published in the last year: {result['video_count']}")
        print("\nFirst 5 videos:")
        for video in result['video_data'][:5]:
            print(f"Title: {video['title']}")
            print(f"Published on: {video['published_at']}")
            print(f"URL: {video['url']}")
            print()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()