from datetime import datetime, timedelta
from googleapiclient.discovery import build
from .utils import get_channel_id, get_uploads_playlist_id
from .exceptions import YTubeInsightError

def analyze_channel(channel_input, api_key, is_channel_id=False):
    """
    Analyze a YouTube channel and return video data for the past year.
    
    :param channel_input: Either a full channel URL or channel ID
    :param api_key: YouTube Data API key
    :param is_channel_id: Boolean indicating if channel_input is a channel ID
    :return: Dictionary containing video count and list of video data
    """
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        
        if is_channel_id:
            channel_id = channel_input
        else:
            channel_id = get_channel_id(channel_input)
        
        if not channel_id:
            raise YTubeInsightError("Unable to extract channel ID. Please check the input.")
        
        uploads_playlist_id = get_uploads_playlist_id(youtube, channel_id)
        
        if not uploads_playlist_id:
            raise YTubeInsightError("Unable to fetch channel's uploads playlist.")
        
        today = datetime.now()
        one_year_ago = today - timedelta(days=365)

        video_count = 0
        video_data = []
        next_page_token = None

        while True:
            request = youtube.playlistItems().list(
                part="snippet",
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            )
            response = request.execute()

            for item in response['items']:
                published_at = datetime.strptime(item['snippet']['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
                if published_at > one_year_ago:
                    video_count += 1
                    video_data.append({
                        'title': item['snippet']['title'],
                        'published_at': published_at.strftime("%Y-%m-%d"),
                        'url': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}"
                    })
                else:
                    break

            next_page_token = response.get('nextPageToken')
            if not next_page_token or published_at <= one_year_ago:
                break

        return {
            'video_count': video_count,
            'video_data': video_data
        }
    
    except Exception as e:
        raise YTubeInsightError(f"An error occurred during analysis: {str(e)}")