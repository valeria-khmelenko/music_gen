import streamlit as st
import librosa
import numpy as np
import soundfile as sf

AUDIO_FILE = '/music/upload.wav'

def play_audio(audio_file):

    data, sr = librosa.load(audio_file)
    st.audio(data, sample_rate=sr) 

def main():
    st.title("Simple Audio Player")

    play_audio(AUDIO_FILE)

if __name__ == "__main__":
    main()