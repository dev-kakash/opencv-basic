import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)

cv2.line(img,(0,250),(512,250),(0,255,255),2)
cv2.line(img,(250,0),(250,512),(0,255,255),2)

cv2.rectangle(img,(200,200),(400,400),(135,0,255),5)

cv2.circle(img,(200,200),50,(255,0,255),1)

cv2.putText(img,"OpenCV Chapter1",(200,100),cv2.FONT_HERSHEY_DUPLEX,.7,(150,0,150),1)



cv2.imshow("image",img)
cv2.waitKey(0)