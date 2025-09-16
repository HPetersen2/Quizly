import os
import json
from .youtube_service import download_audio
from .transcription_service import transcribe_audio
from .ai_service import generate_quiz


def create_quiz_from_video(video_url: str):
    if os.path.exists('./media/audiofile.m4a'):
        os.remove('./media/audiofile.m4a')
    audio_file = download_audio(video_url)
    transcript = transcribe_audio(audio_file)
    quiz = generate_quiz(transcript)
    data = json.loads(quiz)
    os.remove('./media/audiofile.m4a')
    return data
