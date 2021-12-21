import cv2
import imutils

# Đọc ảnh
image = cv2.imread("hello.jpg")

# # convert ảnh dạng BGR(Màu mặc định) sang gray(Xám)...
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Xoay ảnh 180 độ
# image = imutils.rotate(image, 180)


# chỉnh size ảnh
image = cv2.resize(image, dsize=(700, 400))


# áp threshold lên ảnh nếu ngưỡng  > 127 thì bằng 255(Màu trắng), < 127 thì về 0(Màu đen)
# tùy ảnh để chọn ngưỡng phù hợp
# ret, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Tìm cạnh (Biên)
# image = cv2.Canny(image, threshold1=50, threshold2=200)

# Làm mờ ảnh (ksize=(x,y) x, y luôn luôn là số lẻ). ksize càng lớn ảnh càng mờ
image = cv2.GaussianBlur(image, ksize=(31, 31), sigmaX=0)

# Hiển thị ảnh ra màn hình
cv2.imshow("Anh", image)
# Dừng màn hình
cv2.waitKey()
# Đóng các cửa sổ

cv2.destroyAllWindows()

