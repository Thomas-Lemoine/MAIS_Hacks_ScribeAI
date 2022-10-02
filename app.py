import streamlit as st
from youtube import *
from youtube import get_transcript
from extract import generate_all
from anki import generate_anki


st.set_page_config(layout="wide")

st.sidebar.markdown("<div><h1 style='display:inline-block'>EasyNotes</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This web app uses OpenAI’s new open-source Speech-to-text model to transcribe lectures (.MP3 or .MP4) or youtube videos, and brings video transcription, summarization tools as well as automatic Anki-cards creation.")
st.sidebar.markdown("To get started <ol><li>Enter the URL link or upload a file you wish to summarize</li> <li>Choose the compression level if you want to summarize and generating anki-notes.</li> <li>Choose what you want to do with your video.</li><li>Click on <i>Generate<i></li><li>Start learning!</li></ol>",unsafe_allow_html=True)

st.header("EasyNotes")
st.text("")
st.subheader("Upload Files Here!")
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


if st.button("Get File Transcript"):
    wfile = open('binary.mp4', 'wb')
    with open('binary.mp4', 'rb') as wfile:
        wfile.write(input_file)
    get_transcript(file=wfile)

st.text("")
st.subheader("Youtube URL")
input_url = st.text_input('Insert an URL here', value="")
if input_url != "":
    st.video(data=input_url)

st.subheader("Choose what you wish to do with your transcript!")
compression = st.slider("Choose a compression level", 1, 16)
transcript_check = st.checkbox("Transcript of video")
summary_check = st.checkbox('Summary of Transcript')
anki_check = st.checkbox('Anki notes on the transcript')

generate_check = st.button("Generate")
if generate_check:
    transcript_text = get_transcript(url=input_url)
    summary_text = ""
    if summary_check or anki_check:
        summary_text, term_text, desc_text = generate_all(transcript_text, compression)
    if transcript_check:
        st.subheader("Transcript of the video!")
        st.write(transcript_text)
    if summary_check:
        st.subheader("Summary of the Transcript")
        st.write(summary_text)
    if anki_check:
        # anki_title = st.text_input("What name do you want to give to your Anki deck?", value="")
        # create_anki_button = st.button("Create Anki Deck!")
        # if anki_title != "" and create_anki_button:
        generate_anki(term_text, desc_text, "GD1")
        # with open('GD1.apkg') as f:
        #     st.download_button("Download Anki file", f, filename="GD1.apkg")

    


# model_sizes = ['Small', 'Medium','Large']
# capacity = st.radio('Model Sizes for Transcript', model_sizes)


