# 🎥 Video → Notes Generator

A Python application that converts videos into structured study notes using **faster-whisper** for transcription and **Groq** for summarization.

## Features

* Upload a video file
* Paste a YouTube video URL
* Extract audio using FFmpeg
* Transcribe audio using faster-whisper
* Split long transcripts into chunks
* Summarize each chunk using Groq
* Combine summaries into final notes
* Display notes in Streamlit
* Download generated notes as a `.txt` file
* Basic error handling

## Architecture

```text
Video / YouTube URL
        ↓
     yt-dlp
        ↓
      FFmpeg
        ↓
 faster-whisper
        ↓
    Transcript
        ↓
     Chunking
        ↓
       Groq
        ↓
 Chunk Summaries
        ↓
   Final Notes
        ↓
    Streamlit
        ↓
 Display / Download
```

## Tech Stack

* Python
* Streamlit
* FFmpeg
* ffmpeg-python
* faster-whisper
* LangChain
* LangChain Groq
* Groq
* yt-dlp
* python-dotenv
* uv

## Project Structure

```text
Video to notes generate/
│
├── app.py
├── pipeline.py
├── extractor.py
├── transcrib.py
├── chunking.py
├── model.py
├── write_file.py
│
├── temp/
├── outputs/
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Installation

Clone the project and install the dependencies:

```bash
uv sync
```

Make sure FFmpeg is installed on your system.

For macOS:

```bash
brew install ffmpeg
```

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit `.env` to GitHub.

## Run the Application

Start Streamlit:

```bash
uv run streamlit run app.py
```

The application will open in your browser.

## Usage

### Upload Video

1. Select **Upload Video**
2. Upload an MP4, MOV, MKV, or AVI file
3. Click **Generate Notes**
4. Read or download the generated notes

### YouTube URL

1. Select **Video URL**
2. Paste a YouTube URL
3. Click **Generate Notes from URL**
4. The application downloads and processes the video
5. Read or download the generated notes

## Output

Generated notes are saved to:

```text
outputs/notes.txt
```

Temporary audio and downloaded videos are stored in:

```text
temp/
```

## Current Limitations

* Transcription quality depends on audio quality.
* Long videos require more processing time.
* YouTube availability can vary depending on the video and `yt-dlp`.
* The current version generates notes but does not provide RAG-based question answering.
* The application currently uses a local processing pipeline.

## Future Improvements

* RAG-based Q&A over video content
* Better transcript cleaning
* Timestamp-based notes
* Multiple output formats such as PDF and Markdown
* Improved UI
* Cloud deployment
* More robust video URL support

## License

This project is for educational and development purposes.
