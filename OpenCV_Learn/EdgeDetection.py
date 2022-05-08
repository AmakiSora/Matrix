"""
    边缘检测
"""
import cv2

img = cv2.imread('img.jpg')
# 原图展示
cv2.imshow("img", img)

'''
    Sobel检测算子
    相比于Canny算法,效率高,但准确度不如Canny算法
    Sobel算子是高斯平滑与微分操作的结合体,所以其抗噪声能力很强
    API参数:
        src:传入的图像
        ddepth:图像深度
        dx,dy:求导的阶数,0表示此方向上没有求导,取值为0,1
        ksize:Sobel算子的大小,即卷积核的大小,必须为奇数1,3,5,7,默认为3,如果为-1,就演变成为3x3的Scharr算子
        scale:缩放导数的比例常数,默认情况为没有伸缩系数
        borderType:图像边界的模式,默认为cv2.BORDER_DEFAULT
'''
# 计算Sobel卷积结果
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
# 将数据进行转换
scale_absX = cv2.convertScaleAbs(x)
scale_absY = cv2.convertScaleAbs(y)
# 将两个方向合成
result = cv2.addWeighted(scale_absX, 0.5, scale_absY, 0.5, 0)
cv2.imshow("Sobel", result)
cv2.waitKey(0)

# 利用Scharr算子检测
x = cv2.Sobel(img, cv2.CV_16S, 1, 0, ksize=-1)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1, ksize=-1)
# 将数据进行转换
scale_absX = cv2.convertScaleAbs(x)
scale_absY = cv2.convertScaleAbs(y)
# 将两个方向合成
result = cv2.addWeighted(scale_absX, 0.5, scale_absY, 0.5, 0)
cv2.imshow("Scharr", result)
cv2.waitKey(0)

'''
    laplacian算子
    利用二阶导数来检测边缘
    API参数:
        src:图像
        Ddepth:图像深度,-1表示采用的是与原图像相同的深度,目标图像的深度必须大于等于原图像的深度
        ksize:算子的大小,即卷积核的大小,必须为奇数1,3,5,7
'''
result = cv2.Laplacian(img, cv2.CV_16S)
scale_abs = cv2.convertScaleAbs(result)
cv2.imshow("laplacian", scale_abs)
cv2.waitKey(0)

'''
    Canny边缘检测算法
    最优的检测算法
    4个步骤:
        1.噪声去除
        2.计算图像梯度
        3.非极大值抑制
        4.滞后阈值
    API参数:
        image:灰度图
        threshold1:最小值,较小的阈值将间断的边缘连接起来
        threshold2:最大值,较大的阈值检测图像中明显的边缘
'''
canny = cv2.Canny(img, 0, 100)
cv2.imshow("canny", canny)
cv2.waitKey(0)
