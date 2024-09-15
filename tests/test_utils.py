import unittest
from unittest.mock import patch, MagicMock
from ytubeinsight.utils import get_channel_id, get_uploads_playlist_id
from ytubeinsight.exceptions import YTubeInsightError

class TestUtils(unittest.TestCase):

    @patch('ytubeinsight.utils.requests.get')
    def test_get_channel_id_from_url(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '<html><body>Some HTML content</body></html>'
        mock_get.return_value = mock_response

        channel_id = get_channel_id('https://www.youtube.com/channel/UC1234567890')
        self.assertEqual(channel_id, 'UC1234567890')

    @patch('ytubeinsight.utils.requests.get')
    def test_get_channel_id_from_page_source(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '<html><body>"channelId":"UC0987654321"</body></html>'
        mock_get.return_value = mock_response

        channel_id = get_channel_id('https://www.youtube.com/user/somechannel')
        self.assertEqual(channel_id, 'UC0987654321')

    @patch('ytubeinsight.utils.requests.get')
    def test_get_channel_id_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = '<html><body>No channel ID here</body></html>'
        mock_get.return_value = mock_response

        channel_id = get_channel_id('https://www.youtube.com/user/somechannel')
        self.assertIsNone(channel_id)

    def test_get_uploads_playlist_id_success(self):
        mock_youtube = MagicMock()
        mock_youtube.channels().list().execute.return_value = {
            'items': [{'contentDetails': {'relatedPlaylists': {'uploads': 'UU1234567890'}}}]
        }

        playlist_id = get_uploads_playlist_id(mock_youtube, 'UC1234567890')
        self.assertEqual(playlist_id, 'UU1234567890')

    def test_get_uploads_playlist_id_failure(self):
        mock_youtube = MagicMock()
        mock_youtube.channels().list().execute.return_value = {'items': []}

        playlist_id = get_uploads_playlist_id(mock_youtube, 'UC1234567890')
        self.assertIsNone(playlist_id)

if __name__ == '__main__':
    unittest.main()