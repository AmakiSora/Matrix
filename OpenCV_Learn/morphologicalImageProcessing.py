"""
    形态学图像处理
"""
import cv2
import numpy

img = cv2.imread('img.jpg')
# 原图展示
cv2.imshow("img", img)

# 创建核结构
kernel = numpy.ones((5, 5), numpy.uint8)

# # 腐蚀
# erosion = cv2.erode(img, kernel)
# # 膨胀
# dilate = cv2.dilate(img, kernel)
#
# cv2.imshow("erosion", erosion)
# cv2.imshow("dilate", dilate)
# cv2.waitKey(0)
#
# # 开运算(即先侵蚀后膨胀,消除噪点用)
# cvOpen = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# # 闭运算(即先膨胀后侵蚀,填充孔洞用)
# cvClose = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#
# cv2.imshow("cvOpen", cvOpen)
# cv2.imshow("cvClose", cvClose)
# cv2.waitKey(0)
#
# # 礼帽运算(原图像与开运算的结果图之差)
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# # 黑帽运算(闭运算的结果图与原图像之差)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
#
# cv2.imshow("tophat", tophat)
# cv2.imshow("blackhat", blackhat)
# cv2.waitKey(0)

'''
    均值滤波(用于消除噪声)
    src:图像
    ksize:卷积核
    anchor:默认(-1,1),表示核中心
    borderType:填充边界类型
'''
blur = cv2.blur(img, (5, 5))
cv2.imshow("blur", blur)
cv2.waitKey(0)

'''
    高斯滤波(用于消除噪声)
    src:图像
    ksize:卷积核
    sigmaX:水平方向标准差
    sigmaY:垂直方向标准差
    borderType:填充边界类型
'''
gaussianBlur = cv2.GaussianBlur(img, (3, 3), 1)
cv2.imshow("gaussianBlur", gaussianBlur)
cv2.waitKey(0)

'''
    中值滤波(用于消除噪声)
    src:图像
    ksize:卷积核
'''
medianBlur = cv2.medianBlur(img, 5)
cv2.imshow("medianBlur", medianBlur)
cv2.waitKey(0)
