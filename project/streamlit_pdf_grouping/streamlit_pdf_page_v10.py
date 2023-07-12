import streamlit as st
from pdf2image import convert_from_path
from PIL import Image
from streamlit_cropper import st_cropper
import cv2
import numpy as np
import shutil
import os

if 'page' not in st.session_state:
    st.session_state.page = 0

if 'coord' not in st.session_state:
    st.session_state.coord = {}

if 'A' not in st.session_state:
    st.session_state.A = {}

if 'B' not in st.session_state:
    st.session_state.B = {}

if 'C' not in st.session_state:
    st.session_state.C = {}


st.set_option('deprecation.showfileUploaderEncoding', False)

#-------------------------------------------------------------------------------- 반환을 안하는 함수
def pdf_to_image(file_path, uploaded_path):
    images = convert_from_path(file_path)
    for i, image in enumerate(images):
        image.save(uploaded_path + "/" + str(i+1) + ".jpg", "JPEG")

def save_image(file_path, img):
    path = file_path + "/" + str(folder_count_f(file_path)+1) + ".jpg"
    cv2.imwrite(path, img)

def save_state(key, value):
    st.session_state.coord[key] = value

def makedirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def group_btn(path, alphabet, img, value):
    download_path = path + "/" + alphabet
    makedirs(download_path)
    save_image(download_path, img)
    st_key = alphabet+str(folder_count_f(download_path))
    save_state(alphabet, value)
    save_state(st_key, value)

#--------------------------------------------------------------------------------- 반환을 하는 함수
def show_image(file_path, index):
    file = file_path + "/" + str(index) + ".jpg"
    return file

def folder_count_o(path):
    file_list = os.listdir(path)
    file_count = len(file_list) - 1
    return file_count
def folder_count_f(path):
    file_list = os.listdir(path)
    file_count = len(file_list)
    return file_count
#----------------------------------------------------------------------------------

def main():
    st.sidebar.subheader('파일을 선택하세요')
    uploaded_file = st.sidebar.file_uploader("pdf파일을 선택하세요.", type=['pdf'])

    if not uploaded_file:
        return None
    
    bin_folder = "C:/st_bin"    
    folder_path = bin_folder + "/" + str(uploaded_file.name[:-4])             #C:/st_bin/파일이름
    image_path = folder_path + "/img"                                    #C:/st_bin/read_pdf/img
    group_path = folder_path + "/group"
    upload_path = image_path + "/" + uploaded_file.name              #C/st_bin/파일이름/image/파일이름.pdf

    makedirs(bin_folder)
    makedirs(folder_path)
    makedirs(image_path)

    with open(os.path.join(image_path, uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    pdf_to_image(upload_path, image_path)
    
    if folder_count_o(image_path) > 1: 
        num_page = st.sidebar.slider("page", min_value=1, max_value=folder_count_o(image_path))
    else:
        st.session_state.page = 1
    
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
        if not st.session_state.page:
            img = Image.open(show_image(image_path, num_page))
        else:
            img = Image.open(show_image(image_path, 1))
            
        rect = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                        aspect_ratio=aspect_ratio, return_type='box', key='coordination')
    with preview:
        raw_image = np.asarray(img).astype('uint8')
        left, top, width, height = tuple(map(int, rect.values()))
        preview_img = raw_image[top:top + height, left:left + width]
        st.image(preview_img, caption='masked image')
        st.write(rect)
    
    print(rect)
    btA, btB, btC, all = st.columns([0.25, 0.25, 0.25, 0.25])

    ##버튼을 눌렀을 때 특정 폴더에 캡처한 파일을 저장함.

    with btA:
        group_A = st.button("Group A")
        A_display = st.button("A 표시")
    with btB:
        group_B = st.button("Group B") 
        B_display = st.button("B 표시")
    with btC:
        group_C = st.button("Group C")
        C_display = st.button("C 표시")
    with all:
        group_All = st.button("Group All")
        All_display = st.button("모두 표시")

    if group_A:
            group_btn(group_path, "A", preview_img, rect)
            btA.success('성공적으로 추출했습니다.')

    elif group_B:
            group_btn(group_path, "B", preview_img, rect)
            btB.success('성공적으로 추출했습니다.')

    elif group_C:
            group_btn(group_path, "C", preview_img, rect)
            btC.success('성공적으로 추출했습니다.')
    elif group_All:
            group_btn(group_path, "A", preview_img, rect)
            group_btn(group_path, "B", preview_img, rect)
            group_btn(group_path, "C", preview_img, rect)
            btC.success('성공적으로 추출했습니다.')
    
    if A_display:
        preview.write(st.session_state.A)
    elif B_display:
        preview.write(st.session_state.B)
    elif C_display:
        preview.write(st.session_state.C)
    elif All_display:
        preview.write(st.session_state.coord)

    remove_all = st.sidebar.button("그룹 초기화")
    remove_recently = st.sidebar.button('최근 이미지 삭제')
    
    if remove_all:
        shutil.rmtree(group_path)
        st.session_state.coord.clear()
        makedirs(group_path)
    

    if remove_recently:
        recent_file = st.session_state.coord.popitem()
        group_folder = recent_file[0]
        if group_folder == 'A':
            st.session_state.A.popitem()
        elif group_folder == 'B':
            st.session_state.B.popitem()
        elif group_folder == 'C':
            st.session_state.C.popitem()

        recently_file = group_path + "/" + group_folder[0] + "/" + group_folder[1:] +".jpg"
        os.remove(recently_file)
        st.success("삭제 완료")
    
if __name__ == "__main__":
    main()
