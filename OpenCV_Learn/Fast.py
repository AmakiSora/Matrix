"""
    Fast算法关键点检测
"""
import cv2

img = cv2.imread('img.jpg')
cv2.imshow("img", img)
cv2.waitKey(0)

# 创建fast对象(可以处理彩色图像)
fast = cv2.FastFeatureDetector_create(threshold=30)

# 关闭极大值抑制
# fast.setNonmaxSuppression(0)

'''
    关键点检测
    kp = fast.detect(img,mask)
    kp:关键点信息
'''
kp = fast.detect(img, None)

'''
    绘制关键点
'''
cv2.drawKeypoints(img, kp, img, color=(0, 0, 255))

# 显示
cv2.imshow("SIFT", img)
cv2.waitKey(0)
