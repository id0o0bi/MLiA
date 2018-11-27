import cv2
import numpy as np

# create image background
img = np.zeros((720,960,3), np.uint8)

# draw line
cv2.line(img, (0,0), (478,478), (255,0,0), 3)

# draw rectangle
cv2.rectangle(img, (50, 50), (300, 200), (255,255,0), 2)

# draw circle
cv2.circle(img, (300, 200), 120, (0,255,255), 2)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()