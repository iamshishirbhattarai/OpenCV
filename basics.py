import cv2 as cv

img = cv.imread('Images/cat.jpeg')

cv.imshow('Image', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur) 

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Edge Cascade', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=3 )
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (200, 200))
cv.imshow("Resized", resized)

# Cropped
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)