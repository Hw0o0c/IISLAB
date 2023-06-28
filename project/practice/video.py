import streamlit as st
def main():
    video_file = open('D:/data/', 'rb')
    st.video(video_file)

if __name__ == "__main__":
    main()