import yt_dlp
import whisper
import os

tmp_filename = ""

URLS = ['https://www.youtube.com/watch?v=NFLOobHCs20']

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": tmp_filename,
    "quiet": True,
    "noplaylist": True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)

model = whisper.load_model("turbo")
result = model.transcribe("audio.mp3")
print(result["text"])
