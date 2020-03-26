import numpy as np
import cv2

img = cv2.imread('used_images_videos/graf3.png')
img2 = cv2.imread('used_images_videos/lena.jpg')
print(img.shape)
print(img.size)
print(img.dtype)

b, g, r = cv2.split(img)

# print (b[1:5, 1:10])  # same as b[1:5][1:10]
# therefore the statement 
# ball = img[y1:y2, x1:x2] copies rectangular area from the img whose 2 far
# ends are (x1, y1) and (x2, y2) 

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

dps = cv2.addWeighted(img2, 0.6, img, 0.4, 20)  # images are required to be of same size

cv2.imshow('image', dps)

cv2.waitKey(1000)
cv2.destroyAllWindows()


