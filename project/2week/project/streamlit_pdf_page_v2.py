import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
from streamlit_cropper import st_cropper
import os

st.set_option('deprecation.showfileUploaderEncoding', False)

def pdf_to_image(file_path, uploaded_path):
    images = convert_from_path(file_path)
    for i, image in enumerate(images):
        image.save(uploaded_path + "/" + str(i+1) + ".jpg", "JPEG")

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def show_image(file_path, index):
    file = file_path + "/" + str(index) + ".jpg"
    return file

def folder_count(folder_path):
    file_list = os.listdir(folder_path)
    file_count = len(file_list) - 1
    return file_count

def main():
    st.title('PDF를 IMG파일로 변환')
    st.sidebar.subheader('파일을 선택하세요')
    uploaded_file = st.sidebar.file_uploader("pdf파일을 선택하세요.", type=['pdf'])
    bin_folder = "C:/st_bin"
    
    makedirs(bin_folder)
    if not uploaded_file:
        return None
    
    folder_pathname = str(uploaded_file.name[:-4])                              #업로드 파일이름(.pdf X)
    folder_path = bin_folder + "/" + folder_pathname                            #C:/st_bin/파일이름

    convert_button = st.sidebar.button("파읿 변환")

    if convert_button:
        if not uploaded_file:
            return None
        
        makedirs(folder_path)
        with open(os.path.join(folder_path, uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
        uploaded_filepath = folder_path + "/" + uploaded_file.name              #C/st_bin/파일이름/파일이름.pdf
            
        pdf_to_image(uploaded_filepath, folder_path)
        st.success('성공적으로 변환했습니다.')
    
    if folder_count(folder_path) > 1: 
        num_page = st.sidebar.slider("page", min_value=1, max_value=folder_count(folder_path)-1)
        if folder_count(folder_path) >= num_page:
            img = Image.open(show_image(folder_path, num_page))
        else:
            st.error("페이지 수를 수정해주세요.")
    elif folder_count(folder_path) == 1:
        img = Image.open(show_image(folder_path, 1))

    realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
    box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
    aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
    aspect_dict = {
        "1:1": (1, 1),
        "16:9": (16, 9),
        "4:3": (4, 3),
        "2:3": (2, 3),
        "Free": None
    }
    aspect_ratio = aspect_dict[aspect_choice]

    if not realtime_update:
        st.write("Double click to save crop")
    cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                                aspect_ratio=aspect_ratio)
    _ = cropped_img.thumbnail
    st.image(cropped_img, caption="Preview")

if __name__ == "__main__":
    main()

    