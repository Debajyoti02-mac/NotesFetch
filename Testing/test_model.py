from chunking import split_transcript
from model import summarize_chunks, combine_summary

with open("transcrib.txt", "r", encoding="utf-8") as file:
    transcript = file.read()

chunks = split_transcript(transcript)

summaries = summarize_chunks(chunks)

final_notes = combine_summary(summaries)

print("\n===== FINAL NOTES =====")
print(final_notes)