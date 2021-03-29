import cv2

import numpy as np

im = cv2.imread("./image/IU.jpg", 1)

im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

print(im_gray)

cv2.imwrite("C:/Users/PC-11/Desktop/TEST/1TEST.jpg", im_gray)
