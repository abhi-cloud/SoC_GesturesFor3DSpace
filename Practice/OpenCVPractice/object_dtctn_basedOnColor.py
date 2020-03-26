import numpy as np
import cv2

def click(event, x, y, flgs, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        #print(b, g, r)
        findThis = np.uint8([[[b, g, r]]])
        hsvColor = cv2.cvtColor(findThis, cv2.COLOR_BGR2HSV)

        l_b = np.array([hsvColor[0][0][0] - 20, 100, 100])
        u_b = np.array([hsvColor[0][0][0] + 20, 255, 255])

        mask = cv2.inRange(hsv, l_b, u_b)
        res = cv2.bitwise_and(img, img, mask = mask)

        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

"""
cv2.namedWindow('img')
cv2.setMouseCallback('img', click)


img = cv2.imread('used_images_videos/detect_blob.png')
img = cv2.resize(img, (400, 400))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

 
while(1):

    cv2.imshow('img', img)

    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        break

"""
cap = cv2.VideoCapture(0) 

while(1):
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_b = np.array([110, 100, 100])
    u_b = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow('img', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()