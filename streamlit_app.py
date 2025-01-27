import streamlit as st
from streamlit_player import st_player
import time

st.title("YouTube Video Timer")

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = None  # When the video starts
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0  # Total time video has been playing
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False  # Whether the video is currently playing

# Embed the YouTube player and listen for play/pause events
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL
events = st_player(video_url, events=["onPlay", "onPause"])

# Handle play event
if events == "onPlay":
    if not st.session_state.is_playing:
        st.session_state.start_time = time.time()  # Record start time
        st.session_state.is_playing = True

# Handle pause event
if events == "onPause":
    if st.session_state.is_playing:
        # Calculate elapsed time and accumulate
        st.session_state.elapsed_time += time.time() - st.session_state.start_time
        st.session_state.start_time = None
        st.session_state.is_playing = False

# Update elapsed time if video is playing
if st.session_state.is_playing:
    st.session_state.elapsed_time += time.time() - st.session_state.start_time
    st.session_state.start_time = time.time()  # Reset start_time to current

# Display the total elapsed time
st.write(f"Video has been playing for {round(st.session_state.elapsed_time, 2)} seconds.")
