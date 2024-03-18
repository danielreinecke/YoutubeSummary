from youtube_transcript_api import YouTubeTranscriptApi

video = input("Youtube Video Link: ")
video = video.split("=")
tests = YouTubeTranscriptApi.get_transcript(video[-1])
text = ""

for words in tests:
    if words != ("[Music]"):
        text += " ".join (i for i in words["text"].split() if i != "[Music]") + "\n"