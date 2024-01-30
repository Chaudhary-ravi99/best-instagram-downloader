import os
from dotenv import load_dotenv

# we use dotenv to use os.getenv() instead of os.environ[]
# and read from '.env' in current folder instead of '/etc/environment'
# more guide:
# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
load_dotenv()

# instagram user for instaloader
USER = os.getenv('test36640') # to read from .env file
PASS = os.getenv('ravi07yt')

# env variables
bot_token = os.getenv('6619643339:AAEWe8OGFrKyYXGxVZW4LsvUGsUCP8aRRUI')
log_channel_id = os.getenv('-1001890206806') # set to False if not needed

# settings
bot_username = "@Best_Instagram_Downloader_Bot"
caption_trail = "\n\n\n" + bot_username
session_file_name = "session" # any name change should apply to .gitignore too

# regex
insta_post_or_reel_reg = r'(?:https?://www\.)?instagram\.com\S*?/(p|reel)/([a-zA-Z0-9_-]{11})/?'

# messages
start_msg = '''Welcome :)
Send a post link to download.'''

help_msg = '''This bot is open source and you are welcome to contribute and improve it.
https://github.com/arashnm80/best-instagram-downloader

You can give me energy by giving a star in github :)'''

end_msg = '''You can use my *Spotify Downloader* too: @SpotSeekBot

Subscribe to [My YouTube](https://www.youtube.com/@Arashnm80) for more🔥'''

fail_msg = '''Sorry, my process wasn't successful.
But you can try again another time or with another link.'''

wrong_pattern_msg = '''wrong pattern.
Currently only post links are supported.

Motivate me to add support of reels and stories by subscribing to [my youtube](https://www.youtube.com/@Arashnm80)'''

reel_msg = '''reel links are not supported at the moment.
You can send post links instead.

Motivate me to add support of reels and stories by subscribing to [my youtube](https://www.youtube.com/@Arashnm80)'''
