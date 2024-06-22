import turtle as t

t.pen(speed=0)  # 加快绘图速度
t.pencolor("red")
t.pensize(2)
t.penup()
t.goto(-200, -200)  # 以左下角某处为起点
t.pendown()
t.seth(0)
length = 400
while length != 0:  # 利用正方形螺旋线的性质来绘图
    t.fd(length)
    t.left(90)
    length -= 2.5
t.hideturtle()  # 绘图结束后把海龟头(笔触头)隐藏起来
t.done()  # 绘图结束后使窗口停留
