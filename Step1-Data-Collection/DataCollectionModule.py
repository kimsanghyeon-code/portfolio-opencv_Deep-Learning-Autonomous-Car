"""
- 이 모듈은 이미지 및 로그 파일을 저장함
- 이미지는 폴더에 저장됨
- 폴더는 "DataCollected" 이름으로 생성
- 이미지 이름과 스티어링 각도가 로그 파일에 기록됨
- SaveData 기능을 호출하여 시작
- saveLog 기능을 호출하여 종료
"""

import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

# 현재 디렉터리 경로
myDirectory = os.path.join(os.getcwd(), 'DataCollected')

# 이전 폴더 수를 기준으로 새 폴더 생성. +1씩 증가
while os.path.exists(os.path.join(myDirectory,f'IMG{str(countFolder)}')):
        countFolder += 1
newPath = myDirectory +"/IMG"+str(countFolder)
os.makedirs(newPath)

# 폴더에 이미지 저장
def saveData(img,steering):
    global imgList, steeringList
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace('.', '')
    fileName = os.path.join(newPath,f'Image_{timestamp}.jpg')
    cv2.imwrite(fileName, img)
    imgList.append(fileName)
    steeringList.append(steering)

# 세션 종료 시 로그 파일 저장
def saveLog():
    global imgList, steeringList
    rawData = {'Image': imgList,
                'Steering': steeringList}
    df = pd.DataFrame(rawData)
    df.to_csv(os.path.join(myDirectory,f'log_{str(countFolder)}.csv'), index=False, header=False)
    print('Log Saved')
    print('Total Images: ',len(imgList))

if __name__ == '__main__':
    cap = cv2.VideoCapture(-1)
    for x in range(10):
        _, img = cap.read()
        saveData(img, 0.5)
        cv2.waitKey(1)
        cv2.imshow("Image", img)
    saveLog()

