import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

st.sidebar.markdown("<div><img src='MAIS_Hacks_ScribeAI\images\ai.png' width=100 /><h1 style='display:inline-block'>Scribe AI</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This web app uses OpenAI’s new open-source Speech-to-text model to transcribe lectures (.MP3 or .MP4) or youtube videos, and brings question-answering, summarization tools as well as automatic Anki-cards creation.")
st.sidebar.markdown("To get started <ol><li>Enter the URL link or upload a file you wish to summarize</li> <li>Hit <i>Get Data</i>.</li> <li>Get analyzing</li></ol>",unsafe_allow_html=True)

input_url = st.text_input('Insert an URL here', value="")
if st.button('Get Data'):
    st.video(data=input_url)






file_types = ['Audio', 'Video']
files = st.radio('File Types', file_types)

if files == 'Audio':
    input_file = st.file_uploader("Choose your file")

    if input_file is not None:
        audio_bytes = input_file.read()
        st.audio(audio_bytes, format='audio/ogg')

elif files == "Video":
    input_file = st.file_uploader("Choose your file")

    if input_file is not None:
        video_bytes = input_file.read()
        st.video(video_bytes)




