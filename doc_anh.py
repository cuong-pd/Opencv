import cv2
import imutils

# Đọc ảnh
image = cv2.imread("hello.jpg")

# Đọc ảnh dưới dạng đen trắng
image = cv2.imread("hello.jpg", cv2.IMREAD_GRAYSCALE)

# Hiển thị ảnh
cv2.imshow("anh", image)

# đổi size ảnh
# image_size = cv2.resize(image, dsize=None, fx = 0.5, fy = 0.5) giảm một nửa kích thước
# muốn thay đổi theo tùy ý => truyền tham số vào fx, fy
image_size = cv2.resize(image, dsize=(700, 400))
cv2.imshow("Anh resize", image_size)

# Xoay ảnh
image_rotate = imutils.rotate(image, 180)
cv2.imshow("Anh rotate", image_rotate)

# Dừng màn hình
cv2.waitKey()

# convert ảnh dạng BGR(Màu mặc định) sang gray(Xám)...
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Anh xam", image_gray)

# Đóng các cửa sổ
cv2.destroyAllWindows()

