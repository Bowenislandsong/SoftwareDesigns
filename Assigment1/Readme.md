# The twitter image video API 
The API allows users to grab images from specified Twitter account and make them into a short video with related information tags.

Third party dependencies:
- [tweepy]{https://github.com/tweepy/tweepy}
- [PIL]{http://www.pythonware.com/products/pil/}

# API Feature:
- allow user to choose what video content is

- Allow user to specify theme of the video 

- resizeable video, allow passing size and time

- allow users to scan any account accessible via Twitter

The project includes:
 - img2video.py (Converts images to video)
 - twmager.py (Communicates with Twitter and grabs information from Twitter)
 - vision.py (Communicates with Google vision and put tags on to images)