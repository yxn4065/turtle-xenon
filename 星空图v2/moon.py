# coding: utf-8
import os  # 导入设置路径的库
import sys
import pygame  # 导入可以加载音乐的库
from pygame.locals import *


def bgpic(self, picname=None):
    if picname is None:
        return self._bgpicname
    if picname not in self._bgpics:
        self._bgpics[picname] = self._image(picname)
    self._setbgpic(self._bgpic, self._bgpics[picname])
    self._bgpicname = picname


os.chdir('./')  # 把路径改为数据存放的路径
pygame.init()  # pygame初始化
pygame.mixer.init()  # pygame.mixer初始化

pygame.mixer.music.load("星空.mp3")  # 设置背景音乐
# pygame.mixer.music.set_volume(0.4)	          # 设置音量
pygame.mixer.music.play()  # 播放音乐

bg_size = width, height = 300, 200  # 设置界面窗口
bg_rgb = (255, 255, 255)
screen1 = pygame.display.set_mode(bg_size)
pygame.display.set_caption("星空音乐")
clock = pygame.time.Clock()  # 创建设置帧率对象

play_image = pygame.image.load("开始.png").convert_alpha()  # 创建播放图片surface对象
pause_image = pygame.image.load("开始.png").convert_alpha()  # 创建暂停图片surface对象

pause_rect = pause_image.get_rect()  # 获取播放矩形框
print(pause_rect.width, pause_rect.height)  # 获取暂停矩形框
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2

from turtle import *
from random import random, randint

os.chdir('./')  # 把路径改为数据存放的路径
screen = Screen()
width, height = 900, 700
screen.setup(width, height)
screen.title("模拟3D星空")
screen.bgcolor("black")
screen.bgpic(r'./两个背影.gif')
screen.mode("logo")  # 设置乌龟模式（“standard”，“logo”或“world”）并执行重置，logo表示向上
screen.delay(0)  # 设置或返回以毫秒为单位的绘图延迟，这里要设为0，否则很卡

printer = Turtle()
printer.hideturtle()
printer.penup()
printer.color('white')
printer.goto(-100, -350)
printer.write("In the whole universe\n\n", move=True, align="left", font=("Italic", 30, "bold"))
printer.goto(-300, -400)
printer.write("you're the only star belongs me!\n\n", move=True, align="left", font=("Italic", 30, "bold"))

t = Turtle(visible=False, shape='circle')
t.pencolor("white")  # 设置画笔的颜色
t.fillcolor("white")  # 设置图形填充颜色
t.penup()  # 抬起画笔
t.setheading(-90)  # 设置当前朝向角度
t.goto(width / 2, randint(-height / 2, height / 2))  # 把画笔移动到定点

stars = []
for i in range(300):
    star = t.clone()  # 当前海龟的位置处克隆出另一只位置方向等属性相同的海龟，并且取名叫star
    s = random() / 3
    if 0.01 < s < 0.03:
        star.pencolor("black")
        star.fillcolor("black")
    elif 0.03 < s < 0.04:
        star.pencolor("lightcoral")
        star.fillcolor("lightcoral")
    elif 0.05 < s < 0.1:
        star.pencolor("green")
        star.fillcolor("green")
    elif 0.15 < s < 0.16:
        star.pencolor("yellow")
        star.fillcolor("yellow")
    elif 0.19 < s < 0.2:
        star.pencolor("red")
        star.fillcolor("red")
    elif 0.21 < s < 0.22:
        star.pencolor("purple")
        star.fillcolor("purple")
    elif 0.29 < s < 0.3:
        star.pencolor("darkorange")
        star.fillcolor("darkorange")
    elif 0.31 < s < 0.32:
        star.pencolor("red")
        star.fillcolor("yellow")
    elif 0.32 < s < 0.33:
        star.pencolor("yellow")
        star.fillcolor("white")
    star.shapesize(s, s)
    star.speed(int(s * 30))  # 设置画笔移动速度，数字越大越快
    star.setx(width / 2 + randint(1, width))  # 将当前x轴移动到指定位置
    star.sety(randint(-height / 2, height / 2))  # 将当前y轴移动到指定位置
    # star.showturtle()
    stars.append(star)

i = 0
pause = False  # 是否暂停
while True:
    i += 0
    for star in stars:

        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor() < -width / 2:
            star.hideturtle()
            star.setx(width / 2 + randint(1, width))
            star.sety(randint(-height / 2, height / 2))
            star.showturtle()
    if i >= 100:
        break

    # 查找队列事件
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # 检测鼠标左击是否按下
                pause = not pause
            if event.button == 3:  # 检测鼠标右击是否按下
                pause = not pause

        if event.type == KEYDOWN:
            if event.key == K_SPACE:  # 检测是否为空格键按下
                pause = not pause

    screen1.fill(bg_rgb)

    if pause:
        pygame.mixer.music.pause()
        screen1.blit(pause_image, pause_rect)
    else:
        pygame.mixer.music.unpause()
        screen1.blit(play_image, pause_rect)

    pygame.display.flip()
    clock.tick(30)
