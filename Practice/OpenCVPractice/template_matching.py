# finding a certain template in a larger image by drawing a 
# around the found region
# TEMPLATE MATCHING 

import numpy as np
import cv2 as cv

img = cv.imread('used_images_videos/rubberwhale1.png')
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

temp = cv.imread('used_images_videos/whale.png')
grey_temp = cv.cvtColor(temp, cv.COLOR_BGR2GRAY)
w, h = grey_temp.shape[::-1]   # ::-1 just to reverse the order

res = cv.matchTemplate(grey_img, grey_temp, cv.TM_CCOEFF_NORMED)
threshold = 0.99

loc = np.where(res >= threshold)
print(loc)

for i in zip(*loc[::-1]):
    cv.rectangle(img, i, (i[0]+w, i[1]+h), (255, 0, 0), 2)

cv.imshow('img', img)
cv.imshow('template', temp)
cv.waitKey(0)
cv.destroyAllWindows()