#This will physically take the audio recordings and screenshots and overlay them onto a mincreat clip

from moviepy.editor import *
from mutagen.wave import WAVE
import random 


def create_videos(stories):
    for i, v in enumerate(stories):
        audio = WAVE(f"audios/audio{i}.mp3")
        audio_length = int(audio.info.length)
        
        video_start = random.randint(10, 3500)
        video_clip = VideoFileClip("mineCraftGameplay.mp4").subclip(video_start, video_start+audio_length)
        audioclip = AudioFileClip(f"audios/audio{i}.mp3")

        new_audioclip = CompositeAudioClip([audioclip])
        video_clip.audio = new_audioclip
        video_clip.write_videofile(f"videos/redditClip{i}.mp4")


def create_videos_no_audio(stories):
    for i, v in enumerate(stories):
        audio = WAVE(f"audios/audio{i}.mp3")
        audio_length = int(audio.info.length)
        
        video_start = random.randint(10, 3500)
        video_clip = VideoFileClip("cake.mp4").subclip(video_start, video_start+audio_length)
        video_clip.write_videofile(f"videos/redditClip{i}.mp4")