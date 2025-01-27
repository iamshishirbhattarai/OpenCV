import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpeg')
cv.imshow('Original Image', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacian", lap)

# Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel X", sobel_x)
cv.imshow("Sobel Y", sobel_y)

combined_sobel = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow("Combined", combined_sobel) 

cv.waitKey(0)