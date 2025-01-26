import cv2 as cv
import numpy as np

img = cv.imread('Images/city.webp')
img = cv.resize(img, (500, 700))

cv.imshow("Original", img)

b, g,r = cv.split(img)

# wherever the presence of these individual colors are more, it appears whiter in the image.
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

# To obtain the image in their respective color, we can use merging with blank img
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b,blank, blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow("Only Blue", blue)
cv.imshow("Only Green", green)
cv.imshow("Only Red", red)

cv.waitKey(0)
