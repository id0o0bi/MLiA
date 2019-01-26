'''
Detect Edges in an Image and extract Content
'''
# pylint: disable=invalid-name
import cv2
import numpy as np
# import sys

def find_piece(img):
    '''
    find the jigsaw puzzle piece in an image with white background
    Basicly, this funciton removes the white background and replace it with back color
    so we can use edge detection more effciently!
    '''
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # img_blur = cv2.GaussianBlur(img_hsv, (7, 7), 0)
    # print(img_blur.shape) (720, 540, 3)

    for idx_i, val_i in enumerate(img):
        for idx_j, val_j in enumerate(val_i):
            if np.var(val_j) < 20 and val_j[0] > 180:
                img[idx_i][idx_j] = (0, 0, 0)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

def find_edges(img):
    '''
    This function detect image edges using Gaussion Blur && Canny Edge Detection
    '''
    # 1. 滤波，高斯滤波
    img = cv2.GaussianBlur(img, (3, 3), 0)
    # 2. 增强，LapLace图像增强
    kernel = np.ones((3, 3), np.float32)/9
    img = cv2.filter2D(img, -1, kernel)
    # 3. dilation and erosion
    kernel = np.ones((5, 5), np.uint8)
    erossion = cv2.erode(img, kernel, iterations=1)
    dialation = cv2.dilate(erossion, kernel, iterations=1)
    # 4. 检测，Canny边缘检测
    canny = cv2.Canny(dialation, 50, 200)
    #提取轮廓
    _, contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = len(contours)
    print('轮廓集合：%d 个'%count)

    # 标记
    # maxArea = 0
    # for i in range(0, count):
    #     area = cv2.contourArea(contours[i])
    #     if area > maxArea:
    #         maxIndx = i
    #         maxArea = area
    img = cv2.drawContours(dialation, contours, -1, (0, 0, 255), 1)
    return img

image = cv2.imread('imgs/jig003.jpeg')
piece = find_piece(image)
edges = find_edges(piece)

while True:
    cv2.imshow('image', image)
    cv2.imshow('piece', piece)
    cv2.imshow('edges', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cv2.waitKey(27)
# cv2.destroyAllWindows()
