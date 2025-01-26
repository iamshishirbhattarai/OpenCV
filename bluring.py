import cv2 as cv

img = cv.imread('Images/cat.jpeg')
cv.imshow("Original Image", img)

# Blurring : Averaging -> the center of the kernel gets the average intensity value of surrounding pixels 
average = cv.blur(img, (7,7))
cv.imshow("Average", average)

# Blurring : Gaussian -> center gets the average weight of surrounding pixels (weights are 
# assigned to every pixels)
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian", gaussian)

# Blurring : Median -> Similar as averaging but here median is calculated
median = cv.medianBlur(img, 7)
cv.imshow("Median", median)

# Blurring : Bilateral -> Blurs the image but retains the edges in the image
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral", bilateral)

cv.waitKey(0)