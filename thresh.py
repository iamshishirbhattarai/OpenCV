import cv2 as cv

img = cv.imread('Images/cat.jpeg')

cv.imshow("Original Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding : manually specify the specific thresholding value
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)

# Adaptive thresholding : adapts the threshold by iteself
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
                                       cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Threshold", adaptive_thresh)

adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, 
                                           cv.THRESH_BINARY_INV, 11, 3)
cv.imshow("Adaptive Threshold Inverse", adaptive_thresh_inv)


cv.waitKey(0)