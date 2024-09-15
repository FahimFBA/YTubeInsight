import requests
from bs4 import BeautifulSoup
import re
from .exceptions import YTubeInsightError

def get_channel_id(url):
    """
    Extract the channel ID from a YouTube channel URL.
    
    :param url: YouTube channel URL
    :return: Channel ID
    """
    try:
        response = requests.get(url)
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
    except Exception as e:
        raise YTubeInsightError(f"Error extracting channel ID: {str(e)}")

def get_uploads_playlist_id(youtube, channel_id):
    """
    Get the uploads playlist ID for a YouTube channel.
    
    :param youtube: YouTube API client
    :param channel_id: YouTube channel ID
    :return: Uploads playlist ID
    """
    try:
        request = youtube.channels().list(
            part="contentDetails",
            id=channel_id
        )
        response = request.execute()
        
        if 'items' in response and len(response['items']) > 0:
            return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return None
    except Exception as e:
        raise YTubeInsightError(f"Error fetching uploads playlist ID: {str(e)}")