#This will physically take the audio recordings and screenshots and overlay them onto a mincreat clip

from moviepy.editor import *
from mutagen.wave import WAVE
import random 

def createVideos(stories):
    for i, v in enumerate(stories):
        audio = WAVE(f"audios/audio{i}.mp3")
        audioLength = int(audio.info.length)
        
        videoStart = random.randint(10, 3500)
        videoClip = VideoFileClip("mineCraftGameplay.mp4").subclip(videoStart, videoStart+audioLength)
        audioclip = AudioFileClip(f"audios/audio{i}.mp3")

        new_audioclip = CompositeAudioClip([audioclip])
        videoClip.audio = new_audioclip
        videoClip.write_videofile(f"videos/redditClip{i}.mp4")


        #time to make it overlay images

def createVideosNoAudio(stories):
    for i, v in enumerate(stories):
        audio = WAVE(f"audios/audio{i}.mp3")
        audioLength = int(audio.info.length)
        
        videoStart = random.randint(10, 3500)
        videoClip = VideoFileClip("cake.mp4").subclip(videoStart, videoStart+audioLength)
        videoClip.write_videofile(f"videos/redditClip{i}.mp4")

        #time to make it overlay images