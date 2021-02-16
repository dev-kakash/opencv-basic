import cv2
print("package Imported")

img = cv2.imread("../Resources/resized_akash.jpg")
print(img.shape)

imgCropped = img[100:450,50:300]

cv2.imshow("myOutput",img)
cv2.imshow("myOutputCropped",imgCropped)
cv2.waitKey(0)