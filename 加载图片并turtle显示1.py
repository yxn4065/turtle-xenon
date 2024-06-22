import turtle
import cv2
import numpy as np

# 加载并处理图片
image = cv2.imread(r"C:\Users\yxn\Downloads\111.jpg", 0)  # 加载为灰度图像
blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred, 100, 200)  # 提取轮廓

# 简化轮廓（可选步骤，具体实现取决于你选择的算法）
# 这里我们直接使用Canny边缘检测的结果，不进行进一步简化

# 使用turtle进行绘画
turtle.speed(0)  # 设置绘制速度最快
turtle.bgcolor('white')  # 设置画布背景色

# 获取图像尺寸并调整turtle的坐标系统
height, width = edges.shape
turtle.setup(width=width, height=height)
turtle.screensize(width, height)

print("height:", height)
# 绘制轮廓
for y in range(height):
    for x in range(width):
        if edges[y, x] != 0:  # 如果当前点是轮廓的一部分
            turtle.penup()
            turtle.goto(-width // 2 + x, height // 2 - y)  # 调整坐标系统
            turtle.pendown()
            turtle.dot(1)  # 在轮廓点上画一个点

# 完成绘制
turtle.done()
