import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpeg')
cv.imshow('Cat', img)

# Dimension of the mask should be strictly same as that of the image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow("Blank", blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow("Mask", mask)

masking_img = cv.bitwise_and(img,img, mask=mask)
cv.imshow("Masked Image", masking_img)

cv.waitKey(0)