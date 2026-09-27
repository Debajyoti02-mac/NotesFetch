video-notes/
│
├── .venv/
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
├── README.md
│
├── app.py                  # Streamlit UI
│
├── src/
│   ├── __init__.py
│   │
│   ├── video/
│   │   ├── __init__.py
│   │   └── extractor.py    # Video → audio
│   │
│   ├── transcription/
│   │   ├── __init__.py
│   │   └── whisper.py       # Audio → transcript
│   │
│   ├── llm/
│   │   ├── __init__.py
│   │   └── groq.py          # Groq LLM
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── chunking.py      # Transcript → chunks
│   │   └── summarizer.py    # Chunks → notes
│   │
│   └── graph/
│       ├── __init__.py
│       └── workflow.py      # LangGraph workflow
│
├── uploads/
├── outputs/
└── temp/