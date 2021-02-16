import numpy as np
import cv2

image = cv2.VideoCapture(0)
while True:
    _, img = image.read()


    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break