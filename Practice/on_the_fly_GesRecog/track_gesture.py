import cv2 as cv
import numpy as np
import os
import time

import threading

import gestureCNN as nn

# region of interest (roi)
x0 = 400
y0 = 200
height = 200
width =200
thresh_minvalue = 70

save_image = False
guess_gesture = False
visualize = False

skinkernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))

# modes controllers
binary_mode = True
bgdSub_mode = False
flip = False
mask = 0
bgd = 0

# for generarting dataset of our own
counter = 0
max_images_at_once = 25
gest_name = ""
path = ""

# model to be trained/loaded
mod = 0

banner =  '''What task you want to perform?
    1- Use pretrained model for recognotion/visualization
    2- Train the model (try after saving new images)
    3- Visualiize feature maps of different layers
    '''

def saveROI(img):
    global counter, gest_name, path, save_image
    if counter >= (max_images_at_once):
        save_image = False
        gest_name = ""
        counter = 0
        return

    counter += 1
    name = gest_name + str(len(os.listdir(path)))
    print('Saving img:', name)
    cv.imwrite(path+name+".jpg", img)
    time.sleep(0.04)

def skinMask(roi, framecount):
    global guess_gesture, visualize, mod, save_image

    # HSV values "skin" color
    lower = np.array([0, 50, 80])
    upper = np.array([30, 200, 255])
    
    hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, lower, upper)

    mask = cv.erode(mask, skinkernel, iterations=1)
    mask = cv.dilate(mask, skinkernel, iterations=1)

    mask = cv.GaussianBlur(mask, (15, 15), 1)

    res = cv.bitwise_and(roi, roi, mask=mask)
    res = cv.cvtColor(res, cv.COLOR_BGR2GRAY)

    if guess_gesture and (not framecount % 5):
        t= threading.Thread(target=nn.guessGesture, args=[mod, res])
        t.start()
    elif visualize:
        pass
        # layer = int(input("Enter which layer to visualize"))
        # cv.waitKey(0)
        # nn.visualizeLayers(mod, res, layer)
        # visualize = False

    return res

def binaryMask(roi, framecount):
    global guess_gesture, visualize, mod, save_image

    gray = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 2)

    th3 = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv.THRESH_BINARY_INV, 3, 1)
    ret, res = cv.threshold(th3, thresh_minvalue, 255,
                            cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    if guess_gesture and (not framecount % 5):
        # t = threading.Thread(target=nn.guessGesture, args=[mod, res])
        # t.start()
        nn.guessGesture(mod, res)
    elif visualize:
        pass
        # layer = int(input("Enter which layer to visualize"))
        # cv.waitKey(0)
        # nn.visualizeLayers(mod, res, layer)
        # visualize = False

    return res

def bgdSubMask(roi, framecount):
    global guess_gesture, change_bgd, visualize, mod, bgd, save_image

    roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)

    # changing background
    if change_bgd:
        bgd = roi
        change_bgd = False
        print('changing background...')
    
    diff = cv.absdiff(roi, bgd)

    _, diff = cv.threshold(diff, 25, 255, cv.THRESH_BINARY)

    mask = cv.GaussianBlur(diff, (3,3), 5)
    mask = cv.erode(diff, skinkernel, iterations=1)
    mask = cv.dilate(diff, skinkernel, iterations=1)
    res = cv.bitwise_and(roi, roi, mask=mask)

    if guess_gesture and (not framecount % 5):
        t = threading.Thread(target=nn.guessGesture, args=[mod, res])
        t.start()

    elif visualize:
        pass
        # layer = int(input("Enter which layer to visualize"))
        # cv.waitKey(0)
        # nn.visualizeLayers(mod, res, layer)
        # visualize = False

    return res

def Main():
    global flip, change_bgd, binary_mode, guess_gesture, visualize, mod, bgdSub_mode, mask, change_bgd
    global x0, y0, width, height, save_image, gest_name, path

    quite_mode = False



    while True:
        ans = int(input(banner))
        if ans == 1:
            mod = nn.loadCNN()
            break
        else:
        	print('BYE!')
        	return 0

    cap = cv.VideoCapture(0)
    cv.namedWindow('Original', cv.WINDOW_NORMAL)

    ret = cap.set(3, 640)
    ret = cap.set(4, 480)

    framecount = 0
    fps = ""
    start = time.time()

    while True:
        ret, frame = cap.read()

        frame = cv.flip(frame, 3)
        frame = cv.resize(frame, (640, 480))
        cv.rectangle(frame, (x0, y0), (x0+width, y0+height), (0,255,0), 1)

        roi = frame[y0:y0+height, x0:x0+width]

        if ret == True:
            if bgdSub_mode:
                roi = bgdSubMask(roi, framecount)
            elif binary_mode:
                roi = binaryMask(roi, framecount)
            else:
                roi = skinMask(roi, framecount)
        
        framecount += 1
        end = time.time()
        if(end - start >= 1):
            fps = 'FPS:%s' %(framecount)
            start = time.time()
            framecount = 0
    
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        size = 0.7
        fx, fy, fh = 10, 350, 18
        color = (0, 255, 0)

        
        cv.putText(frame, fps, (10,20), font, size, color, 2, 1)
        cv.putText(frame, 'Options:', (fx, fy), font, size, color, 2, 1)
        cv.putText(frame, 'b- Toggle Binary/SkinMask', (fx, fy+fh), font, size, color, 2, 1)
        cv.putText(frame, 'x- Toggle Background SubMask:', (fx, fy+2*fh), font, size, color, 2, 1)
        cv.putText(frame, 'g- Toggle Prediction Mode', (fx, fy+3*fh), font, size, color, 2, 1)
        cv.putText(frame, 'q- Toggle Quiet Mode', (fx, fy+4*fh), font, size, color, 2, 1)
        cv.putText(frame, 'n- To enter name of new gesture folder', (fx, fy+5*fh), font, size, color, 2, 1)
        cv.putText(frame, 's- To start capturing new gestures', (fx, fy+6*fh), font, size, color, 2, 1)
        cv.putText(frame, 'Esc - exit', (fx, fy+7*fh), font, size, color, 1, 1)

        if flip:
        	roi = roi[:,-1::-1]
        if save_image:
        	saveROI(roi)

        if not quite_mode:
            cv.imshow('Original', frame)
            cv.imshow('ROI', cv.resize(roi, (400, 400)))

            if guess_gesture:
                plot = np.zeros((512, 512, 3), np.uint8)
                plot = nn.update(plot)
                cv.imshow('Gesture Probability', plot)

        ##Key functions##
        key = cv.waitKey(5) & 0xff

        if key == 27:
            break

        elif key == ord('b'):
            binary_mode = not binary_mode
            bgdSub_mode = False
            if binary_mode:
                    print("Binary Threshold filter active")
            else:
                print("SkinMask filter active")
        
        elif key == ord('x'):
            change_bgd = True
            bgdSub_mode = True
            print("BgdSubMask filter active")
        
        elif key == ord('g'):
            guess_gesture = not guess_gesture
            print("Prediction Mode - {}".format(guess_gesture))
        
        elif key == ord('i'):
            y0 = y0 - 5
        elif key == ord('k'):
            y0 = y0 + 5
        elif key == ord('j'):
            x0 = x0 - 5
        elif key == ord('l'):
            x0 = x0 + 5

        elif key == ord('q'):
            quite_mode = not quite_mode
            print("Quiet Mode - {}".format(quite_mode))
        
        elif key == ord('s'):
            save_image = not save_image
            
            if gest_name != '':
                save_image = True
            else:
                print("Enter a gesture group name first, by pressing 'n'")
                save_image = False

        elif key == ord('n'):
            gest_name = input("Enter the gesture folder name: ")
            
            if not os.path.isdir(os.path.join('./test' ,gest_name)):
                os.makedirs(os.path.join('./test' ,gest_name))
            
            path = "./test/"+gest_name+"/"

        elif key == ord('f'):
        	flip = not flip
        	if flip:
        		print('Flipping ON...')
        	else:
        		print('Flipping OFF...')

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    Main()