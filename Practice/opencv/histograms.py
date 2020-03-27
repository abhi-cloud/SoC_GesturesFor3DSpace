# histograms tell us whether the image is properly exposed to light or not
# especially for the digital images. We can make adjustments based on that.

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('used_images_videos/lena.jpg')
# img = np.zeros((200, 200, 3), np.uint8)
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)
b, g, r = cv.split(img)
img_B = np.zeros((512, 512, 3), np.uint8)
img_G = np.zeros((512, 512, 3), np.uint8)
img_R = np.zeros((512, 512, 3), np.uint8)

img_B[:, :, 0] = b
img_G[:, :, 1] = g
img_R[:, :, 2] = r

cv.imshow('original', img)
cv.imshow('img_B', img_B)
cv.imshow('img_G', img_G)
cv.imshow('img_R', img_R)

plt.hist(b.ravel(), 256, [0, 256])          # cv2 also contains a method calcHist() and returns a histogram image
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()