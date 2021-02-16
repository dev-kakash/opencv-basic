import cv2
import numpy as np
img = cv2.imread("../Resources/resized_sample.jpg")
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ingBlur=cv2.GaussianBlur(img,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imageDialetion = cv2.dilate(imgCanny,kernel,iterations=1)
imageEroded = cv2.erode(imageDialetion,kernel,iterations=1)


cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",ingBlur)
cv2.imshow("EdgeDectected",imgCanny)
cv2.imshow("ThickEdge",imageDialetion)
cv2.imshow("ThinEdge",imageEroded)
cv2.waitKey(0)