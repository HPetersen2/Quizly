from youtube_service import download_audio
from transcription_service import transcribe_audio
from ai_service import generate_quiz

def create_quiz_from_video(video_url: str):
    audio_file = download_audio(video_url)
    transcript = transcribe_audio(audio_file)
    quiz = generate_quiz(transcript)
    return quiz

create_quiz_from_video("https://www.youtube.com/watch?v=5FUPEWn241M")