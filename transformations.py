import cv2 as cv
import numpy as np

img = cv.imread('Images/cat.jpeg')
cv.imshow("Original Image", img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated_img = translate(img, 100, 100)
cv.imshow("Translated Image", translated_img)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)
 
rotated_img = rotate(img, 45)
cv.imshow("Rotated Image", rotated_img)

# Flipping
flip = cv.flip(img, -1) # 0 -> Vertical Flip, 1 -> Horizontal Flip, -1 -> Both
cv.imshow("Flipped Image", flip)
cv.waitKey(0)