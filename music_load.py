import streamlit as st
import numpy as np

audio_file = open("https://github.com/valeria-khmelenko/music_gen/blob/main/music/upload.wav", "rb")
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/wav")
