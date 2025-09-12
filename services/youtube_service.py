import yt_dlp
import tempfile
import os

def download_audio(url):
    temp_dir = tempfile.mkdtemp()

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download([url])

    downloaded_files = os.listdir(temp_dir)
    print(downloaded_files)
    if downloaded_files:
        return os.path.join(temp_dir, downloaded_files[0])
    else:
        return None
