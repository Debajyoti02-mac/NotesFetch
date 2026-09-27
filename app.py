import os

import streamlit as st
import yt_dlp

from pipeline import process_video


st.set_page_config(
    page_title="Video → Notes",
    page_icon="🎥"
)

st.title("🎥 Video → Notes Generator")

os.makedirs("temp", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

video_path = "temp/input_video.mp4"


option = st.radio(
    "Choose input method",
    ["Upload Video", "Video URL"]
)


# =====================================================
# UPLOAD VIDEO
# =====================================================

if option == "Upload Video":

    uploaded_file = st.file_uploader(
        "Upload your video",
        type=["mp4", "mov", "mkv", "avi"]
    )

    if uploaded_file is not None:

        try:

            # Remove previous video
            if os.path.exists(video_path):
                os.remove(video_path)

            with open(video_path, "wb") as file:
                file.write(uploaded_file.getbuffer())

            st.success("Video uploaded successfully!")

        except Exception as e:

            st.error(f"Upload failed: {e}")

        if st.button("Generate Notes"):

            try:

                with st.spinner("Generating notes..."):

                    notes_path = process_video(video_path)

                if not os.path.exists(notes_path):
                    raise Exception("Notes file was not created.")

                with open(
                    notes_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    notes = file.read()

                st.success("Notes generated!")

                st.markdown("## 📝 Generated Notes")
                st.markdown(notes)

                st.download_button(
                    "Download Notes",
                    notes,
                    "notes.txt",
                    "text/plain"
                )

            except Exception as e:

                st.error(f"Processing failed: {e}")


# =====================================================
# VIDEO URL
# =====================================================

else:

    video_url = st.text_input(
        "Paste YouTube URL",
        placeholder="https://youtu.be/YMAwgRwjEOQ"
    )

    if st.button("Generate Notes from URL"):

        if not video_url.strip():

            st.warning("Please enter a YouTube URL.")

        else:

            try:

                # Remove previous video
                if os.path.exists(video_path):
                    os.remove(video_path)

                with st.spinner("Downloading video..."):

                    ydl_opts = {
        "format": "best",
        "outtmpl": video_path,
        "noplaylist": True,
        "extractor_args": {
            "youtube": {
            "player_client": ["android"]
            }
        }
        }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_url.strip()])

                # Check download
                if not os.path.exists(video_path):
                    raise Exception(
                        "Video download completed, but the video file was not found."
                    )

                st.success("Video downloaded!")

                with st.spinner("Generating notes..."):

                    notes_path = process_video(video_path)

                if not os.path.exists(notes_path):
                    raise Exception("Notes file was not created.")

                with open(
                    notes_path,
                    "r",
                    encoding="utf-8"
                ) as file:

                    notes = file.read()

                st.success("Notes generated!")

                st.markdown("## 📝 Generated Notes")
                st.markdown(notes)

                st.download_button(
                    "Download Notes",
                    notes,
                    "notes.txt",
                    "text/plain"
                )

            except yt_dlp.utils.DownloadError as e:

                st.error(f"YouTube download failed: {e}")

            except Exception as e:

                st.error(f"Processing failed: {e}")