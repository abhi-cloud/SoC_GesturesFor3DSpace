import numpy as np
import cv2 as cv

cv.namedWindow('tracking')
Org = cv.imread('used_images_videos/sudoku.png')
# Org = cv.imread('used_images_videos/aloeR.jpg')
Org = cv.resize(Org, (512, 512))

cv.imshow('tracking', Org)

cv.createTrackbar('t1', 'tracking', 100, 255, lambda x: None)
cv.createTrackbar('t2', 'tracking', 200, 255, lambda x: None)

while True:
    img = Org.copy()
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    t1 = cv.getTrackbarPos('t1', 'tracking')
    t2 = cv.getTrackbarPos('t2', 'tracking')
    # thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 10) # THRESH_BINARY
    canny = cv.Canny(img_gray, t1, t2)
    contours, heirarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    
    # "contours" (here stores) is a python list of all contors in the image
    # each individual contour is a Numpy array of (x, y) co-ordinates of boundary points of the object
    # "heirarchy" is optional output vector containing information about the topology of the image

    cv.drawContours(img, contours, -1, (0, 255, 0), 2)

    cv.imshow('Image', img)
    cv.imshow('thresh', canny)
    # cv.imshow('ghey', img_gray)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()