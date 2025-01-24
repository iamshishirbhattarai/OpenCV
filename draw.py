import cv2 as cv
import numpy as np

blank_image = np.zeros((500,500,3), dtype='uint8') # uint8 is the dtype of the image

# Painting the whole blank image with some color
# blank_image[:] = 0,255,0
# cv.imshow('Green', blank_image)


# Painting the certain portion of the blank image
blank_image_two = np.zeros((500,500,3), dtype='uint8')
blank_image_two[200:300, 300:400] = 255,0,0
# cv.imshow('PaintingSomePart', blank_image_two)

# Draw a rectangle
# cv.rectangle(blank_image, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) 
# cv.imshow('Rectangle', blank_image)

# Draw a circle
cv.circle(blank_image, (250,250), 40, (0,255,0), thickness=-1)
cv.imshow('Circle', blank_image)

# Draw a line
cv.line(blank_image, (50,50), (250,250), (0,255,0), thickness=3)
cv.imshow('Line', blank_image)

# Put a text
cv.putText(blank_image, 'Hello', (300, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank_image)

cv.waitKey(0)


