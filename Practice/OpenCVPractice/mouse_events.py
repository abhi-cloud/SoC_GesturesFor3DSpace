import numpy as np
import cv2

# events = {i for i in dir(cv2) if 'EVENT' in i}
# print (events)
# just to print classes/members that have str 'EVENT' in their name

""" img[y, x, i] (where i is 0, 1, 2) represents the BGR channels respectively """

def click(event, x, y, flags, param):           # defining a callback function
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_DUPLEX
        strXY = str(x) + ', ' + str(y)

        cv2.putText(img, strXY, (x, y), font, 0.5, (255, 0, 0), 2)
        
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        cv2.circle(img, (x, y), 2, (255, 255, 255), -1)
        thecolor = np.zeros((512, 512, 3), np.uint8)

        thecolor[:256] = [blue, green, red]
        thecolor[256:] = [red, green, blue]
        cv2.imshow('image', img)
        cv2.imshow('COLOR', thecolor)



# img = np.zeros((512, 512, 4), np.uint8)
img = cv2.imread('used_images_videos/lena.jpg')
cv2.imshow('image', img)
# print (img)

cv2.setMouseCallback('image', click)

cv2.waitKey(0)
cv2.destroyAllWindows()