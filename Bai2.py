import cv2
import imutils

camera_id = 0

# Biến rotate không xoay = 0 độ
rotate = 0
video = cv2.VideoCapture(camera_id)

while True:
    ret, frame = video.read()
    if ret:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Anh tu cam", frame)
    key = cv2.waitKey(1)

    if key == ord("q"):
        break

    elif key == ord("a"):
        rotate = 90
    elif key == ord("d"):
        rotate = -90
