"""
- 웹캠을 통해 opencv 패키지를 사용하여 이미지를 얻는 모듈
- 디스플레이를 켜거나 끄고 이미지 크기를 정의할 수 있음
"""

import cv2

cap = cv2.VideoCapture(-1)

def getImg(display=False,size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)