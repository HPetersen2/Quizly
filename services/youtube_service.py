import yt_dlp

def download_audio(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "output.%(ext)s",
        "quiet": True,
        "noplaylist": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(url)
