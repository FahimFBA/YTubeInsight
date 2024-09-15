"""Test module for the analyzer functionality of YTubeInsight."""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from ytubeinsight.analyzer import analyze_channel
from ytubeinsight.exceptions import YTubeInsightError

class TestAnalyzer(unittest.TestCase):
    """Test cases for the analyze_channel function."""

    @patch('ytubeinsight.analyzer.build')
    @patch('ytubeinsight.analyzer.get_channel_id')
    @patch('ytubeinsight.analyzer.get_uploads_playlist_id')
    @patch('ytubeinsight.analyzer.datetime')
    def test_analyze_channel_success(self, mock_datetime, mock_get_uploads,
                                     mock_get_channel_id, mock_build):
        """Test successful channel analysis."""
        # Mock the current date
        mock_now = datetime(2023, 6, 1)
        mock_datetime.now.return_value = mock_now
        mock_datetime.strptime.side_effect = datetime.strptime

        # Mock the YouTube API client
        mock_youtube = MagicMock()
        mock_build.return_value = mock_youtube

        # Mock channel ID and uploads playlist ID
        mock_get_channel_id.return_value = 'UC1234567890'
        mock_get_uploads.return_value = 'UU1234567890'

        # Mock the YouTube API response
        mock_response = {
            'items': [
                {
                    'snippet': {
                        'publishedAt': '2023-01-01T00:00:00Z',
                        'title': 'Test Video',
                        'resourceId': {'videoId': 'abc123'}
                    }
                },
                {
                    'snippet': {
                        'publishedAt': '2022-01-01T00:00:00Z',
                        'title': 'Old Video',
                        'resourceId': {'videoId': 'def456'}
                    }
                }
            ]
        }
        mock_youtube.playlistItems().list().execute.return_value = mock_response

        result = analyze_channel('https://www.youtube.com/channel/UC1234567890', 'fake_api_key')

        self.assertEqual(result['video_count'], 1)
        self.assertEqual(len(result['video_data']), 1)
        self.assertEqual(result['video_data'][0]['title'], 'Test Video')

    def test_analyze_channel_invalid_input(self):
        """Test channel analysis with invalid input."""
        with self.assertRaises(YTubeInsightError):
            analyze_channel('invalid_input', 'fake_api_key')

if __name__ == '__main__':
    unittest.main()