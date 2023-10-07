# TikTok_Bot
## By Brett Dorfman
### CS @ NJIT

This tiktok bot automatically scrapes stories from reddit, voices it, and combines it with a randomy generated Minecraft clip. 

---

## How to use the bot

1. Download Python [here](https://www.python.org/downloads/)

2. Download Selenium [here](https://pypi.org/project/selenium/)

3. Download a webdriver. I use the chrome Webdriver, attached [here](https://chromedriver.chromium.org/downloads). Keep in mind, some selenium versions and webdrivers force you to set up a path, but the newest selenium and webdriver versions do it automatically. 

4. Clone this repository by typing
    `git clone https://github.com/Bdorf04 Tik_Tok_Bot.git `


## How does it work
The code is split into multiple files, each which must be customized

* The audio/video files
    
   > These files are where we store our videos and audios

* createVideos.py
   > within this file, we need to specify which video we are going to create our clips from. In here my file is
    ``` python
    video_clip = VideoFileClip("mineCraftGameplay.mp4").subclip(video_start, video_start+audio_length)
    ```
    You can name this file whatever you want, but made sure it is inside the folder your code is in
* getAudio.py

    > This is where we turn the stories into audio files
* getStories.py
    
     > This is where we pull the stories from reddit, the function takes 2 variables. The first is our url, and the second is the number of videos we would like to create

    ``` python
    #This code makes 10 videos from the r/relationships reddit
    url="https://www.reddit.com/r/relationships" 
    story_list=get_stories(url, 10)
    ```
---
Finally, we bring all the files together, finishing our tiktok bot!

``` python

from getStories import get_stories
from getAudio import PYTTSX3_save_audios
from createVideos import create_videos


#after importing all the modules. We can finally use them all together in conjunction
url = "https://www.reddit.com/r/TIFU" 
story_list=get_stories(url, 1)
PYTTSX3_save_audios(story_list, 150)
create_videos(story_list)

```
