import cv2
import numpy as np

image = cv2.imread("0.jpg", 1)
#이미지 불러오기 및 px사이즈 바꾸기
image_two = cv2.resize(image,(28, 28))
#흑백화시키기
image_wb = cv2.cvtColor(image_two, cv2.COLOR_BGR2GRAY)
#숫자의 색상과 배경색상 반전시켜서 소수점 만들어주기
img_input = (255 - image_wb)/255
#일렬로 배열화 시키기
img_input2 = np.reshape(img_input, (1, 28*28))

print(img_input2)
print(img_input2.shape)

cv2.imshow("Test", img_input2)
cv2.waitKey()
cv2.destroyAllWindows()