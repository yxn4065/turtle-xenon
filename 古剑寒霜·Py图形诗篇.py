import turtle as t
import cv2

# 设置画布背景色
t.getscreen().colormode(255)
# 加载图片并缩小
img1 = cv2.imread('image.jpg')[0: -2: 2]
width = len(img1[0])  # 图片宽度
height = len(img1)  # 图片高度

# 设置画布大小
t.setup(width=width / 2 + 100, height=height + 100)
t.pu()  # 提起画笔
t.goto(-width / 4 + 10, height / 2 - 10)  # 移动到起始位置
t.pd()  # 放下画笔
# 设置Turtle绘制速度
t.tracer(2000)
# 遍历图片的每个像素并使用turtle绘制
for k1, i in enumerate(img1):
    for j in i[::2]:  # 每隔一个像素绘制
        t.pencolor((j[0], j[1], j[2]))  # 设置画笔颜色
        t.fd(1)  # 前进一个单位
    t.pu()  # 提起画笔
    t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)  # 移动到下一行的起始位置
    t.pd()  # 放下画笔

t.done()  # 完成绘制,等待用户关闭窗口

