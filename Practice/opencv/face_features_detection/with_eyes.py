import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# here we will detect eyes within those detected faces 

img = cv.imread('friends2.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 12)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
    f_gray = gray[y:y+h, x:x+w]
    f_color = img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(f_gray, 1.05, 4)

    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(img, (x+ex,y+ey), (x+ex+ew, y+ey+eh), (255, 0, 0), 2)

cv.imshow('detected', img)
cv.waitKey(0)
cv.destroyAllWindows()
