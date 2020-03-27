import cv2

cap = cv2.VideoCapture(0)   # in the parameters we can also specify the video path to open an existing video
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1280)    # here the numbers 3, 4 represents the CAP_FRAME_PROP_WIDTH/HEIGHT
cap.set(4, 960)     # could have written cv2.CAP_FRAME_PROP_WIDTH etc       

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_DUPLEX
        text = 'Width: ' + str(cap.get(3)) + 'Heigth: ' + str(cap.get(4))

        frame = cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()

""" 
We can get current date/time by datetime.datetime.now().
And similarly we can add shapes to the frame as frame is nothing but a image which can be edited
just as in the geometric_shapes.py file.
 """