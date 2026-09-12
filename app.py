import streamlit as st
from pipeline import SpeechToSpeechPipeline

st.set_page_config(page_title="Speech-to-Speech AI", layout="wide")
st.title("🎙️ Real-time Speech-to-Speech AI Pipeline")
st.caption("Sub-500ms streaming pipeline combining Whisper STT, Llama-3, and XTTS-v2.")

if st.button("Start Voice Streaming Session"):
    s2s = SpeechToSpeechPipeline()
    res = s2s.process_audio_stream("dummy_audio")
    st.success(res)
