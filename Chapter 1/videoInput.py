import cv2
cap = cv2.VideoCapture("../Resources/myVideo.mp4")

while True:
    success, img=cap.read()
    cv2.imshow("MyVideo",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break