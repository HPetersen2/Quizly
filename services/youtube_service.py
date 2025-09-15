import yt_dlp
import os

import yt_dlp
import os

def download_audio(url) -> str:
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        output_path = ydl.prepare_filename(info)
        return os.path.abspath(output_path)
