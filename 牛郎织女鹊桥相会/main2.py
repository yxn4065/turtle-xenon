import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()
t2.up()
t2.pensize(0)
t2.goto(500,-50)

t3 = turtle.Turtle()
t3.up()
t3.pensize(0)
t3.goto(0,500)

# 开始画图
#################桥上-前
#抬起笔
t.up()
t.goto(-330,-100)
#画笔落下
t.down()
t.pencolor("pink")
# 画笔粗细
t.pensize(3)
#前130
t.fd(90)
t.left(70)
t.circle(-250,60)
t.right(10)
t.fd(90)
t.right(10)
t.circle(-250,60)
t.left(70)
t.fd(90)

#############桥下
#抬起笔
t.up()
t.goto(-330,-180)
#画笔落下
t.down()
t.pencolor("black")
# 画笔粗细
t.pensize(3)
#前130
t.fd(130)
t.left(90)
t.circle(-200,180)
t.left(90)
t.fd(130)


###################桥上-后
#抬起笔
t.up()
t.goto(-330,-50)
#画笔落下
t.down()
t.pencolor("pink")
# 画笔粗细
t.pensize(3)
#前130
t.fd(90)
t.left(70)
t.circle(-250,60)
t.right(10)
t.fd(90)
t.right(10)
t.circle(-250,60)
t.left(70)
t.fd(90)

#阶梯
def row(x,y,left,right,length):
    #抬起画笔
    t.up()
    t.goto(x,y)
    t.pencolor("gray")
    #画笔落下
    t.down()
    t.left(left)
    t.right(right)
    t.fd(length)

#从左到中
row(-330,-50,0,90,130)
row(-240,-50,0,0,50)
row(-210,5,30,0,30)
row(-160,60,5,0,42)
row(-110,90,0,5,47)
row(-45,110,1,30,50)
#从中到右
row(38,110,0,0,50)
row(103,90,0,30,47)
row(153,60,0,5,42)
row(203,5,5,0,30)
row(233,-50,30,0,50)
row(323,-50,0,0,130)

# 移动牛郎织女
def move_b_g(b1,g1,h):
    ########移动牛郎
    t.up()
    t.goto(b1,h)
    #画笔落下
    t.down()
    image = "boy1.gif"
    #screen = turtle.Screen()
    screen = t.getscreen()
    screen.addshape(image)
    t.shape(image)
    ########移动织女
    t2.up()
    t2.goto(g1,h)
    #画笔落下
    t2.down()
    image = "girl1.gif"
    #screen = turtle.Screen()
    screen = t2.getscreen()
    screen.addshape(image)
    t2.shape(image)

move_b_g(-285,278,-50)
move_b_g(-225,218,-22)
move_b_g(-185,178,32)
move_b_g(-135,128,75)
move_b_g(-77,70,100)
move_b_g(-25,18,110)







####写字
t3.up()
t3.goto(-80,-80)
t3.down()
t3.pencolor("#ffa0a0")
t3.write('七夕今宵看碧霄',font=("Arial",'22'))

t3.up()
t3.goto(-80,-130)
t3.down()
t3.pencolor("#ffa0a0")
t3.write('牵牛织女渡河桥',font=("Arial",'22'))
#
# ##########月亮落下来
t3.up()
t3.goto(0,250)
#画笔落下
t3.down()
image = "yue1.gif"
#screen = turtle.Screen()
screen = t3.getscreen()
screen.addshape(image)
t3.shape(image)

turtle.done() # `turtle`, not `t`

