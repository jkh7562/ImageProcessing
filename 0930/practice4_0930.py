import cv2

image = cv2.imread("../Image/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

cv2.imwrite("../Image/write_test1.jpg", image)
cv2.imwrite("../Image/write_test2.jpg", image, params_jpg)
cv2.imwrite("../Image/write_test3.png", image, params_png)
cv2.imwrite("../Image/write_test4.bmp", image)
print("저장 완료")
