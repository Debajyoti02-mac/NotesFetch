from transcrib import transcrib_audio
## Testing 
text = transcrib_audio("audio.wav")
try:
    with open(file="transcrib.txt",mode='w') as f :
        result = f.write(text)
        print(f'its sucessfully created')
except Exception as e :
    print(str(e))
