import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/city.webp')
height = int(img.shape[0] * 0.75)
width = int(img.shape[1] * 0.5)
img = cv.resize(img, (width,height))
cv.imshow("Image", img)

# Whenever we observe the image in other libraries than OpenCV, the colors are kind of inverted
# As other libraries follows the RGB format and OpenCV follows BGR format
# Here we see the same thing with matplotlib
plt.imshow(img)
plt.show()

# Now lets see the same thing by converting BGR into RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

# BGR to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV image", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# Note : We can do the inverse conversion likewise except the direct conversion from
# Grayscale to HSV and LAB !! For that, the conversion should be like gray -> BGR -> HSV/LAB

cv.waitKey(0)