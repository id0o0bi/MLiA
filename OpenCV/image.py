import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread('OpenCV/shark.jpg', cv2.IMREAD_GRAYSCALE)

plt.imshow(im, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()