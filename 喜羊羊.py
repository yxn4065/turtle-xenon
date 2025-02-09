
# coding=gbk

import turtle

def plotLine(points, pencolor=None, width=None, speed=None):
    '''
    功能：画折线
    参数：
    - points : 一系列点，用列表或元组表示
    - pencolor : 画笔颜色，默认不变
    - width : 画笔宽度，默认不变
    - speed : 绘制速度，默认不变
    '''
    # 记录旧参数
    oldpencolor = turtle.pencolor()
    oldwidth = turtle.width()
    oldspeed = turtle.speed()

    # 修改新参数
    if pencolor is not None:
        turtle.pencolor(pencolor)
    if width is not None:
        turtle.width(width)
    if speed is not None:
        turtle.speed(speed)

    # 绘制折线
    turtle.up()
    turtle.goto(points[0])
    turtle.down()
    for point in points[1:]:
        turtle.goto(point)

    # 恢复旧参数
    turtle.pencolor(oldpencolor)
    turtle.width(oldwidth)
    turtle.speed(oldspeed)


def plotPoly(points, fill=False, pencolor=None, fillcolor=None,
             width=None, speed=None):
    '''
    功能：绘制封闭多边形
    '''
    # 保存旧参数
    oldfillcolor = turtle.fillcolor()

    # 更新新参数
    if fillcolor is not None:
        turtle.fillcolor(fillcolor)

    # 绘制封闭多边形
    points_plotline = list(points) + [points[0]]
    if fill:
        turtle.begin_fill()
        plotLine(points_plotline, pencolor, width, speed)
        turtle.end_fill()
    else:
        plotLine(points_plotline, pencolor, width, speed)

    turtle.fillcolor(oldfillcolor)

# 设置一些参数
turtle.setup(680, 680)

# 绘画

# 脸部轮廓
points = [
    (-146, 130), (-140, 135), (-137, 138), (-135, 142), (-131, 147), 
(-127, 152), (-126, 156), (-124, 163), (-131, 161), (-124, 162), 
(-119, 164), (-113, 166), (-106, 171), (-102, 175), (-96, 179), 
(-100, 189), (-101, 200), (-99, 206), (-96, 215), (-90, 225), 
(-96, 215), (-98, 208), (-100, 201), (-100, 191), (-97, 180), 
(-92, 172), (-89, 166), (-83, 160), (-76, 156), (-71, 153), 
(-63, 151), (-54, 148), (-47, 148), (-39, 148), (-32, 149), 
(-26, 152), (-16, 154), (-7, 159), (0, 168), (4, 171), 
(8, 181), (11, 188), (13, 194), (11, 202), (8, 210), 
(5, 214), (-1, 217), (0, 211), (2, 205), (0, 204), 
(-3, 201), (-10, 202), (-16, 205), (-19, 211), (-22, 219), 
(-25, 227), (-21, 219), (-20, 213), (-16, 205), (-14, 203), 
(-6, 202), (0, 202), (2, 208), (-3, 215), (5, 214), 
(9, 208), (10, 202), (13, 196), (12, 194), (20, 191), 
(26, 191), (33, 188), (38, 190), (44, 191), (50, 194), 
(55, 187), (58, 184), (62, 180), (68, 174), (77, 170), 
(87, 168), (94, 169), (94, 161), (94, 153), (95, 148), 
(98, 140), (102, 133), (108, 126), (115, 119), (123, 112), 
(118, 106), (114, 97), (112, 88), (112, 80), (113, 71), 
(115, 64), (120, 57), (112, 52), (106, 46), (102, 38), 
(99, 33), (96, 26), (95, 18), (95, 12), (92, 5), 
(86, 2), (85, -5), (85, -13), (87, -20), (90, -28), 
(96, -35), (99, -36), (93, -38), (84, -42), (75, -46), 
(65, -49), (50, -54), (42, -56), (37, -56), (24, -59), 
(11, -59), (-1, -60), (-15, -59), (-27, -60), (-39, -59), 
(-52, -56), (-64, -54), (-77, -49), (-89, -45), (-103, -37), 
(-118, -26), (-123, -19), (-130, -12), (-136, -3), (-139, 6), 
(-141, 15), (-141, 23), (-141, 36), (-139, 50), (-139, 60), 
(-140, 68), (-140, 74), (-141, 81), (-141, 92), (-142, 100), 
(-141, 112), (-140, 123), (-138, 134)
    ]
plotPoly(points, True, pencolor=(0.67, 0.5, 0.22),
         width=2, fillcolor=(1, 0.82, 0.71))

# 围巾和铃铛
points = [
    (-65, -54), (-58, -63), (-54, -65), (-46, -71), (10, -78), 
(20, -76), (29, -76), (41, -72), (52, -68), (63, -61), 
(74, -54), (80, -48), (84, -40), (78, -43), (70, -46), 
(64, -49), (56, -52), (43, -54), (33, -57), (19, -58), 
(8, -59), (-6, -59), (-17, -59), (-31, -59), (-41, -59), 
(-48, -57), (-57, -55)
    ]
plotPoly(points, True, pencolor=(0.67, 0.5, 0.22),
         width=2, fillcolor=(0.13, 0.45, 0.68))
turtle.up()
turtle.goto(-24, -125)
turtle.down()
turtle.color((0.67, 0.5, 0.22), (0.96, 0.73, 0.38))
turtle.width(2)
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.up()
turtle.goto(-33, -94)
turtle.down()
turtle.pencolor((0.36, 0.26, 0.18))
turtle.dot(20)

# 头轮廓
points = [
    (-123, -25), (-129, -23), (-134, -21), (-142, -19), (-145, -15), 
(-150, -10), (-155, 0), (-157, 7), (-158, 15), (-163, 17), 
(-168, 23), (-171, 28), (-175, 37), (-177, 45), (-178, 50), 
(-178, 57), (-179, 66), (-178, 72), (-180, 77), (-183, 81), 
(-186, 86), (-190, 94), (-190, 102), (-189, 109), (-189, 115), 
(-189, 123), (-186, 129), (-188, 138), (-191, 146), (-192, 154), 
(-192, 160), (-192, 167), (-187, 176), (-185, 183), (-180, 194), 
(-174, 200), (-167, 204), (-160, 212), (-160, 221), (-157, 232), 
(-155, 239), (-150, 243), (-144, 251), (-139, 256), (-133, 259), 
(-126, 261), (-120, 271), (-117, 278), (-114, 282), (-106, 291), 
(-101, 296), (-93, 301), (-85, 304), (-77, 305), (-70, 307), 
(-62, 308), (-57, 308), (-53, 307), (-44, 305), (-40, 305), 
(-35, 309), (-29, 313), (-22, 317), (-13, 320), (-8, 323), 
(-2, 323), (7, 324), (17, 323), (26, 319), (30, 319), 
(34, 318), (40, 316), (46, 314), (52, 312), (58, 313), 
(69, 315), (75, 315), (81, 315), (93, 313), (103, 313), 
(111, 310), (118, 305), (127, 296), (133, 285), (144, 283), 
(153, 281), (198, 239), (206, 232), (211, 227), (216, 221), 
(220, 217), (224, 210), (227, 202), (229, 191), (229, 186), 
(231, 178), (232, 167), (235, 162), (241, 152), (245, 140), 
(247, 134), (248, 125), (246, 119), (244, 113), (243, 108), 
(238, 101), (237, 96), (237, 89), (241, 84), (240, 78), 
(240, 73), (238, 63), (237, 57), (234, 47), (228, 41), 
(223, 30), (220, 27), (212, 25), (204, 19), (204, 11), 
(201, 6), (199, -5), (190, -13), (185, -17), (181, -20), 
(175, -24), (161, -27), (154, -27), (147, -30), (142, -32), 
(134, -34), (124, -37), (116, -38)
    ]
plotLine(points, pencolor=(0.67, 0.5, 0.22), width=2)

# 左耳朵
points = [
    (173, 192), (179, 195), (184, 196), (190, 195), (197, 195), 
(200, 193), (206, 190), (214, 183), (217, 179), (222, 173), 
(224, 169), (226, 164), (231, 160), (235, 155), (241, 152), 
(239, 148), (235, 148), (234, 146), (230, 142), (225, 142), 
(221, 140), (211, 139), (206, 140), (200, 141), (193, 143), 
(187, 142), (182, 146), (176, 152), (169, 157), (169, 163), 
(167, 168), (167, 174), (167, 182), (172, 187)
    ]
plotPoly(points, True, pencolor=(0.67, 0.5, 0.22),
         width=2, fillcolor=(1, 0.82, 0.71))

# 右耳朵
points = [
    (-195, 159), (-197, 156), (-200, 153), (-204, 151), (-206, 149), 
(-208, 146), (-205, 143), (-201, 139), (-193, 135), (-189, 135), 
(-192, 143), (-192, 148), (-192, 155)
    ]
plotPoly(points, True, pencolor=(0.67, 0.5, 0.22),
         width=2, fillcolor=(1, 0.82, 0.71))

# 左角
points = [
    (130, 269), (139, 268), (142, 273), (144, 277), (151, 281), 
(155, 286), (161, 289), (171, 294), (175, 296), (184, 300), 
(194, 302), (200, 303), (212, 303), (219, 303), (227, 301), 
(234, 297), (239, 291), (239, 283), (235, 279), (231, 273), 
(227, 267), (221, 264), (216, 261), (213, 257), (210, 255), 
(206, 251), (203, 245), (196, 238), (192, 233), (188, 228), 
(186, 227), (191, 220), (186, 224), (182, 223), (177, 223), 
(175, 227), (175, 230), (173, 235), (170, 240), (164, 243), 
(158, 242), (154, 243), (152, 249), (152, 254), (148, 260), 
(142, 265), (139, 270)
    ]
plotPoly(points, True, pencolor=(0.67, 0.5, 0.22),
         width=2, fillcolor=(0.52, 0.38, 0.29))

# 右角
points = [
    (-118, 276), (-127, 280), (-133, 282), (-142, 285), (-150, 288), 
(-156, 288), (-164, 289), (-167, 289), (-174, 289), (-178, 288), 
(-184, 284), (-186, 278), (-186, 271), (-183, 266), (-178, 259), 
(-172, 253), (-168, 249), (-162, 243), (-158, 237), (-158, 233), 
(-154, 237), (-149, 244), (-143, 249), (-137, 254), (-133, 257), 
(-126, 260), (-126, 263), (-124, 268), (-121, 271)
    ]
plotPoly(points, True, pencolor=(0.67, 0.5, 0.22),
         width=2, fillcolor=(0.52, 0.38, 0.29))

# 左眼睛
turtle.color((0.67, 0.5, 0.22), (1, 1, 1))
turtle.width(2)
turtle.up()
turtle.goto(-94, 40)
turtle.down()
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.pencolor((0.1, 0.1, 0.1))
turtle.up()
turtle.goto(-93, 78)
turtle.down()
turtle.dot(50)

turtle.pencolor((1, 1, 1))
turtle.up()
turtle.goto((-100, 86))
turtle.down()
turtle.dot(20)

# 右眼睛
turtle.color((0.67, 0.5, 0.22), (1, 1, 1))
turtle.width(2)
turtle.up()
turtle.goto(30, 44)
turtle.down()
turtle.begin_fill()
turtle.circle(40)
turtle.end_fill()

turtle.pencolor((0.1, 0.1, 0.1))
turtle.up()
turtle.goto(32, 81)
turtle.down()
turtle.dot(50)

turtle.pencolor((1, 1, 1))
turtle.up()
turtle.goto((23, 93))
turtle.down()
turtle.dot(19)

# 右眉毛
points = [
    (-122, 145), (-120, 148), (-115, 151), (-111, 152), (-104, 154), 
(-99, 155), (-90, 154), (-83, 152), (-79, 148), (-75, 144), 
(-78, 146), (-84, 146), (-90, 147), (-97, 148), (-103, 148), 
(-108, 147), (-113, 145), (-117, 144)
    ]
plotPoly(points, True, pencolor=(0.35, 0.11, 0.21),
         width=2, fillcolor=(0.35, 0.11, 0.21))

# 左眉毛
points = [
    (-2, 154), (4, 158), (10, 160), (17, 161), (20, 162), 
(27, 163), (32, 163), (39, 160), (47, 160), (53, 157), 
(60, 153), (53, 153), (44, 154), (35, 154), (27, 154), 
(22, 155), (16, 154), (9, 155)
    ]
plotPoly(points, True, pencolor=(0.35, 0.11, 0.21),
         width=2, fillcolor=(0.35, 0.11, 0.21))

# 鼻子
points = [
    (-56, 44), (-50, 44), (-42, 44), (-35, 40), (-28, 35), 
(-25, 30), (-26, 23), (-31, 19), (-38, 16), (-45, 14), 
(-50, 13), (-60, 14), (-68, 16), (-73, 22), (-74, 28), 
(-72, 32), (-68, 37), (-61, 42)
    ]
plotPoly(points, True, pencolor=(0.2, 0.14, 0.11),
         fillcolor=(0.2, 0.14, 0.11), width=2)
turtle.pencolor((1, 1, 1))
turtle.up()
turtle.goto((-64, 32))
turtle.down()
turtle.dot(15)

# 嘴巴
points = [
    (-49, -20), (-45, -23), (-41, -25), (-34, -27), (-29, -28), 
(-23, -29), (-15, -28), (-7, -25), (-4, -22), (2, -17), 
(7, -11)
    ]
plotLine(points, pencolor=(0.2, 0.14, 0.11), width=2)

# 隐藏海龟
turtle.hideturtle()
turtle.done()
