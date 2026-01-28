import whisper
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
modelo = whisper.load_model("tiny", device=device)

def transcrever_audio(caminho_audio):
    # fp16 só em GPU; Whisper/ffmpeg aceita .webm/.ogg/.wav
    resultado = modelo.transcribe(caminho_audio, language="pt", fp16=(device == "cuda"))
    return resultado.get("text", "")