import cv2

camera_id = 0
# Khai báo đối tượng video
video = cv2.VideoCapture(camera_id)

while True:
    ret, frame = video.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Anh tu cam", frame)
    if cv2.waitKey(1) == ord("q"):
        break

video.release()
cv2.destroyAllWindows()