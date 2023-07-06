import streamlit as st
import cv2 as cv
import numpy as np

# 드래그로
# GUI를 streamlit 라이브러리 사용
# 화면 캡쳐 및 글자분석은 opencv 라이브러리 사용

img = np.full((800, 800, 3), 255, dtype=np.uint8)

cv.imshow("blank", img)

#  event는 윈도우에서 발생하는 이벤트, x와 y는 마우스의 좌표
# flags는 특수한 상태를 확인하는 용도, param은 전달되는 사용자 정의 데이터

user_xy =[0 for i in range(4)]

def mouse_click(event, x, y, flags, param):
    global user_xy

    if event == cv.EVENT_LBUTTONDOWN:
        previus_x = x
        previus_y = y
        user_xy[0] = previus_x
        user_xy[1] = previus_y
        print(user_xy)

    elif event == cv.EVENT_LBUTTONUP:
        user_xy[2]  = x
        user_xy[3]  = y
        print(user_xy)
        cv.rectangle(img, (user_xy[0], user_xy[1]), (user_xy[2], user_xy[3]), (0,255,0), 10)
        cv.imshow("blank", img)

while True:
    if cv.waitKey(0):
        break

cv.destroyAllWindows()