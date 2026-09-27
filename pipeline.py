# Imports
from extractor import extract_audio
from transcrib import transcrib_audio
from chunking import split_transcript
from model import summarize_chunks, combine_summary
from write_file import save_file


def process_video(video_path):

    audio_path = "temp/audio.wav"
    notes_path = "outputs/notes.txt"

    # 1. Video → Audio
    try:
        extract_audio(video_path, audio_path)
    except Exception as e:
        raise Exception(f"Audio extraction failed: {e}")

    # 2. Audio → Transcript
    try:
        transcript = transcrib_audio(audio_path)

        if not transcript.strip():
            raise Exception("No speech detected in the video.")

    except Exception as e:
        raise Exception(f"Transcription failed: {e}")

    # 3. Transcript → Chunks
    try:
        chunks = split_transcript(transcript)

        if not chunks:
            raise Exception("No transcript chunks were created.")

    except Exception as e:
        raise Exception(f"Chunking failed: {e}")

    # 4. Chunks → Summaries
    try:
        summaries = summarize_chunks(chunks)

        if not summaries:
            raise Exception("No summaries were generated.")

    except Exception as e:
        raise Exception(f"Summarization failed: {e}")

    # 5. Summaries → Final Notes
    try:
        final_notes = combine_summary(summaries)

        if not final_notes.strip():
            raise Exception("Final notes are empty.")

    except Exception as e:
        raise Exception(f"Final note generation failed: {e}")

    # 6. Save Notes
    try:
        save_file(final_notes, notes_path)
    except Exception as e:
        raise Exception(f"Saving notes failed: {e}")

    return notes_path