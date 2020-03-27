import numpy as np
import cv2 as cv
import matplotlib.pylab as plt

def region_mask(img, vertices):
    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    mask_color = (255)  #  * channel_count
    cv.fillPoly(mask, vertices, mask_color)
    masked_img = cv.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines):
    img = np.copy(img)
    line_img = np.zeros(img.shape, np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 1)

    img = cv.addWeighted(img, 0.5, line_img, 0.5, 10)
    return img

image = cv.imread('used_images_videos/roads.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

h = image.shape[0]
w = image.shape[1]

interest_region = [
    (451, 221),
    (0, 440),
    (0, h),
    (w, h),
    (w, 440)
]

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 175, 250, apertureSize=3)
cv.imshow('edges', edges)
crpd = region_mask(edges, np.array([interest_region], np.int32))
lines = cv.HoughLinesP(crpd, 6, np.pi/60, 160, lines=np.array([]), minLineLength=40, maxLineGap=25)
with_lines = draw_lines(image, lines)

plt.imshow(crpd)
plt.imshow(with_lines)
plt.show()