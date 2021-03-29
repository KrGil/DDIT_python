import cv2
import numpy as np

arr = [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ]

arr_n = np.array(arr)*255

print(arr_n)

cv2.imwrite("C:/Users/PC-11/Desktop/TEST/red.jpg", arr_n)

