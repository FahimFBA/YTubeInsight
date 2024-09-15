"""Basic usage example for YTubeInsight."""

import os
from ytubeinsight import analyze_channel, YTubeInsightError

# Replace with your actual YouTube Data API key
API_KEY = os.environ.get('YOUTUBE_API_KEY', 'YOUR_API_KEY_HERE')

def main():
    """Run example analyses on YouTube channels."""
    # Example with full channel URL
    channel_url = 'https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw'  # Google Developers channel
    print("Analyzing channel by URL...")
    analyze_channel_and_print_results(channel_url, API_KEY)

    # Example with channel ID
    channel_id = 'UCJFp8uSYCjXOMnkUyb3CQ3Q'  # Tasty channel
    print("\nAnalyzing channel by ID...")
    analyze_channel_and_print_results(channel_id, API_KEY, is_channel_id=True)

def analyze_channel_and_print_results(channel_input, api_key, is_channel_id=False):
    """Analyze a channel and print the results."""
    try:
        result = analyze_channel(channel_input, api_key, is_channel_id=is_channel_id)
        print(f"Videos published in the last year: {result['video_count']}")
        print("\nFirst 5 videos:")
        for video in result['video_data'][:5]:
            print(f"Title: {video['title']}")
            print(f"Published on: {video['published_at']}")
            print(f"URL: {video['url']}")
            print()
    except YTubeInsightError as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()