"""
    SIFT算法关键点检测
"""
import cv2

img = cv2.imread('img.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)
cv2.waitKey(0)

# 实例化sift对象
sift = cv2.SIFT_create()

'''
    关键点检测
    kp, des = sift.detectAndCompute(img,mask)
    kp:关键点信息
    des:关键点描述符,每个关键点对应128个梯度信息的特征向量
'''
kp, des = sift.detectAndCompute(gray, None)

'''
    绘制关键点
    cv2.drawKeypoints(img,keyPoints,outImg,color,)
    img:原始图像
    keyPoints:关键点信息
    outImg:输出图像
    color:颜色设置
    flags:绘图功能的标识设置
        DRAW_MATCHES_FLAGS_DEFAULT
            创建输出图像矩阵,使用现存的输出图像绘制匹配对和特征点,对每个关键点只绘制中间点
        DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
            对每一个特征点绘制带大小和方向的关键点图形
        DRAW_MATCHES_FLAGS_DRAW_OVER_OUTIMG
            不创建输出图像矩阵,而是在输出图像上绘制匹配对
        DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
            单点的特征点不被绘制 
'''
cv2.drawKeypoints(img, kp, img, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# 显示
cv2.imshow("SIFT", img)
cv2.waitKey(0)
