import streamlit as st

st.title("YouTube Timer App")

# Display the timer if it starts
if "start_time" not in st.session_state:
    st.session_state.start_time = None

if st.session_state.start_time:
    elapsed_time = (st.time() - st.session_state.start_time) // 1000
    st.write(f"Video playing for {elapsed_time} seconds")

# JavaScript + HTML to embed the YouTube video and detect play event
youtube_html = """
<!DOCTYPE html>
<html>
  <body>
    <div id="player"></div>

    <script>
      // Load the YouTube Player API
      var tag = document.createElement('script');
      tag.src = "https://www.youtube.com/iframe_api";
      var firstScriptTag = document.getElementsByTagName('script')[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

      var player;
      var startTime = null;

      // Initialize the player
      function onYouTubeIframeAPIReady() {
        player = new YT.Player('player', {
          height: '360',
          width: '640',
          videoId: 'koMp3ei4xJw', // Replace with your YouTube Video ID
          events: {
            'onStateChange': onPlayerStateChange
          }
        });
      }

      // Handle state changes
      function onPlayerStateChange(event) {
        if (event.data == YT.PlayerState.PLAYING && startTime === null) {
          startTime = Date.now();
          // Notify Streamlit
          const streamlitMsg = JSON.stringify({type: 'video_started', timestamp: startTime});
          window.parent.postMessage(streamlitMsg, '*');
        }
      }

      // Post messages back to Streamlit
      window.addEventListener('message', (event) => {
        const streamlitResponse = JSON.stringify(event.data);
        console.log(streamlitResponse);
        window.parent.Streamlit.setComponentValue(streamlitResponse);
      });
    </script>
  </body>
</html>
"""

# Embed YouTube with custom HTML
st.components.v1.html(youtube_html, height=400)



