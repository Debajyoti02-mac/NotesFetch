import os

import streamlit as st

from pipeline import process_video


st.set_page_config(
    page_title="Video → Notes",
    page_icon="🎥"
)

st.title("🎥 Video → Notes Generator")

os.makedirs("temp", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

video_path = "temp/input_video.mp4"


# =====================================================
# UPLOAD VIDEO
# =====================================================

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


# =====================================================
# GENERATE NOTES
# =====================================================

if uploaded_file is not None:

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
