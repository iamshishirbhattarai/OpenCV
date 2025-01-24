import cv2 as cv

# Reading the images
img = cv.imread('Images/Cat.jpeg')

cv.imshow("Cat", img)

# Reading the videos
capture = cv.VideoCapture('Videos/cat_video.mov') # This will open the webcam but for existing vidos you can just open as cv.VideoCapture('video.mp4)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

