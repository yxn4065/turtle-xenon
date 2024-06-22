# coding=utf-8
# @Author : Xenon
# @File : 樱花树.py
# @Date : 2024/5/13 13:52 
# @IDE : PyCharm(2023.3) Python3.9.13

import turtle as t
import time, random


# 画樱花的躯干
# 画樱花的躯干
def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                # 白色
                t.color('snow')
            else:
                # 淡珊瑚色
                t.color('lightcoral')
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 2)
        else:
            # 赭色
            t.color('sienna')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


# 掉落的花瓣
def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


# 改变颜色
def changeColor():
    t.up()
    t.color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
    t.goto(-330, -60)  # 设置文字位置
    t.write('云南大学', font=("Arial", 18, "normal"))
    t.goto(-300, -90)
    t.write('艺术类专业', font=("Arial", 18, "normal"))
    t.goto(-280, -120)
    t.write('Python原创图形设计', font=("Arial", 18, "normal"))


# 绘图区域

# 隐藏画笔
t.hideturtle()
t.getscreen().tracer(5, 0)
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# 画樱花的躯干

t.hideturtle()  # 影藏最终箭头


# 画星星
def pentagram(size, x, y, seth=0):
    t.goto(x, y)
    t.setheading(seth)
    t.backward(size * 1.1756 / 2)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()
    t.penup()


def drawflag():
    t.penup()
    t.goto(360, -10)
    t.pendown()
    color = 'red'
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(100)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill()
    t.penup()
    t.pencolor('yellow')
    t.fillcolor('yellow')
    pentagram(51, 390, 50)
    pentagram(20, 440, 80, 30)
    pentagram(20, 460, 60, -30)
    pentagram(20, 460, 30)
    pentagram(20, 450, 10, 30)
    t.pendown()


# 添加飘带绘制函数
def draw_ribbon(t, length, width, color):
    t.color(color)
    t.pensize(width)
    for _ in range(2):
        t.forward(length)
        t.right(180)
        t.circle(width * 2, 180)
        t.hideturtle()

    # 添加星星闪烁函数


def twinkle_stars(num_stars, max_size, min_size):
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(100, 400)
        size = random.randint(min_size, max_size)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.color(random.uniform(0.5, 1), random.uniform(0.5, 1), 1)
        for _ in range(5):
            t.forward(size)
            t.right(144)
        t.end_fill()


# 主程序部分
t.speed(0)  # 设置绘制速度为最快
t.hideturtle()
# t.getscreen().tracer(0, 0)  # 关闭屏幕更新，提高绘图效率

# 绘制樱花树和花瓣
Tree(60, t)
Petal(200, t)

# 绘制彩带
t.penup()
t.goto(-200, -100)
draw_ribbon(t, 300, 10, 'pink')

t.penup()
t.goto(200, -100)
draw_ribbon(t, 300, 10, 'lightblue')

# 绘制星星背景
twinkle_stars(50, 10, 5)

# 绘制旗帜（可选）
# drawflag()

start_time = time.time()  # 记录开始时间
duration = 10  # 设置持续时间，例如10秒

# 持续改变颜色（可选，如果希望有这个效果可以取消注释）
while True:
    elapsed_time = time.time() - start_time  # 计算已经过去的时间
    if elapsed_time > duration:
        break  # 如果超过了设定的持续时间，则退出循环
    time.sleep(1)
    changeColor()
    t.getscreen().update()  # 手动更新屏幕

# 更新屏幕并等待用户关闭窗口
t.getscreen().update()
t.done()
