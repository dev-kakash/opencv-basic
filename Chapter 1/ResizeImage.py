import cv2
img = cv2.imread("../Resources/color.jpg")

scale_percent = 0.50
width = int(img.shape[1]*scale_percent)
height = int(img.shape[0]*scale_percent)
dimension = (width,height)

resizedImage = cv2.resize(img,dimension,interpolation=cv2.INTER_AREA)

cv2.imshow("Resized Window",resizedImage)
cv2.imwrite("../Resources/resized_sample.jpg", resizedImage)
cv2.waitKey(0)