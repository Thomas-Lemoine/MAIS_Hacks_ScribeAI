import pytube
from pydub import AudioSegment
import os
import whisper

def get_transcript(url=None, video_path=None):
    if url is None and video_path is None:
        raise ValueError("Either url or video_path must be specified")
    if video_path is None:
        data = pytube.YouTube(url)
        video = data.streams.get_highest_resolution()
        video_path = video.download("MAIS_Hacks_ScribeAI/videos")
        print("\nVideo Path") 
        print(video_path)
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