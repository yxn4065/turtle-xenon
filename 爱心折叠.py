import turtle  
  
# 初始化  
turtle.speed(1)  
turtle.bgcolor("black")  
turtle.pensize(2)  
  
# 设置颜色循环  
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]  
  
# 画心形  
def draw_heart(x, y, size, color):  
    turtle.penup()  
    turtle.goto(x, y)  
    turtle.pendown()  
    turtle.begin_fill()  
    turtle.fillcolor(color)  
    turtle.left(45)  
    turtle.forward(size)  
    turtle.circle(size / 2, 180)  
    turtle.right(90)  
    turtle.circle(size / 2, 180)  
    turtle.forward(size)  
    turtle.end_fill()  
  
# 主程序  
turtle.penup()  
turtle.goto(0, -200)  
turtle.pendown()  
turtle.color("white")  
  
for i in range(36):  
    draw_heart(0, 0, 100, colors[i % len(colors)])  
    turtle.right(10)  
    turtle.forward(20)  
  
turtle.done()
