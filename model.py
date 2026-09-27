from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

def summarize(chunk: str):
    prompt = f"""
Summarize the following transcript into clear study notes.

Transcript:
{chunk}
"""

    response = llm.invoke(prompt)
    return response.content


def summarize_chunks(chunks):
    summaries = []

    for chunk in chunks:
        summary = summarize(chunk)
        summaries.append(summary)

    return summaries 

# Combine summary : 
def combine_summary(summaries):
    combine = "\n\n".join(summaries)
    
    prompt = f"""
Create one final set of clear study notes from these summaries.

Organize them with:
- Main concepts
- Key points
- Important details
- Final takeaway

Summaries:
{combine}
"""

    response = llm.invoke(prompt)
    return response.content

