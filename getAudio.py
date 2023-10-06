#This will use the scripts and turn them into mp3 files of talking. You have a choice between using GTTS or PYTTSX3
import pyttsx3
from gtts import gTTS

def PYTTSX3saveAudios(stories, talking_speed):
    for i, v in enumerate(stories):
        engine=pyttsx3.init()
        voices=engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", talking_speed)
        engine.save_to_file(v, f"audios/audio{i}.mp3")
        engine.runAndWait()

def GTTSsaveAudios(stories):
    for i, v in enumerate(stories):
        speech = gTTS(text=v, lang='en', slow=False)
        speech.save(f"audios/audio{i}.mp3")
