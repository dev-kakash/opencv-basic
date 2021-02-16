import cv2
print("package Imported")

img = cv2.imread("../Resources/akash.jpg")

cv2.imshow("myOutput",img)
cv2.waitKey(0)