import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import Qt
import sys
#import pdf2image

image_path = "D:/data/banana.jpeg"

image = cv2.imread(image_path)

def image_reset():
    image = cv2.imread(image_path)
    cv2.imshow("img", image)


cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", image)

def mouse_click(event, x, y, flags, param):
    global image, previus_x, previus_y

    if event == cv2.EVENT_FLAG_LBUTTON: # 좌클릭으로 마우스 좌표저장
        previus_x = x
        previus_y = y

    elif event == cv2.EVENT_FLAG_RBUTTON:# 우클릭으로 그림 초기화
        image_reset()
    # 마우스를 드래그 했을 때 상자로 영역 표시
    # UI가 나오고
    # UI의 버튼을 클릭했을 경우 이미지 추출해서
    # 어떤 그룹에 넣음.

    elif event == cv2.EVENT_LBUTTONUP:
        # 다시 그리기 전 이미지 원본을 초기화
        # 리셋을 앞에 둔 이유는 드래그 한 범위를 표시하기 위함.
        
        image_reset()

        if(previus_x !=x and previus_y != y):
            copied_image = image.copy()
            cv2.rectangle(copied_image, (previus_x, previus_y), (x, y), (0,0,255), 0)
            cv2.imshow("img", copied_image)
            
            select_image = image[ min(previus_y,y) : max(previus_y,y), min(previus_x, x) : max(previus_x, x)]
            cv2.namedWindow("selected", cv2.WINDOW_NORMAL)
            cv2.imshow("selected", select_image)


#def buttonUI():


# PyQt5 애플리케이션 초기화
app = QApplication(sys.argv)
window = QWidget()

# QLabel 및 QPushButton 생성
label = QLabel("OpenCV Image")
button = QPushButton("Click Me")

# QVBoxLayout 생성
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)

# 위젯에 레이아웃 설정
window.setLayout(layout)

# OpenCV 창에 마우스 이벤트 연결
cv2.setMouseCallback("img", mouse_click)

# PyQt5 애플리케이션 실행
window.show()
sys.exit(app.exec_())