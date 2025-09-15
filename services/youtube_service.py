import yt_dlp
import os

def download_audio(url) -> str:
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        "format": "m4a/bestaudio/best",
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
        base, ext = os.path.splitext(output_path)
        final_path = base + ".mp3"
        return os.path.abspath(final_path)
