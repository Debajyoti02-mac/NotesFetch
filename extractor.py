import ffmpeg 
def extract_audio(video_path:str , audio_path:str):
    (
        ffmpeg.input(video_path).output(audio_path,ac=1,ar=16000)
        .overwrite_output()
        .run()
        
    )