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



# Simulate play/pause functionality with a toggle
play_video = st.toggle("Play Video")

# Create a container for displaying the elapsed time
time_container = st.container()

if play_video:
    # Embed the YouTube player inside a container
    video_container = st.container()
    with video_container:
        video_url = "https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"  # Replace with your video URL
        st.video(video_url, autoplay=True)
    
    # Start time tracking when video is played
    if st.session_state.start_time is None:
        st.session_state.start_time = time.time()  # Record start time

else:
    if st.session_state.start_time is not None:
        st.session_state.end_time = time.time()
        st.session_state.elapsed_time += st.session_state.end_time - st.session_state.start_time
        st.session_state.start_time = None  # Reset the start time once the video is paused

# Update and display the total elapsed time
with time_container:
    if st.session_state.elapsed_time > 0:
        st.write(f"Video has been playing for {round(st.session_state.elapsed_time, 2)} seconds.")
        st.session_state.elapsed_time = 0
    else:
        st.write("Start the video via the toggle button.")
