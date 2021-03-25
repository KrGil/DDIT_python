import cv2
image = cv2.imread("image/IU.jpg", cv2.IMREAD_ANYCOLOR)
image_wb = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_rate = cv2.rotate(image_wb, cv2.ROTATE_90_CLOCKWISE ) 
print(image)

cv2.imshow("IU", image_rate)
cv2.waitKey(0) #화면에 떠있을 때 잡아주기.
cv2.destroyAllWindows()