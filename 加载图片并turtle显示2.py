# 导入必要的库  
import turtle as t
import cv2

# 设置画布背景色为RGB模式  
t.getscreen().colormode(255)

# 加载并缩小图片，这里简单地下采样图片以减少绘制量  
img1 = cv2.imread('image.jpg')[0: -2: 2]  # 读取并下采样图片  
width = len(img1[0])  # 获取图片宽度  
height = len(img1)  # 获取图片高度  

# 设置Turtle画布大小和初始画笔状态  
t.setup(width=width / 2 + 100, height=height + 100)  # 设置画布大小  
t.pu()  # 提起画笔，移动到起始位置  
t.goto(-width / 4 + 10, height / 2 - 10)
t.pd()  # 放下画笔，准备绘制  
t.tracer(2000)  # 设置Turtle的绘制速度优化显示过程  

# 遍历图片的每个像素并使用Turtle进行绘制  
for k1, i in enumerate(img1):  # 枚举图片的每一行  
    for j in i[::2]:  # 枚举当前行的每个像素（隔列采样）  
        t.pencolor((j[0], j[1], j[2]))  # 设置画笔颜色为当前像素颜色  
        t.fd(1)  # 前进一个单位，代表绘制一个像素点  
    t.pu()  # 一行绘制完成后提起画笔  
    t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)  # 移动到下一行的起始位置  
    t.pd()  # 放下画笔，继续绘制下一行  

t.done()  # 绘制完成，等待用户关闭窗口
