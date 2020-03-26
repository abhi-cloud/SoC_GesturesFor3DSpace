import numpy as np
import cv2

# MASKS are binary images that indicates the pixels on which operations have to be performed
# Binary opeartions are used on masks

img1 = np.zeros((512, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((512, 512, 3), np.uint8)
img2 = cv2.rectangle(img2, (256, 0), (512, 512), (255, 255, 255), -1)

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot = cv2.bitwise_not(img1)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitNot', bitNot)


cv2.waitKey(0)
cv2.destroyAllWindows()