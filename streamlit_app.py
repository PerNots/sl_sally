import streamlit as st
from streamlit_player import st_player
import time

st.title("YouTube Video Timer")

# Initialize start time in session state
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Embed the YouTube player
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL
playing = st_player(video_url, events=["onPlay"])

# Check if the video started playing
if playing and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# Display elapsed time
if st.session_state.start_time is not None:
    elapsed_time = round(time.time() - st.session_state.start_time, 2)
    st.write(f"Video has been playing for {elapsed_time} seconds.")
