import streamlit as st
from streamlit_player import st_player

st.title("YouTube Video Timer")

# Initialize start time
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# Embed the YouTube player
video_url = "https://www.youtube.com/watch?v=koMp3ei4xJw"  # Replace with your video URL
playing = st_player(video_url, events=["onPlay"])

# Check if the video started playing
if playing and st.session_state.start_time is None:
    st.session_state.start_time = st.time()

# Display elapsed time
if st.session_state.start_time is not None:
    elapsed_time = round(st.time() - st.session_state.start_time, 2)
    st.write(f"Video has been playing for {elapsed_time} seconds.")
