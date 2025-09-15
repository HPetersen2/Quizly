import whisper

def transcribe_audio(audio_file):
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_file)
    return result["text"]