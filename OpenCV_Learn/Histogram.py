"""
    直方图
"""
import cv2
import matplotlib.pyplot as plt
import numpy

img = cv2.imread('img.jpg')
# 原图展示
cv2.imshow("img", img)

'''
    直方图的绘制
    参数:
        images: 图像
        channels: 如果是灰度图,入参为[0];如果是彩色图像,入参可以是[0],[1],[2]
        mask: 掩膜图像
        histSize: BIN的数目
        ranges: 像素值范围,通常为[0,256]
'''
histr = cv2.calcHist(img, [3], None, [256], [0, 256])
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(histr)
plt.grid()
plt.show()
cv2.waitKey(0)

'''
    掩膜
    盖住一部分图像
'''
# 创建蒙版
mask = numpy.zeros(img.shape[:2], numpy.uint8)
mask[400:650, 200:500] = 1

# 掩膜
masked_img = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("masked_img", masked_img)
mask_histr = cv2.calcHist([img], [0], mask, [256], [0, 256])  # 注意，第一个参数要加[]
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(mask_histr)
plt.grid()
plt.show()
cv2.waitKey(0)

'''
    直方图均值化
'''
img_gray = cv2.imread('img.jpg', 0)  # 以灰度图读入
cv2.imshow("img_gray", img_gray)
histr_gray = cv2.calcHist(img_gray, [0], None, [256], [0, 256])
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(histr_gray)
plt.grid()
plt.show()
# 均值化
dst = cv2.equalizeHist(img_gray)
cv2.imshow("img_dst", dst)
histr_gray_dst = cv2.calcHist(dst, [0], None, [256], [0, 256])
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(histr_gray_dst)
plt.grid()
plt.show()
cv2.waitKey(0)

'''
    自适应均值化
    将图像分成多个小块进行均值化
    clipLimit: 对比度限制,默认为40
    tileGridSize: 分块大小,默认8X8
'''
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img_gray)
cv2.imshow("img_clahe", cl1)
histr_gray_clahe = cv2.calcHist(cl1, [0], None, [256], [0, 256])
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(histr_gray_clahe)
plt.grid()
plt.show()
cv2.waitKey(0)
