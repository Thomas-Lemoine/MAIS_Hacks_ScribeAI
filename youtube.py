import pytube
from pydub import AudioSegment
from pydub.playback import play
import os
import whisper
import pickle
import io

def get_transcript(url=None, video_path=None, file=None):
    if url is None and video_path is None and file is None:
        raise ValueError("Either url or video_path must be specified")
    if url is not None:
        data = pytube.YouTube(url)
        video = data.streams.get_highest_resolution()
        video_path = video.download("MAIS_Hacks_ScribeAI/videos")
        print("\nVideo Path") 
        print(video_path)
    elif file is not None:
        # recording = AudioSegment.from_file(file, format="mp3")
        # recording.export("temp.mp3", format="mp3")
        video_path = file
    model = whisper.load_model("base.en")
    result = model.transcribe(video_path, language='english')
    os.remove(video_path)
    return result["text"]

# Vid url to transcript
# video_url = 'https://www.youtube.com/watch?v=zhWDdy_5v2w&ab_channel=AsapSCIENCE'
# print(get_transcript(url=video_url))

# Vid mp4 to transcript
# video_path = '/content/Gradient Descent in 3 minutes.mp4'
# transcript = get_transcript(video_path=video_path)