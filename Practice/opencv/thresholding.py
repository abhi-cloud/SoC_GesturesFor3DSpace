import numpy as np
import cv2

# THRESHOLDING is the way by which we try to make an object
# come out of a background

""" img = cv2.imread('used_images_videos/lena.jpg', 0)
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) 
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # similarly thresh_toZero


cv2.imshow('Image', img)
cv2.imshow('Th1', th1)
cv2.imshow('Th2', th2)
cv2.imshow('Th3', th3)
cv2.imshow('Th4', th4)
 """

# ADAPTIIVE THREHOLDING is the method where ther the threshold is calculated 
# for different group of pixels
# used when we have different illuminations at different groups of pixels

img = cv2.imread('used_images_videos/sudoku.png', 0)
_, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 10)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)

cv2.imshow('Image', img)
cv2.imshow('Th1', th1)      # direct binary_threshold doent work
cv2.imshow('Th2 ', th2)
cv2.imshow('Th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()