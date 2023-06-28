import streamlit as st
from pdf2image import convert_from_path
import pdf2image
import os

def pdf_to_image(file_path, uploaded_path):
    images = convert_from_path(file_path)
    for i, image in enumerate(images):
        image.save(uploaded_path + "/" + str(i) + ".jpg", "JPEG")
    print('conversion complete')

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    bin_folder = "C:/st_bin"
    makedirs(bin_folder)

    st.title('PDF를 IMG파일로 변환')
    st.subheader('파일을 선택하세요')
    uploaded_file = st.file_uploader('pdf를 업로드하세요', type=['pdf'])
    
    if uploaded_file is not None:
        if st.button('파일 변환'):
            
            # pdf파일 이름의 폴더를 bin 폴더에 생성
            uploaded_pathname = str(uploaded_file.name[:-4])
            uploaded_path = bin_folder + "/" + uploaded_pathname

            makedirs(uploaded_path)
            with open(os.path.join(uploaded_path, uploaded_file.name), 'wb') as f:
                f.write(uploaded_file.getbuffer())

            uploaded_filepath = uploaded_path + "/" + uploaded_file.name
            pdf_to_image(uploaded_filepath, uploaded_path)
            st.subheader('성공적으로 변환했습니다.')

            if st.button('이미지 그룹화'):
                print("")

if __name__ == "__main__":
    main()