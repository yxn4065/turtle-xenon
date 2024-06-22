import tkinter as tk
import tkinter.filedialog
import turtle as t  # 导入turtle模块，命名为t
import cv2  # 导入OpenCV模块，命名为cv2
def hua(path):
    t.getscreen().colormode(255)  # 设置画布颜色模式为RGB的0-255模式
    img1 = cv2.imread(path)[0: -2: 2]  # 读入图像，每隔2行2列读取一个像素点，裁剪最后两行
    width = len(img1[0])  # 获取图像的列数，即宽度
    height = len(img1)  # 获取图像的行数，即高度
    t.setup(width=width / 2 + 100, height=height + 100)  # 设置画布宽和高
    t.pu()  # 抬起画笔
    t.goto(-width / 4 + 10, height / 2 - 10)  # 将画笔移动到左上角起点处
    t.pd()  # 放下画笔
    t.tracer(2000)  # 设置绘制的速度为2000
    for k1, i in enumerate(img1):  # 遍历每一行
        for j in i[::2]:  # 每隔一个像素点遍历一次列
            t.pencolor((j[0], j[1], j[2]))  # 获取当前像素点的颜色，设置为画笔颜色
            t.fd(1)  # 前进一个像素点的距离
        t.pu()  # 抬起画笔
        t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)  # 移动到下一行的起点处
        t.pd()  # 放下画笔
    t.done()  # 绘制完成，关闭绘图窗口
gu=tk.Tk()
gu.geometry("200x100")
gu.title("             turtle画图片")
def tu():
    kuang.delete(0,"end")  #删除上次
    ts=tkinter.filedialog.askopenfilename()  #图片目录   注意不要把照片放在中文路径下
    v.set(ts)
    hua(ts)
an=tk.Button(text="选择",command=tu,bg='skyblue').place(x=130,y=35)
test=tk.Label(text="turtle图片",font=("宋体")).place(x=8,y=10)
v = tk.StringVar()
kuang=tk.Entry(width=15,textvariable=v)
kuang.place(x=15,y=40)
gu.mainloop()
