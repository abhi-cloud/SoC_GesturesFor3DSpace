import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output2.avi', fourcc, 20.0, (640, 480))

while(cap.isOpened()):
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)	# 3-way channel to 1-channel
	gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)   # pixels remain gray but the img is converted back to 3 way channel
													# out.write() expects 3-way channel
	""" 											
	print (cap.get(cv2.CAP_PROP_FRAME_HEIGHT))    # gives height and width of the frame
	print (cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	"""

	cv2.imshow('frame', frame)

	out.write(gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
out.release()
cv2.destroyAllWindows()

