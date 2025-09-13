import yt_dlp
import os

def download_audio(url, filename: str = "audiofile.mp3") -> str:

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": filename,
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        output_path = ydl.prepare_filename(info)
        base, ext = os.path.splitext(output_path)
        final_path = base + ".mp3"
        return os.path.abspath(final_path)
