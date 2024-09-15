# YTubeInsight

YTubeInsight is a Python package for effortless YouTube channel analytics. Track video counts, extract details, and gain insights from YouTube channels with ease.

## Features

- Analyze YouTube channels using either full channel URLs or channel IDs
- Count videos published within the last year
- Retrieve detailed information about each video (title, publish date, URL)
- Easy-to-use API with comprehensive error handling
- Compatibility with Python 3.6+

## Installation

You can install YTubeInsight using pip:

```
pip install ytubeinsight
```

## Quick Start

Here's a simple example of how to use YTubeInsight:

```python
from ytubeinsight import analyze_channel

# Replace with your YouTube Data API key
API_KEY = 'YOUR_API_KEY_HERE'

# Analyze a channel by URL
channel_url = 'https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw'
result = analyze_channel(channel_url, API_KEY)

print(f"Videos published in the last year: {result['video_count']}")

# Print details of the first video
if result['video_data']:
    video = result['video_data'][0]
    print(f"Latest video:")
    print(f"Title: {video['title']}")
    print(f"Published on: {video['published_at']}")
    print(f"URL: {video['url']}")
```

## Detailed Usage

### Analyzing a channel by URL

```python
from ytubeinsight import analyze_channel

result = analyze_channel('https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw', 'YOUR_API_KEY')
```

### Analyzing a channel by ID

```python
from ytubeinsight import analyze_channel

result = analyze_channel('UCJFp8uSYCjXOMnkUyb3CQ3Q', 'YOUR_API_KEY', is_channel_id=True)
```

### Handling errors

```python
from ytubeinsight import analyze_channel, YTubeInsightError

try:
    result = analyze_channel('invalid_channel_url', 'YOUR_API_KEY')
except YTubeInsightError as e:
    print(f"An error occurred: {str(e)}")
```

## API Reference

### analyze_channel(channel_input, api_key, is_channel_id=False)

Analyzes a YouTube channel and returns video data for the past year.

- `channel_input`: Either a full channel URL or channel ID
- `api_key`: YouTube Data API key
- `is_channel_id`: Boolean indicating if channel_input is a channel ID

Returns a dictionary containing:
- `video_count`: Number of videos published in the last year
- `video_data`: List of dictionaries, each containing video details (title, publish date, URL)

## Requirements

- Python 3.6+
- google-api-python-client
- requests
- beautifulsoup4

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Google for providing the YouTube Data API
- All contributors who will help improve this package

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/yourusername/YTubeInsight/issues) on GitHub.

## Disclaimer

This project is not affiliated with, authorized, maintained, sponsored or endorsed by YouTube or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use at your own risk.
