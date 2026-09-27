from faster_whisper  import WhisperModel 
model = WhisperModel("base",compute_type="int8")

def transcrib_audio(audip_path:str):
    segments , info = model.transcribe(audip_path)
    transcrib = ""
    
    for segment in segments :
        transcrib+=segment.text+''
    return transcrib.strip() 