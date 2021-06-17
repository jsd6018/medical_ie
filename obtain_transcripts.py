import pandas as pd
import numpy as np
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

data = pd.read_csv('input/medical_youtube - metadata.csv')
key = data['S.No'].astype('str').tolist()
url = data['Link of the Video'].tolist()
video_id = [(s.split('?v='))[1] for s in url]

for i in range(len(video_id)):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id[i])
        formatter = TextFormatter()
        text = formatter.format_transcript(transcript)
        print("=========== FILE ", i + 1, " ===========")
        f = open("output/video" + key[i] + ".txt", 'w')
        f.write(text)
    except Exception:
        pass
