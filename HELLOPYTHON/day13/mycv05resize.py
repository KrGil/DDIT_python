import cv2

image = cv2.imread("image/IU.jpg", cv2.IMREAD_COLOR)

#절대 사이즈
image_two = cv2.resize(image, dsize=(640, 480))
#상대 사이즈
image_three= cv2.resize(image, dsize=(0, 0), fx=0.3, fy=0.7, interpolation=cv2.INTER_LINEAR)

cv2.imshow("original", image)
cv2.imshow("absolute", image_two)
cv2.imshow("relative", image_three)
cv2.waitKey()
cv2.destroyAllWindows()