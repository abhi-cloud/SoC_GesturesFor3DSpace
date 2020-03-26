import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
""" 
LPF(Low Pass Filter) helps in removing the noise from the image
HPF helps in finding the edges in the image 
"""

img = cv.imread('used_images_videos/lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25  # homogeneous filter kernel
""" 
kernal = [1 1 . . . 1]       /
         |1 .       1|      / kwidth * kheight
         |1 .       1|     /
         [1 1 . . . 1]    /
 """

dst = cv.filter2D(img, -1, kernel)

blur = cv.blur(img, (5, 5))
# simple averaging filter

gblur = cv.GaussianBlur(img, (5, 5), 0) # they have kernel which have lower weight as we go away from center
# sigmax, y can be specified, used to remove very high frequency noises in between the images

median = cv.medianBlur(img, 5)
# replaces the pixel value  with the median of pixels in the kernel
# great with salt and pepper noise
# i.e. a noise tjhat is due to  sharp and sudden disturbances in the image signal. 
# It presents itself as sparsely occurring white and black pixels.

bilateral = cv.bilateralFilter(img, 9, 75, 75)
# preserves the edges by taking one more gaussian filter which is function 
# of pixel difference (but slower than the other filters)


titles = ['image', '2D Convulution', 'blur', 'gblur', 'median', 'bilateral']
images = [img, dst, blur, gblur, median, bilateral]

for i in range(len(images)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()