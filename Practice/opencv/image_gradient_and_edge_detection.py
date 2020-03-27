""" 
Image gradient is directional change in the intensity or the color of the image
Used in image processing fields like finding edges inside the image
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('used_images_videos/messi5.jpg', 0)

lap = cv.Laplacian(img, cv.CV_64F, ksize = 3)
lap = np.uint8(np.absolute(lap))

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0) # d/dx      # DOUBT!!!
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1) # d/dy

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# it = cv.addWeighted(sobelX, 1, sobelY, 1, 10)
# with sobel taken with 2nd derivatives will give laplacian 

titles = ['image', 'laplacian', 'sobelX', 'sobelY']
images = [img, lap, sobelX, sobelY]

for i in range(len(images)):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()