import streamlit as st
from PIL import Image

def main() :
    img = Image.open('D:/data/banana.jpeg')
    st.image(img)

    url = 'https://i.kym-cdn.com/entries/icons/mobile/000/035/692/cover1.jpg'
    st.image(url)
    st.text('사진출처 : https://knowyourmeme.com/memes/pop-cat')

if __name__ == "__main__":
    main()