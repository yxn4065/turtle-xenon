import turtle


# 初始化画布和画笔
def setup_canvas_and_turtle():
    turtle.pensize(2)  # 画笔宽度
    turtle.bgcolor("black")  # 背景颜色
    turtle.speed(0)  # 设置画笔速度为最快
    turtle.tracer(False)  # 关闭绘图更新，提高性能


# 绘制分形图形
def draw_fractal(iterations, colors):
    for x in range(iterations):
        # 根据迭代次数计算移动距离
        distance = x  # 或使用其他函数，如 distance = 2 * x
        # 选择当前颜色
        turtle.color(colors[x % len(colors)])
        # 移动画笔绘制线段
        turtle.forward(distance)
        # 旋转画笔到下一个方向
        turtle.left(59)  # 可以调整这个角度来改变图形


# 添加附加信息
def add_additional_info():
    turtle.penup()
    turtle.goto(0, -200)  # 调整位置以适应画布
    turtle.color("white")
    turtle.write("数学之美：分形艺术", align="center", font=("Arial", 16, "normal"))
    turtle.goto(0, -230)  # 调整位置以适应画布
    turtle.write("Python原创图形设计", align="center", font=("Arial", 16, "normal"))


# 主函数
def main():
    # 初始化
    setup_canvas_and_turtle()
    # 定义颜色列表
    colors = ["red", "yellow", 'purple', 'blue', 'green', 'orange']
    # 绘制分形图形
    draw_fractal(400, colors)
    # 添加附加信息
    add_additional_info()
    # 更新画布以显示图形
    turtle.tracer(True)
    turtle.update()
    # 隐藏画笔
    turtle.hideturtle()
    # 保持窗口打开，直到用户关闭它
    turtle.done()


# 运行主函数
if __name__ == "__main__":
    main()
