# 'matplotlib' is a python plotting library which gives wide variety of plotting methods,
# highly used with OpenCV for different kinds of graphs of images
# graphs are generally used to analyse the images  

from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread('used_images_videos/lena.jpg', -1)
cv.imshow('image', img)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)     # takes images in rbg format
plt.xticks([]), plt.yticks([]) 
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
