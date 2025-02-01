# YTubeInsight

[![PyPI version](https://badge.fury.io/py/ytubeinsight.svg)](https://badge.fury.io/py/ytubeinsight)
[![Python Versions](https://img.shields.io/pypi/pyversions/ytubeinsight.svg)](https://pypi.org/project/ytubeinsight/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/ytubeinsight/badge/?version=latest)](https://ytubeinsight.readthedocs.io/en/latest/?badge=latest)
![PyPI Downloads](https://static.pepy.tech/badge/ytubeinsight)

YTubeInsight is a Python package for effortless YouTube channel analytics. Track video counts, extract details, and gain insights from YouTube channels with ease. You can check the download stats of YTubeInsight [here](https://pypistats.org/packages/ytubeinsight).

## Features

- Analyze YouTube channels using either full channel URLs or channel IDs
- Count videos published within the last year
- Retrieve detailed information about each video (title, publish date, URL)
- Easy-to-use API with comprehensive error handling
- Compatibility with Python 3.6+

## Installation

You can install YTubeInsight using pip. We recommend using a virtual environment to manage your dependencies. You can choose between venv (built into Python) or conda based on your preference.

### Option 1: Using venv

1. Create a virtual environment:
   ```
   python -m venv ytubeinsight-env
   ```

2. Activate the virtual environment:
   - On Windows:
     ```
     ytubeinsight-env\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source ytubeinsight-env/bin/activate
     ```

3. Install YTubeInsight:
   ```
   pip install ytubeinsight
   ```

### Option 2: Using conda

1. Create a conda environment:
   ```
   conda create --name ytubeinsight-env python=3.8
   ```

2. Activate the conda environment:
   ```
   conda activate ytubeinsight-env
   ```

3. Install YTubeInsight:
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

For more detailed API documentation, please visit our [Read the Docs page](https://ytubeinsight.readthedocs.io/).

## Obtaining a YouTube Data API Key

To use YTubeInsight, you need a YouTube Data API key. Here's how to get one:

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project or select an existing one.
3. Enable the YouTube Data API v3 for your project.
4. Create credentials (API key) for your project.
5. Use this API key in your YTubeInsight calls.

Remember to keep your API key secret and never share it publicly.

## Requirements

- Python 3.6+
- google-api-python-client
- requests
- beautifulsoup4

## Development

To set up the development environment:

1. Clone the repository:
   ```
   git clone https://github.com/FahimFBA/YTubeInsight.git
   cd YTubeInsight
   ```

2. Create and activate a virtual environment (choose one):
   - Using venv:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Using conda:
     ```
     conda create --name ytubeinsight-dev python=3.8
     conda activate ytubeinsight-dev
     ```

3. Install the development dependencies:
   ```
   pip install -e .[dev]
   ```

4. Run the tests:
   ```
   pytest
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

For a detailed changelog, please see the [CHANGELOG.md](CHANGELOG.md) file.

## Acknowledgments

- Google for providing the YouTube Data API
- All contributors who help improve this package

## Support

If you encounter any problems or have any questions, please [open an issue](https://github.com/FahimFBA/YTubeInsight/issues) on GitHub.

## Disclaimer

This project is not affiliated with, authorized, maintained, sponsored or endorsed by YouTube or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use at your own risk.
