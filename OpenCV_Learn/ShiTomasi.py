"""
    Shi-Tomasi角点检测
"""
import cv2

img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

'''
    cv2.goodFeaturesToTrack(Image,maxCorners,qualityLevel,minDistance)
    Image:灰度图像
    maxCorners:获取角点数的数目
    qualityLevel:指出最低可接受的角点质量水平,取值0-1之间
    minDistance:角点之间最小的欧式距离,避免得到相邻的特征点
'''
# 角点检测
corners = cv2.goodFeaturesToTrack(gray, 1000, 0.01, 10)
# 将角点绘制出来
for i in corners:
    x, y = i.ravel()
    x = int(x)
    y = int(y)
    cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
# 显示
cv2.imshow("corners", img)
cv2.waitKey(0)
