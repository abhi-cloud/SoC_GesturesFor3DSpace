import numpy as np
import cv2 as cv

# def nothing(x):
#     print (x)

img = np.zeros((512, 512, 3), np.uint8)

cv.namedWindow('LetsRoll')

cv.createTrackbar('B', 'LetsRoll', 0, 255, lambda x: None)
cv.createTrackbar('G', 'LetsRoll', 0, 255, lambda x: None)
cv.createTrackbar('R', 'LetsRoll', 0, 255, lambda x: None)
cv.createTrackbar('switch', 'LetsRoll', 0 , 1, lambda x: None)

""" 
img2 = cv.imread('used_images_videos/lena.jpg')
print (img2[0][0])
"""

while(1):
    img2 = cv.imread('used_images_videos/lena.jpg')
    k= cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('B', 'LetsRoll')
    g = cv.getTrackbarPos('G', 'LetsRoll')
    r = cv.getTrackbarPos('R', 'LetsRoll')
    s = cv.getTrackbarPos('switch', 'LetsRoll')


    for x in img2:
        for y in x:
            y[0] = b

    if s == 1:
        img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
    else:
        pass

    cv.imshow('LetsRoll', img2)

cv.destroyAllWindows()
