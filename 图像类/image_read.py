import cv2
import numpy as np

img1 = cv2.imread('view.jpg')
cv2.imshow('Sunset',img1)
cv2.waitKey(5000)

img2 = cv2.imread('CET6.jpg')
kernel = np.ones((5,5), np.uint8) # filter
print(kernel, '\n')
print('\n', img2.shape)
print('\n', type(img2))

img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img2Blur = cv2.GaussianBlur(img2Gray, (7, 7), 0)
img2Canny = cv2.Canny(img2, 150, 200)
img2Dialation = cv2.dilate(img2Canny, kernel, iterations=1)
img2Eroded = cv2.erode(img2Dialation, kernel, iterations=1)

cv2.imshow("Gray",img2Gray)
cv2.imshow("Blur",img2Blur)
cv2.imshow("Canny",img2Canny)
cv2.imshow("Dialation",img2Dialation)
cv2.imshow("Eroded",img2Eroded)
cv2.waitKey(0)

cv2.destroyAllWindows()


