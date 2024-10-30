import streamlit as st
import numpy as np

audio_file = open("/blob/main/music/upload.mp3", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mpeg")
