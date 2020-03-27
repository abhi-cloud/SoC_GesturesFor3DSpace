import numpy as np
import cv2 as cv

apple = cv.imread('used_images_videos/apple.jpg')
orange = cv.imread('used_images_videos/orange.jpg')
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

# gaussian pyr for apple
apple_cpy = apple.copy()
apple_gp = [apple_cpy]
for i in range(6):
    apple_gp.append(cv.pyrDown(apple_gp[i]))

# gaussian pyr for orange
orange_cpy = orange.copy()
orange_gp = [orange_cpy]
for i in range(6):
    orange_gp.append(cv.pyrDown(orange_gp[i]))

# laplacian pyr for apple
apple_lp = [apple_gp[5]]
for i in range(5, 0, -1):
    lap = cv.subtract(apple_gp[i-1], cv.pyrUp(apple_gp[i]))
    apple_lp.append(lap)

# laplacian pyr for orange
orange_lp = [orange_gp[5]]
for i in range(5, 0, -1):
    lap = cv.subtract(orange_gp[i-1], cv.pyrUp(orange_gp[i]))
    orange_lp.append(lap)

# Add left and right halves at each level
apple_orange_pyr = []
n = 0

for apple_lap, orange_lap in zip(apple_lp, orange_lp):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyr.append(laplacian)
    # cv.imshow(str(n), apple_orange_pyr[n-1])

# now reconstruct
ap_or_reconstruct = apple_orange_pyr[0]
for i in range(1, 6):
    ap_or_reconstruct = cv.pyrUp(ap_or_reconstruct)
    ap_or_reconstruct = cv.add(apple_orange_pyr[i], ap_or_reconstruct)


cv.imshow('blended_reconstruct', ap_or_reconstruct)
cv.imshow('cutNadd', apple_orange)
cv.waitKey(0)
cv.destroyAllWindows()
