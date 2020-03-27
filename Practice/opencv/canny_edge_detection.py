import numpy as np
import cv2 as cv
from  matplotlib import pyplot as plt

img = cv.imread('used_images_videos/messi5.jpg', 0)

cv.namedWindow('image')
cv.imshow('image', img)
cv.createTrackbar('t1', 'image', 100, 255, lambda x: None)
cv.createTrackbar('t2', 'image', 200, 255, lambda x: None)

while True:
    t1 = cv.getTrackbarPos('t1', 'image')
    t2 = cv.getTrackbarPos('t2', 'image')

    print(t1, t2)
    canny = cv.Canny(img, t1, t2)

    titles = ['canny']
    images = [canny]

    # cv.imshow('canny', canny)
    for i in range(len(images)):
        plt.subplot(1, 1, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])

    plt.show()
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()