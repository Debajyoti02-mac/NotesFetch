# Imports 
from extractor import extract_audio 
from transcrib import transcrib_audio 
from chunking import split_transcript 
from model import summarize_chunks , combine_summary 
from write_file import save_file 

def process_video(video_path):
    audio_path = "temp/audio.wav"
    notes_path = "outputs/notes.txt"

    # 1. Video → Audio
    extract_audio(video_path, audio_path)

    # 2. Audio → Transcript
    transcript = transcrib_audio(audio_path)

    # 3. Transcript → Chunks
    chunks = split_transcript(transcript)

    # 4. Chunks → Summaries
    summaries = summarize_chunks(chunks)

    # 5. Summaries → Final Notes
    final_notes = combine_summary(summaries)

    # 6. Save Notes
    save_file(final_notes, notes_path)

    return notes_path
