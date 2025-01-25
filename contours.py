import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpeg')

cv.imshow('Cats', img)

# Converting the image to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# Applying Threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresholded Images", thresh)


# Contours Detection
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# Displaying Contours in a blank image
blank = np.zeros((img.shape), dtype = 'uint8')
cv.imshow("Blank Image", blank)
cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow("Contours", blank)

# Note : Try the contours with Canny images (edge Detection) at first

cv.waitKey(0)