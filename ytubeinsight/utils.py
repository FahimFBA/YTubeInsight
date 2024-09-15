"""Utility functions for YTubeInsight."""

import re
import requests
from bs4 import BeautifulSoup
from .exceptions import YTubeInsightError


def get_channel_id(url):
    """
    Extract the channel ID from a YouTube channel URL.

    Args:
        url (str): YouTube channel URL

    Returns:
        str or None: Channel ID if found, None otherwise

    Raises:
        YTubeInsightError: If an error occurs during channel ID extraction
    """
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Try to find the channel ID in the URL
        channel_id_match = re.search(r'youtube\.com/channel/([^/?&]+)', url)
        if channel_id_match:
            return channel_id_match.group(1)

        # If not found in URL, try to extract from the page source
        channel_id_match = re.search(r'"channelId":"([^"]+)"', response.text)
        if channel_id_match:
            return channel_id_match.group(1)

        # If still not found, try to extract from meta tags
        meta_tag = soup.find('meta', {'itemprop': 'channelId'})
        if meta_tag:
            return meta_tag['content']

        return None
    except requests.RequestException as e:
        raise YTubeInsightError(
            f"Error extracting channel ID: {str(e)}") from e


def get_uploads_playlist_id(youtube, channel_id):
    """
    Get the uploads playlist ID for a YouTube channel.

    Args:
        youtube: YouTube API client
        channel_id (str): YouTube channel ID

    Returns:
        str or None: Uploads playlist ID if found, None otherwise

    Raises:
        YTubeInsightError: If an error occurs during playlist ID retrieval
    """
    try:
        request = youtube.channels().list(
            part="contentDetails",
            id=channel_id
        )
        response = request.execute()

        if 'items' in response and response['items']:
            return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return None
    except Exception as e:
        raise YTubeInsightError(
            f"Error fetching uploads playlist ID: {str(e)}") from e
