import cv2
import numpy as np

img1=cv2.imread("../Resources/resized_sample.jpg")
img2 = cv2.GaussianBlur(img1,(7,7),0)

imgHor = np.hstack((img1,img2))

cv2.imshow("a",imgHor)
cv2.waitKey(0)