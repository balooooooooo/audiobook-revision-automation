import whisper
import json


def main():
    with open("config.json", "r") as f:
        CONFIG = json.load(f)
    print("Loading model...")
    model = whisper.load_model("large")
    audio = whisper.load_audio(CONFIG["audio_source"])

    print("Starting transcription...")
    result = model.transcribe(audio, language="cs")

    with open("result.txt", "w") as f:
        f.write(result["text"])

    print("Result exported to target folder.")


if __name__ == '__main__':
    main()
