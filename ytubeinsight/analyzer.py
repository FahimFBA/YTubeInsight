"""Module for analyzing YouTube channels and extracting video data."""

from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .utils import get_channel_id, get_uploads_playlist_id
from .exceptions import YTubeInsightError


def analyze_channel(channel_input, api_key, is_channel_id=False):
    """
    Analyze a YouTube channel and return video data for the past year.

    Args:
        channel_input (str): Either a full channel URL or channel ID
        api_key (str): YouTube Data API key
        is_channel_id (bool): Indicates if channel_input is a channel ID

    Returns:
        dict: Contains video count and list of video data

    Raises:
        YTubeInsightError: If any error occurs during the analysis process
    """
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        channel_id = channel_input if is_channel_id else get_channel_id(
            channel_input)

        if not channel_id:
            raise YTubeInsightError(
                "Unable to extract channel ID. Please check the input.")

        uploads_playlist_id = get_uploads_playlist_id(youtube, channel_id)

        if not uploads_playlist_id:
            raise YTubeInsightError(
                "Unable to fetch channel's uploads playlist.")

        return fetch_video_data(youtube, uploads_playlist_id)

    except HttpError as e:
        raise YTubeInsightError(f"YouTube API error: {str(e)}") from e
    except Exception as e:
        raise YTubeInsightError(
            f"An error occurred during analysis: {str(e)}") from e


def fetch_video_data(youtube, uploads_playlist_id):
    """
    Fetch video data for the past year from the given uploads playlist.

    Args:
        youtube: YouTube API client
        uploads_playlist_id (str): ID of the uploads playlist

    Returns:
        dict: Contains video count and list of video data
    """
    today = datetime.now()
    one_year_ago = today - timedelta(days=365)
    video_count = 0
    video_data = []
    next_page_token = None

    while True:
        # pylint: disable=no-member
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            published_at = datetime.strptime(
                item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            if published_at > one_year_ago:
                video_count += 1
                video_data.append({
                    'title': item['snippet']['title'],
                    'published_at': published_at.strftime("%Y-%m-%d"),
                    'url': (f"https://www.youtube.com/watch?v="
                            f"{item['snippet']['resourceId']['videoId']}")
                })
            else:
                return {
                    'video_count': video_count,
                    'video_data': video_data
                }

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return {
        'video_count': video_count,
        'video_data': video_data
    }
