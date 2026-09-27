
from chunking import split_transcript 
from model import summarize , combine_summary
from write_file import save_file
with open('transcrib.txt','r') as f :
    transcrib = f.read()
    
chunking = split_transcript(transcrib)
summary = summarize(chunking)

final_notes = combine_summary(summary)

save_file(final_notes, "outputs/notes.txt")