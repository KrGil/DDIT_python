# 필요한 라이브러리 불러오기
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
import numpy as np
import cv2

# MNIST 데이터셋 불러오기
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 이미지 데이터 준비하기 (모델에 맞는 크기로 바꾸고 0과 1사이로 스케일링)
train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print(train_labels[0])
print(test_labels[0])

# 레이블을 범주형으로 인코딩
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

print(train_labels[0])
print(test_labels[0])


# 모델 정의하기 (여기에서는 Sequential 클래스 사용)
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
model.add(layers.Dense(10, activation='softmax'))

# 모델 컴파일 하기
model.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
                
# fit() 메서드로 모델 훈련 시키기
model.fit(train_images, train_labels, epochs=5, batch_size=128)

# 학습 후 predict 해보기.
predictions = model.predict(test_images)
predictions_np = np.array(predictions)
predictions_argmax = np.argmax(predictions_np)

# predictions한 것의 값과 test_labels의 값을 비교하기.
# predictions 값으로 변경. 

cnt =0
wrong_cnt =0
for pred in predictions:
    prediction = np.argmax(np.array(pred))
    test_label = np.argmax(test_labels[cnt])
    if prediction!=test_label:
        print(wrong_cnt)
        img = np.array(test_images[cnt] *255)
        img_np = img.reshape(28, 28)
        fileName = f"./diff/{prediction}_{test_label}_{wrong_cnt}.png" 
        cv2.imwrite(fileName, img_np)
        wrong_cnt += 1;
    cnt += 1
    
# predict_google_i.png로 틀린것을 저장하기.

# 테스트 데이터로 정확도 측정하기
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('test_acc: ', test_acc)