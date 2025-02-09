import time
import turtle as t
from turtle import *
t.setup(1280,720)
t.speed(0)
t.pensize(1)
length = 6
path = 'F'
angle = 27

expalnation = {
    'F': '画线',
    'x': '-',
    '+': '逆时针旋转',
    '-': '顺时针旋转',
    '[': '记录当前位置',
    ']': '恢复上一个位置',
    'a': '上色',
    'b': '上色',
    'c': '上色'
}
rules = {
    'F': 'aFF[b-F++F][c+F--F]c++F--F',
    'X': 'aFF+[b+F]+[c-F]'
}


def draw_path(path, expalnation):
    posList, angleList = [], []
    t.up()
    t.goto(600, -350)
    t.down()
    t.lt(90)
    for symbol in path:
        if symbol == 'F':
            t.forward(length)
        elif symbol == '+':
            t.left(angle)
        elif symbol == '-':
            t.rt(angle)
        elif symbol == '[':
            posList.append(t.pos())
            angleList.append(t.heading())
        elif symbol == 'a':
            t.pensize(3)
            t.color("#8c503c")
        elif symbol == 'b':
            t.pensize(2)
            t.color("#4ab441")
        elif symbol == 'c':
            t.pensize(2)
            t.color("#18b418")
        elif symbol == ']':
            t.up()
            t.home()
            t.goto(posList.pop())
            t.left(angleList.pop())
            t.down()


def apply_rules(path, rules):
    L = [_ for _ in path]
    for i in range(len(L)):
        symbol = L[i]
        if symbol == 'F':
            L[i] = rules[symbol]
        if symbol == 'X':
            L[i] = rules[symbol]
    path = ''.join(L)
    return path


for _ in range(4):
    path = apply_rules(path, rules)
draw_path(path, expalnation)