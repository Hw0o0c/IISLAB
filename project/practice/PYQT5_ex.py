import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap
import sys

app = QApplication(sys.argv)
window = QWidget()

# OpenCV 창 생성
cv2.namedWindow("OpenCV Window")

# QLabel 생성
label = QLabel("OpenCV Window")

# 레이아웃 생성
layout = QVBoxLayout()
layout.addWidget(label)

# 위젯에 레이아웃 설정
window.setLayout(layout)

# 위젯을 OpenCV 창에 표시
window.show()

# OpenCV 창 업데이트
while cv2.getWindowProperty("OpenCV Window", 0) >= 0:
    ret, frame = cv2.read()

    # OpenCV 프레임을 PyQt 이미지로 변환
    image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_BGR888)
    pixmap = QPixmap.fromImage(image)

    # QLabel에 이미지 표시
    label.setPixmap(pixmap)

    # OpenCV 창에 이미지 표시
    cv2.imshow("OpenCV Window", frame)

    # OpenCV 창이 업데이트되는 동안 PyQt 이벤트 처리
    app.processEvents()

# OpenCV 창 닫기
cv2.destroyAllWindows()