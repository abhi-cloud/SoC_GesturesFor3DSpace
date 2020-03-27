import numpy as np
import cv2 as cv

img = cv.imread('used_images_videos/detect_blob.png')
# img = cv.resize(img, (400, 400))

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Shi Tomasi method for detecting corners- we can also specify the required number of corners
corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x,y), 2, 255, -1)

## harris corner detector method

# gray = np.float32(gray)
# dst = cv.cornerHarris(gray, 2, 3, 0.04)

# dst = cv.dilate(dst, None)
# img[dst > 0.01 * dst.max()] = [0, 0, 255]
# # print(dst.max())


cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()