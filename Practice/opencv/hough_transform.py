import numpy as np
import cv2 as cv

img = cv.imread('used_images_videos/sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 38, 80, apertureSize=3)

# # Standard Hough Transform
# lines = cv.HoughLines(edges, 1, np.pi/180, 200) # gives detected set of lines, each line is a set of points with each point of form(r, theta, votes)

# for line in lines:
#     # print(line)
#     r, theta = line[0]
#     x0 = r * np.cos(theta)
#     y0 = r * np.sin(theta)
#     x1 = int(x0 - 1000 * np.sin(-theta))
#     y1 = int(y0 - 1000 * np.cos(theta))
#     x2 = int(x0 + 1000 * np.sin(-theta))
#     y2 = int(y0 + 1000 * np.cos(theta))

#     cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

# Probabilistic Hough Line Transform
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=20)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv.imshow('canny', edges)
cv.imshow('detected edge lines', img)
cv.waitKey(0)
cv.destroyAllWindows()