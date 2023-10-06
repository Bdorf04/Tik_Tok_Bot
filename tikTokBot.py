from getStories import getStories
from getAudio import PYTTSX3saveAudios
from createVideos import createVideos

#after importing all the modules. We can finally use them all together in conjunction
url="https://www.reddit.com/r/relationships" 
storyList=getStories(url, 1)
PYTTSX3saveAudios(storyList, 150)
createVideos(storyList)
