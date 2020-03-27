# MORPHOLOGY is a broad set of image processing operations that process images
# based on shapes. In a morphological operation, each pixel in the 
# image is adjusted based on the value of other pixels in its neighborhood.

# normally we perform morphological transformations on the binary images
# therefore we need to provide a mask to the images

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('used_images_videos/smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)  
# defines the neighbourhood over which dilation is done around the pixel

dilation = cv.dilate(mask, kernel, iterations = 5) 
# dilates the source image using the specified structuring element that determines the shape of a pixel neighborhood over which the maximum is taken

erosion = cv.erode(mask, kernel, iterations = 2)   
# sets a particular pixel iff all the neighbourhood pixels( given by kernel) are 1

opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel, iterations=5) 
# erosion followed by dilation

closing = cv.morphologyEx(mask,cv.MORPH_CLOSE, kernel, iterations = 5) 
# dialation followed by erosion

mg = cv.morphologyEx(mask,cv.MORPH_GRADIENT, kernel, iterations = 5) 
# difference between dilation and erosion

th = cv.morphologyEx(mask,cv.MORPH_TOPHAT, kernel, iterations = 5) 
# difference between original image and opening of image

titles = ['smarties', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(len(images)):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])


plt.show()