"""
    霍夫线变换
    Hough线变换是一种用于检测直线的变换
    它最大的优点是,即使是虚线,或者某些部分缺失,被遮挡的直线,也能检测到完整的线条
"""
import cv2
import numpy

img = cv2.imread('img.jpg', cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img, 50, 150)
cv2.imshow("edges", edges)
cv2.waitKey(0)

'''
    cv2.HoughLines(img,rho,theta,threshold)
    在调用霍夫线变换前,先要进行二值化,或者进行Canny边缘检测
    img:图像,要求是二值化的图像
    rho:ρ,以像素为单位的累加器的距离分辨率,推荐1.0
    theta:θ,以弧度表示的累加器角度分辨率,CV_PI/180
    threshold:阈值,只有累加器中的值高于该阈值才被认为是直线
'''
# 检测
lines = cv2.HoughLinesP(edges, 1, numpy.pi / 180, 10)

# 将检测到的线绘制在图像上(极坐标)
for line in lines:
    rho, theta = line[0]
    a = numpy.cos(theta)
    b = numpy.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 + 1000 * (-b))
    y2 = int(y0 + 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0))
cv2.imshow('233', img)
cv2.waitKey(0)
