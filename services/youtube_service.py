import yt_dlp
import tempfile
import os

def download_audio(url):
    # Erstelle ein temporäres Verzeichnis
    temp_dir = tempfile.mkdtemp()

    # Definiere den Ausgabepfad im temporären Verzeichnis
    outtmpl = os.path.join(temp_dir, '%(title)s.%(ext)s')

    ydl_opts = {
        "format": "bestaudio/best",  # Beste Audioqualität
        "outtmpl": outtmpl,  # Pfad zur temporären Datei
        "quiet": True,  # Kein Output
        "noplaylist": True,  # Keine Playlist herunterladen
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Gibt den Pfad zum heruntergeladenen Audio zurück
    # Hier kannst du auch eine Liste der heruntergeladenen Dateien zurückgeben
    downloaded_files = os.listdir(temp_dir)
    return os.path.join(temp_dir, downloaded_files[0])

# Beispiel:
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Beispiel URL
audio_path = download_audio(url)
print(f"Audio gespeichert unter: {audio_path}")
