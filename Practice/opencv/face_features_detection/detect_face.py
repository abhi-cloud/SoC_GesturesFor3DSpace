import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# ^^^ here the machine trains over some positive and some negative 
# images i.e. images that contain faces and don't contain faces 
# respectively

img = cv.imread('friends.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 10)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('detected', img)
cv.waitKey(0)
cv.destroyAllWindows()
