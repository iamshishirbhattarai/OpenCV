import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/cat.jpeg')
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(gray_hist)
plt.show()

# Masking with histogram
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Mask", mask)

# Masked grayscale histogram
masked_gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title("Masked Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.plot(masked_gray_hist)
plt.show()

# Color Histogram
colors = ('b', 'g', 'r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    
plt.title("Coloured Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.show()

# Similarly we can also do for mask ....

cv.waitKey(0)