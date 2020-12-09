import cv2 as cv
import cv2
import numpy as np
camera = cv2.VideoCapture("videounuz.mp4")
while 1:
    _,frame = camera.read()
    cv.imshow('camera',frame)
    laplacian = cv.Laplacian(frame,cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv2.imshow('Laplacian',laplacian)
    kenar = cv.Canny(frame,100,100)
    cv2.imshow('Canny',kenar)
    if cv.waitKey(5) == ord('x'):
        break
camera.relase()
cv.destroyAllWindows()