import streamlit as st

def main():

    audio_file = open('D:/data')
    st.audio(audio_file.read(), format='audio/mp3')

if __name__ == "__main__":
    main()