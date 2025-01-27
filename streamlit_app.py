import streamlit as st
import time

st.title("YouTube Video Timer")

# Initialize session state variables
if "start_time" not in st.session_state:
    st.session_state.start_time = None  # When the video starts
if "end_time" not in st.session_state:
    st.session_state.end_time = None  # When the video ends
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0  # Total elapsed time

# Simulate play/pause functionality with a checkbox
play_video = st.checkbox("Play Video")
if play_video:
    # Embed the YouTube player
    video_url = "https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"  # Replace with your video URL
    st.audio(video_url, autoplay=True)
    
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()  # Record start time

else:
    if st.session_state.start_time is not None:
        st.session_state.end_time = time.time()
        st.session_state.elapsed_time += st.session_state.end_time - st.session_state.start_time
        st.session_state.start_time = None  # Reset the start time once the video is paused

# Display the total elapsed time
if st.session_state.elapsed_time > 0:
    st.write(f"Video has been playing for {round(st.session_state.elapsed_time, 2)} seconds.")
else:
    st.write("Start the video via the toggle button.")

