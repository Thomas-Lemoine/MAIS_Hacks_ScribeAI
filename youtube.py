import pytube
from pydub import AudioSegment
import os

def url_to_mp3(video_url, audio_path):  
    data = pytube.YouTube(video_url)
    audio = data.streams.get_audio_only()
    video_path = audio.download("/".join(audio_path.split("/")[:-1]))

    audio_format = audio_path.split(".")[-1]
    AudioSegment.from_file(video_path).export(audio_path, format=audio_format)

    os.remove(video_path)

def mp4_to_mp3(video_path, audio_path):  
    audio_format = audio_path.split(".")[-1]
    AudioSegment.from_file(video_path).export(audio_path, format=audio_format)

# Vid url to mp3
video_url = 'https://youtu.be/qg4PchTECck'
audio_path = "/content/audio/audio_file.mp3"
url_to_mp3(video_url, audio_path)

# Vid mp4 to mp3
video_path = '/content/Gradient Descent in 3 minutes.mp4'
audio_path = "/content/audio/audio_file2.mp3"
mp4_to_mp3(video_path, audio_path)