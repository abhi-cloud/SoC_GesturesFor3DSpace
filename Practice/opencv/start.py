import cv2

img = cv2.imread('used_images_videos/lena.jpg', 1)
print(img)

cv2.imshow('image', img)

k = cv2.waitKey(0) & 0xFF  # mask for 64-bit machines

if k == 27:
	cv2.destroyAllWindows()
	
elif k == ord('s'):
	cv2.imwrite('lenacpy.png', img)
	cv2.destroyAllWindows()