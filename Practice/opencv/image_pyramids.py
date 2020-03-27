# Pyramid representation is a type of multi-scale signal representation in
# which a signal or an image is subject to repeated smoothing and subsampling.

import numpy as np
import cv2 as cv

# Gaussian pyramid
img = cv.imread('used_images_videos/lena.jpg')
layer = img.copy()
gpyr = [layer]

for i in range(5):
    layer = cv.pyrDown(layer)       # similarly pyrUp, note that pyrDown loses information 
    gpyr.append(layer)
    # cv.imshow(str(i), layer)

# No exculsive function for Laplacian pyramid
# A layer of LAPLACIAN PYRAMID is formed by the difference between that 
# level in GP and expanded version of its upper level in GP

lpyr = []

for i in range(4):
    upper_gp = cv.pyrUp(gpyr[i+1])
    laplacian = cv.subtract(gpyr[i], upper_gp)
    cv.imshow(str(i), laplacian)
    lpyr.append(laplacian)

cv.imshow('Original', img)
cv.waitKey(0)
cv.destroyAllWindows()


