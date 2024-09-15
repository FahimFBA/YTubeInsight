Usage
=====

Installation
------------

You can install YTubeInsight using pip:

.. code-block:: bash

    pip install ytubeinsight

Basic Usage
-----------

Here's a simple example of how to use YTubeInsight:

.. code-block:: python

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

    # Analyze a channel by ID
    channel_id = 'UCJFp8uSYCjXOMnkUyb3CQ3Q'
    result = analyze_channel(channel_id, API_KEY, is_channel_id=True)

    print(f"Videos published in the last year: {result['video_count']}")

API Reference
-------------

.. autofunction:: ytubeinsight.analyze_channel

Exceptions
----------

.. autoexception:: ytubeinsight.YTubeInsightError
   :members:
