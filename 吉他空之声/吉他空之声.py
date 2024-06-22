import turtle as q
import time  # 导入time模块，使用time.sleep(1)指令使得每画完一个结构后都停顿1秒
import random  # 导入随机模块

q.bgpic(r"C:\Users\yxn\Downloads\渐变色背景.png")  # 设置背景图片
q.pensize(3)
q.speed(0)
q.delay(0)  # 将绘图延迟时间设置为0，绘图速度会更快

# 绘制背景上散落的圆点
for i in range(100):
    x = random.randint(-400, 400)
    y = random.randint(-300, 300)
    q.penup()
    q.goto(x, y)
    q.pendown()
    q.speed(900)
    q.color("#d2a4b4")
    a = random.randint(2, 7)
    q.dot(a)
q.penup()
q.home()  # 让海龟回到初始位置，即原点(0,0),并且朝右
q.pendown()

q.delay(1)  # 将绘图延迟时间设置为1，相当于关闭delay(0)的加速效果
# ① 绘制吉他面板
q.pencolor('black')
q.fillcolor("#E6AE00")
q.begin_fill()
q.left(90)
q.penup()
q.forward(50)
q.pendown()
q.right(90)
q.circle(-40, 120)
q.left(20)
q.circle(70, 10)
q.left(60)
q.circle(-50, 140)
q.right(10)
q.forward(35)
q.right(10)
q.circle(-50, 140)
q.left(60)
q.circle(70, 10)
q.left(20)
q.circle(-40, 120)
q.goto(0, 50)
q.penup()
q.end_fill()

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ② 绘制音孔
q.goto(0, -20)
q.pencolor('darkgreen')
q.dot(50)
q.pencolor('red')
q.dot(45)
q.pencolor('black')
q.dot(35)

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ③ 绘制琴头和弦钮
q.pensize(1)
q.left(90)
q.goto(0, 0)
q.forward(120)
q.pendown()
q.right(90)
q.begin_fill()
for j in range(2):
    if j == 0:
        q.forward(10)
        q.left(90)
    for i in range(3):
        q.forward(5)
        q.right(90)
        q.forward(3)
        q.right(90)
        q.forward(3)
        q.left(90)
        q.forward(3)
        q.left(90)
        q.forward(9)
        q.left(90)
        q.forward(3)
        q.left(90)
        q.forward(6)
        q.forward(-3)
        q.right(90)
        q.forward(3)
        q.right(90)
        q.forward(-3)
        q.forward(8)
    if j == 0:
        q.left(30)
        q.forward(20)
        q.left(120)
        q.forward(20)
        q.left(30)
    else:
        q.left(90)
        q.forward(10)
q.end_fill()

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ④ 绘制两组白色弦柱
q.fillcolor('white')
q.penup()
q.forward(2)
q.left(90)
q.forward(4)
q.pendown()
q.begin_fill()
for i in range(2):
    q.forward(30)
    q.right(90)
    q.forward(4)
    q.right(90)
q.end_fill()

q.penup()
q.left(90)
q.forward(8)
q.right(90)
q.pendown()
q.begin_fill()
for i in range(2):
    q.forward(30)
    q.right(90)
    q.forward(4)
    q.right(90)
q.end_fill()

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ⑤ 绘制吉他的指板
q.fillcolor('black')
q.pensize(0)
q.begin_fill()
q.penup()
q.forward(-4)
q.pendown()
q.forward(-126)
q.circle(-6, 180)
q.forward(-126)
q.end_fill()

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ⑥ 绘制6根弦
c = 'yellow'
co = 'darkyellow'
colors = [c, c, c, co, co, co]
q.pensize(0.5)
for i in range(6):
    color = colors[(1 % 8)]
    q.pencolor(color)
    q.penup()
    q.right(90)
    q.forward(1.75)
    q.left(90)
    q.pendown()
    q.forward(190)
    q.forward(-190)

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ⑦ 绘制下弦枕
q.penup()
q.forward(190)
q.left(90)
q.forward(-20)
q.pencolor('black')
q.pensize(10)
q.pendown()
q.forward(48)

q.pencolor('white')
q.penup()
q.pensize(1)
q.forward(-12)
q.right(90)
q.forward(5)
q.left(90)
for i in range(3):
    q.pendown()
    q.forward(-24)
    q.forward(24)
    q.penup()
    q.left(90)
    q.forward(5)
    q.right(90)

time.sleep(1)  # 停顿1秒后再执行（此代码可直接删除）
# ⑧ 绘制18道品丝
# 吉他品丝就是音品。品丝是指按精准间距嵌在整个指板上的薄金属条。
q.pensize(1)
q.penup()
q.goto(0, 0)
q.forward(-3)
for i in range(18):
    q.pendown()
    q.forward(6)
    q.forward(-6)
    q.penup()
    q.left(90)
    q.forward(7)
    q.right(90)

# ⑨ 写文字
q.pencolor("white")  # 文字是白色
q.goto(0, -200)
q.write("Python原创图形设计：吉他与梦幻天空", align="center", font=("隶书", 18))  # 居中书写文字

q.hideturtle()

q.done()
