import cv2
import numpy as np

img = cv2.imread("../Resources/wrap.jpg")


width,height = 350,250;

points = np.float32([[78,255],[377,125],[199,467],[500,274]])
points1 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(points,points1)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("OriginalImage",img)
cv2.imshow("WarpImage",imgOutput)
cv2.waitKey(0)