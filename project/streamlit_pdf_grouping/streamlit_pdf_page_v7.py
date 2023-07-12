import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
from streamlit_cropper import st_cropper
import numpy as np
import shutil
import os

if 'r_path' not in st.session_state:
    st.session_state.r_path = ""

st.set_option('deprecation.showfileUploaderEncoding', False)

#-------------------------------------------------------------------------------- 반환을 안하는 함수

def pdf_to_image(file_path, uploaded_path):
    images = convert_from_path(file_path)
    for i, image in enumerate(images):
        image.save(uploaded_path + "/" + str(i+1) + ".jpg", "JPEG")

def save_image(file_path, img):
    img.save(file_path + "/" + str(folder_count(file_path) + 1) + ".jpg", "JPEG")

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
#--------------------------------------------------------------------------------- 반환을 하는 함수
def show_image(file_path, index):
    file = file_path + "/" + str(index) + ".jpg"
    return file

def folder_count(path):
    file_list = os.listdir(path)
    file_count = len(file_list) - 1
    return file_count
#----------------------------------------------------------------------------------

def main():
    st.sidebar.subheader('파일을 선택하세요')
    uploaded_file = st.sidebar.file_uploader("pdf파일을 선택하세요.", type=['pdf'])

    bin_folder = "C:/st_bin"

    makedirs(bin_folder)
    if not uploaded_file:
        return None
    
    folder_path = bin_folder + "/" + str(uploaded_file.name[:-4])             #C:/st_bin/파일이름
    image_path = folder_path + "/img"                                    #C:/st_bin/read_pdf/img
    group_path = folder_path + "/group"

    makedirs(folder_path)
    makedirs(image_path)

    with open(os.path.join(image_path, uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    uploaded_filepath = image_path + "/" + uploaded_file.name              #C/st_bin/파일이름/image/파일이름.pdf
    pdf_to_image(uploaded_filepath, image_path)
    
    if folder_count(image_path) > 1: 
        num_page = st.sidebar.slider("page", min_value=1, max_value=folder_count(image_path))
        img = Image.open(show_image(image_path, num_page))

    elif folder_count(image_path) == 1:
        img = Image.open(show_image(image_path, 1))
    
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

    ori, preview = st.columns([0.75,0.25])
    with ori:
        rect = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                        aspect_ratio=aspect_ratio, return_type='box', key='coordination')
        raw_image = np.asarray(img).astype('uint8')
        left, top, width, height = tuple(map(int, rect.values()))

        masked_image = np.zeros(raw_image.shape, dtype='uint8')
        masked_image[top:top + height, left:left + width] = raw_image[top:top + height, left:left + width]
    
    with preview:
        preview_img = Image.fromarray(masked_image)
        st.image(preview_img, caption='masked image')
        st.write(rect)
    
    btA, btB, btC, empty1 = st.columns([0.25, 0.25, 0.25, 0.25])

    ##버튼을 눌렀을 때 특정 폴더에 캡처한 파일을 저장함.

    with btA:
        group_A = st.button("Group A")
    with btB:
        group_B = st.button("Group B") 
    with btC:
        group_C = st.button("Group C")
    with empty1:
        st.write("")
    
    print(st.session_state.r_path)
    
    if group_A:
            st.session_state.r_path = "A"
            download_path = group_path + "/A"
            makedirs(download_path)
            save_image(download_path, preview_img)
            btA.success('성공적으로 추출했습니다.')

    elif group_B:
            st.session_state.r_path = "B"
            download_path = group_path + "/B"
            makedirs(download_path)
            save_image(download_path, preview_img)
            btB.success('성공적으로 추출했습니다.')

    elif group_C:
            st.session_state.r_path = "C"
            download_path = group_path + "/C"
            makedirs(download_path)
            save_image(download_path, preview_img)
            btC.success('성공적으로 추출했습니다.')

    remove_all = st.sidebar.button("그룹 초기화")
    remove_recently = st.sidebar.button('그룹 단일 추출 개체 삭제')

    if remove_all:
        shutil.rmtree(group_path)
        makedirs(group_path)
    
    if remove_recently:
        r_path = group_path + "/" + st.session_state.r_path
        if (not st.session_state.r_path) or (not os.path.exists(r_path)) or (folder_count(r_path) < 0):
            st.info(st.session_state.r_path + "에 파일이 존재하지 않습니다.")
        else:
            recently_file = group_path + "/" + st.session_state.r_path + "/" +str(folder_count(r_path)) +".jpg"
            os.remove(recently_file)
            st.success("삭제 완료")

if __name__ == "__main__":
    main()