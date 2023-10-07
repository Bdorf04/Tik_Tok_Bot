# TikTok_Bot
## By Brett Dorfman
### CS @ NJIT

This tiktok bot automatically scrapes stories from reddit, voices it, and combines it with a randomy generated mincraft clip. 

---

## How to use

1. Downlaod Python [Here](https://www.python.org/downloads/)

2. Downlaod Selenium [Here](https://pypi.org/project/selenium/)

3. Download a webdriver. I use the chrome Webdriver, attached [Here](https://chromedriver.chromium.org/downloads). Keep in mind, some selenium versions and webdrivers force you to set up a path, but the newest selenium and webdriver versions do it automatically. 

4. Clone this repository by typing
    'git clone https://github.com/Bdorf04 Tik_Tok_Bot.git'


The code is split into multiple files

* createVideos.py
* getAudio.py
* getStories.py

We bring all the filed together in tikTokBot.py

``` python

from getStories import get_stories
from getAudio import PYTTSX3_save_audios
from createVideos import create_videos


#after importing all the modules. We can finally use them all together in conjunction
url="https://www.reddit.com/r/relationships" 
story_list=get_stories(url, 1)
PYTTSX3_save_audios(story_list, 150)
create_videos(story_list)

```
