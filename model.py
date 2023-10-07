import whisper
from torch.cuda import is_available

model = whisper.load_model("large")

audio = whisper.load_audio("C:/sources/prepisy/vanocni-povidky-ze-sumavy-klosterman/01_Vanoce_pod_snehem.mp3")
print("Starting transcribtion...")
result = model.transcribe(audio,language="cs")
print(result["text"])

with open("result.txt", "w") as f:
    f.write(result["text"])