from langchain_text_splitters import RecursiveCharacterTextSplitter
def split_transcript(transcript: str):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(transcript)

    return chunks