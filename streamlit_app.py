import streamlit as st
import time

st.title("YouTube Video Timer")

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = None  # When the video starts
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0  # Total time video has been playing
if "is_playing" not in st.session_state:
    st.session_state.is_playing = False  # Whether the video is currently playing

# Simulate play/pause functionality with a checkbox
play_video = st.checkbox("Play Video")

# Embed the YouTube player
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Replace with your video URL
st.video(video_url)

# Handle play event
if play_video and not st.session_state.is_playing:
    st.session_state.start_time = time.time()  # Record start time
    st.session_state.is_playing = True

# Handle pause event
if not play_video and st.session_state.is_playing:
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
