from getStories import get_stories
from getAudio import PYTTSX3_save_audios
from createVideos import create_videos


#after importing all the modules. We can finally use them all together in conjunction
url="https://www.reddit.com/r/relationships" 
story_list=get_stories(url, 1)
PYTTSX3_save_audios(story_list, 150)
create_videos(story_list)
