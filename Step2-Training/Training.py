print('Setting UP')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from sklearn.model_selection import train_test_split
from utlis import *


#### 1단계 - 데이터 초기화
path = '/home/pi/portfolio/project1/Neural-Networks-Self-Driving-Car-Raspberry-Pi-main/Step1-Data-Collection/DataCollected'
data = importDataInfo(path)
print(data.head())

#### 2단계 - 데이터 시각화 및 균형 조정
data = balanceData(data,display=True)

#### 3단계 - 처리 준비
imagesPath, steerings = loadData(path,data)

#### 4단계 - 트레이닝 및 확인을 위한 분할작업 
xTrain, xVal, yTrain, yVal = train_test_split(imagesPath, steerings,
                                              test_size=0.2,random_state=10)
print('Total Training Images: ',len(xTrain))
print('Total Validation Images: ',len(xVal))

#### 5단계 - 데이터 확장

#### 6단계 - 전처리

#### 7단계 - 모델 생성
model = createModel()

#### 8단계 - 트레이닝
history = model.fit(dataGen(xTrain, yTrain, 100, 1),
                                  steps_per_epoch=100,
                                  epochs=10,
                                  validation_data=dataGen(xVal, yVal, 50, 0),
                                  validation_steps=50)

#### 9단계 - 모델 저장
model.save('model.h5')
print('Model Saved')

#### 10단계 - 결과 표시
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Training', 'Validation'])
plt.title('Loss')
plt.xlabel('Epoch')
plt.show()
























