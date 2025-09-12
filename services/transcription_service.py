import whisper

def transcribe_audio(audio_file):
    model = whisper.load_model("medium")
    result = model.transcribe(audio_file)
    print(result["text"])
    return result["text"]