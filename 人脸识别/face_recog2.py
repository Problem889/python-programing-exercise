import cv2
print(cv2.__file__)
print(cv2.__version__)

image1 = cv2.imread("1.webp")
image2 = cv2.imread("2.webp")

cv2.imshow("image",image1)
cv2.waitKey(0)

cv2.imshow("picture", image2)
cv2.waitKey(0)

gray_img2 = cv2.cvtColor(image2, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_picture', gray_img2)
cv2.waitKey(0)

gray_img1 = cv2.cvtColor(image1, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray_picture', gray_img1)
cv2.waitKey(0)