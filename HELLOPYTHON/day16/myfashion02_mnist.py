# 0. 사용할 패키지 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
from keras.models import load_model
import cv2

# 1. 실무에 사용할 데이터 준비하기
# fashion_mnist = tf.keras.datasets.fashion_mnist
# (train_images, train_labels), (test_origin_images, test_origin_labels) = fashion_mnist.load_data()
#
# test_images = test_origin_images.reshape((10000, 28 * 28))
# test_images = test_images.astype('float32') / 255
#
# myimage = test_images[0:1,:]
# print("myimage.shape : ", myimage.shape)

# 1. 실무에 사용할 데이터 준비하기
image = cv2.imread("1.jfif", 1)

image_two = cv2.resize(image,(28, 28))
# 흑백화
image_wb = cv2.cvtColor(image_two, cv2.COLOR_BGR2GRAY)
#사진의 0과 학습한 0의 색상이 반전된다. 그래서 반전해준다.
print(image_two)

test_images = image_wb.reshape((1, 28 * 28))
test_images = (255-test_images.astype('float32')) / 255

print(test_images)
print(test_images.shape)

# 2. 모델 불러오기
model = load_model('./model/mymodel_fashion.h5')
predictions = model.predict(test_images)

# 3. 모델 사용하기
print(np.argmax(predictions))