import cv2

# Cam máy tính mặc định ID = 0, nếu muốn đọc file video thì camera_id = "Tên file video"
camera_id = 0
# Mở cam
cap = cv2.VideoCapture(camera_id)
# Đọc ảnh từ cam
while True:
    # Đọc ảnh
    ret, frame = cap.read()
    # hiển thị
    cv2.imshow("cam", frame)

    # Kiểm tra nếu bấm Q thì thoát
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

# Thoát cam
cap.release()
cv2.destroyAllWindows()


