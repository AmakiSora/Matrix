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
img = cv2.imread('Img.jpg', cv2.IMREAD_UNCHANGED)  # 如果加载的路径有误,会返回None
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
