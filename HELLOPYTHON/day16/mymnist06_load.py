# 0. 사용할 패키지 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
from keras.models import load_model

# 1. 실무에 사용할 데이터 준비하기
(train_images, train_labels), (test_origin_images, test_origin_labels) = mnist.load_data()
print(test_origin_images.shape) #(10000, 28, 28)
print(test_origin_images[0])
print(test_origin_images[0].shape) #(28, 28)
test_images = test_origin_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255
print(test_images.shape) #(10000, 784)
print(test_images[0])
print(test_images[0].shape) #(784,)

myimage = test_images[0:1,:]
print("myimage.shape : ", myimage.shape)


# 2. 모델 불러오기
model = load_model('./model/mnist_mlp_model.h5')
predictions = model.predict(myimage)

# 3. 모델 사용하기
print(np.argmax(predictions[0]))