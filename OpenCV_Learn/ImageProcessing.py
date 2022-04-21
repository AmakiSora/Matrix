"""
    图像处理
"""

import cv2

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
