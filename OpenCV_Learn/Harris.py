"""
    Harris角点检测
"""
import cv2
import matplotlib as matplotlib
import numpy

gray_img = cv2.imread('img.jpg')
gray = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

'''
    cv2.(img,blockSize,ksize,k)
    img:图像,要求是float32
    blockSize:角点检测中要考虑的邻域大小
    ksize:sobel求导使用的核大小
    k:角点检测方程中的自由参数,取值为[0.04,0.06]
'''
# 转换为float32
gray = numpy.float32(gray_img)
# 检测
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
# 设置阈值,将角点绘制出来
gray_img[dst > 0.001 * dst.max()] = [0, 0, 255]

# 显示

cv2.imshow("Harris", gray_img)
cv2.waitKey(0)
