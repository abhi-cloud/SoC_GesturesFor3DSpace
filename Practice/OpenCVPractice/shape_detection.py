import numpy as np
import cv2 as cv

img = cv.imread('used_images_videos/detect_blob.png')
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(grey, 25, 255, cv.THRESH_BINARY)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in contours:
    approx = cv.approxPolyDP(c, 0.01*cv.arcLength(c, True), True)
    cv.drawContours(img, [approx], 0, (255, 255, 255), 2)

    x = approx.ravel()[0] + 10
    y = approx.ravel()[1] + 10

    text = ""
    if len(approx) == 3:
        text = "Triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv.boundingRect(approx)
        as_ratio = float(w)/h
        if as_ratio > 0.9 and as_ratio < 1.1:
            text = "Square"
        else:
            tect = "Rectangle"
    elif len(approx) == 5:
        text = "Pentagon"
    elif len(approx) == 10:
        text = "Star"
    else:
        (x, y, w, h) = cv.boundingRect(approx)
        as_ratio = float(w)/h
        if as_ratio > 0.9 and as_ratio < 1.1:
            text = "Circle"
        else:
            tect = "Ellipse"
    
    cv.putText(img, text, (x, y), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)

cv.imshow('shapes', img)
cv.imshow('shapes_grey', thresh)

cv.waitKey(0)
cv.destroyAllWindows()
