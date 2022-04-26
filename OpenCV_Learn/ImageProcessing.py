"""
    图像处理
"""

import cv2
import numpy

'''
    读取图像
    imread('路径',模式)
    模式:
        cv2.IMREAD_COLOR 彩色,忽略透明度没,默认
        cv2.IMREAD_GRAYSCALE 灰度
        cv2.IMREAD_UNCHANGED 包括alpha通道
'''
img = cv2.imread('img.jpg', cv2.IMREAD_UNCHANGED)  # 如果加载的路径有误,会返回None

'''
    显示图像
    imshow('显示名',图片对象)
'''
cv2.imshow('test', img)
cv2.waitKey(0)  # 等待键盘响应

'''
    保存图像
    imwrite('文件名',图片对象)
'''
cv2.imwrite('test', img)

'''
    修改图中像素点
'''
for i in range(500):
    img[i, i] = [255, 255, 255]  # 蓝,绿,红
cv2.imshow('test', img)
cv2.waitKey(0)

'''
    获取图像属性
'''
print(img.shape)  # 行数,列数,通道数
print(img.size)  # 图片大小
print(img.dtype)  # 图片类型

'''
    图像通道拆分与合并
'''
b, g, r = cv2.split(img)
cv2.imshow('b', b)
cv2.waitKey(0)

cv2.imshow('g', g)
cv2.waitKey(0)

cv2.imshow('r', r)
cv2.waitKey(0)

mergeImg = cv2.merge((b, g, r))
cv2.imshow('mergeImg', mergeImg)
cv2.waitKey(0)

'''
    改变图像的色彩空间
    OpenCV中有150多种颜色空间的转换方法,最广泛使用的有两种
    cv2.COLOR_BGR2GRAY  BGR <-> Gray
    cv2.COLOR_BGR2HSV   BGR <-> HSV
'''
c1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('mergeImg', c1)
cv2.waitKey(0)
c2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('mergeImg', c2)
cv2.waitKey(0)

'''
    图像加法
    要求图像大小一致
'''
addImg = cv2.add(img, img)  # cv2的加法是数组对应位置相加,超过255则为255
cv2.imshow('mergeImg', addImg)
cv2.waitKey(0)

addImg = img + img  # 直接相加,超过255的数值会取模
cv2.imshow('mergeImg', addImg)
cv2.waitKey(0)

'''
    图像混合
    两幅图按不同的比例进行相加
'''
mixImg = cv2.addWeighted(img, 0.7, img, 0.3, 0)  # (图像1,比重1,图像2,比重2,伽马值)

'''
    图像缩放
    dsize: 绝对尺寸,直接指定调整后图像大小
    fx,fy: 相对尺寸,将dsize设置为None,然后fx和fy设置为比例因子即可
    interpolation: 插值方法
        cv2.INTER_LINEAR        双线性插值法
        cv2.INTER_NEAREST       最近邻插法
        cv2.INTER_AREA          像素区域重采样(默认)
        cv2.INTER_CUBIC         双三次插值
'''
res1 = cv2.resize(img, (800, 500), interpolation=cv2.INTER_LINEAR)  # (图像,绝对尺寸,相对尺寸x,相对尺寸y,插值方法)
res2 = cv2.resize(img, (800, 500), interpolation=cv2.INTER_NEAREST)
res3 = cv2.resize(img, (800, 500), interpolation=cv2.INTER_AREA)
res4 = cv2.resize(img, (800, 500), interpolation=cv2.INTER_CUBIC)
res5 = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
cv2.imshow("1", res1)
cv2.imshow("2", res2)
cv2.imshow("3", res3)
cv2.imshow("4", res4)
cv2.imshow("5", res5)
cv2.waitKey(0)

'''
    图像平移
'''
M = numpy.float32([[1, 0, 100], [0, 1, 50]])  # 平移矩阵
wa = cv2.warpAffine(img, M, (500, 500))  # (图像,移动矩阵,图像大小)
cv2.imshow("img", img)
cv2.imshow("wa", wa)
cv2.waitKey(0)

'''
    图像旋转
    center: 旋转中心
    angle: 旋转角度
    scale: 缩放比例
'''
rows, cols = img.shape[:2]
RM = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)  # (旋转中心,旋转角度,缩放比例)
rm = cv2.warpAffine(img, RM, (cols, rows))
cv2.imshow("rm", rm)
cv2.waitKey(0)

'''
    仿射变换
'''
rows, cols = img.shape[:2]
pts1 = numpy.float32([[50, 50], [200, 50], [50, 200]])
pts2 = numpy.float32([[100, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('dst', dst)
cv2.waitKey(0)

'''
    投射变换
'''
rows, cols = img.shape[:2]
pts1 = numpy.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = numpy.float32([[100, 145], [300, 100], [80, 290], [310, 300]])
T = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, T, (cols, rows))
cv2.imshow('dst', dst)
cv2.waitKey(0)

'''
    图像金字塔
'''
up_img = cv2.pyrUp(img)  # 上采样操作
down_img = cv2.pyrDown(img)  # 下采样操作
cv2.imshow('up_img', up_img)
cv2.imshow('down_img', down_img)
cv2.waitKey(0)
