#!/usr/bin/env python
#-*- coding=utf8 -*-

import cv2
import numpy

img = cv2.imread('imgs/jig03.jpeg')

### 1. 滤波，高斯滤波
img = cv2.GaussianBlur(img, (3,3),0)

### 2. 增强，LapLace图像增强
kernel = numpy.ones((3,3), numpy.float32)/9
img = cv2.filter2D(img, -1, kernel)

### 3. 检测，Canny边缘检测
canny = cv2.Canny(img, 50, 150)

#提取轮廓
_,contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print('轮廓集合：%d 个'%len(contours))
# 标记
cv2.drawContours(img,contours,-1,(0,0,255),2)

# # 标记最大区域
# maxArea = 0
# maxAreaIndex = -1
# for i in range(0, len(contours)):
# 	contour = contours[i]
# 	area = cv2.contourArea(contour)
# 	if area > maxArea:
# 		maxArea = area
# 		maxAreaIndex = i
# cv2.drawContours(img,contours,maxAreaIndex,(0,255,0),2)
cv2.namedWindow('img')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite('out.jpg', canny)