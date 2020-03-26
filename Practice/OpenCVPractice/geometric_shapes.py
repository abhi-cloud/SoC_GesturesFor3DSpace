import numpy as np
import cv2

img0 = cv2.imread('used_images_videos/lena.jpg', 1)
img = np.zeros([512, 512, 3], np.uint8)

img2 = cv2.rectangle(img, (0, 0), (255, 255), (147, 96, 47), -1)

""" Similarly we use circle, line, arrowedLine, polygon, ellipse etc to draw the shapes tacit from the names  """

font = cv2.FONT_HERSHEY_DUPLEX
img2 = cv2.putText(img2, 'Abhinav', (100, 100), font, 2, (100, 100, 20), 4, cv2.LINE_8)


cv2.imshow('pagal', img2)

# cv2.imwrite('gshape.jpg', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

