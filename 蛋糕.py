# Layer Cake Challenge - www.101computing.net/layer-cake/
from turtle import *
import time, math
import turtle

def draw_circle(turtle, color, x, y, radius):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def draw_rectangle(turtle, color, x, y, width, height):
    turtle.hideturtle()
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)


def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.right(144)
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)


def addIcing(turtle, color, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(-x - 2, y + 10)
    turtle.pendown()
    turtle.begin_fill()

    for z in range(-x - 3, x + 3):
        turtle.goto(z, y - 10 - 10 * math.cos((z / 100) * 2 * math.pi))

    turtle.goto(x + 3, y + 10)
    turtle.goto(-x - 3, y + 10)
    turtle.end_fill()


myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)
myPen.hideturtle()
window = turtle.Screen()
window.bgcolor("#69D9FF")
y = -140

# Inititalise the dictionary
ingredients = {}
# Add items to the dictionary
ingredients["strawberry"] = "pink"
ingredients["milk chocolate"] = "#BF671F"
ingredients["matcha"] = "#93c572"
ingredients["icing sugar"] = "#FFFFFF"

### Now let's preview the layer cake

# let's draw the plate
draw_rectangle(turtle, "white", -150, y - 10, +300, 10)

# Iterate through each layer of the list
draw_rectangle(myPen, ingredients["milk chocolate"], -120, y, 240, 30)
y += 30
draw_rectangle(myPen, ingredients["strawberry"], -120, y, 240, 35)
y += 35
addIcing(myPen, ingredients["icing sugar"], 120, y)
y += 10
draw_rectangle(myPen, ingredients["milk chocolate"], -100, y, 200, 20)
y += 20
draw_rectangle(myPen, ingredients["strawberry"], -100, y, 200, 40)
y += 40
addIcing(myPen, ingredients["icing sugar"], 100, y)
y += 10
draw_rectangle(myPen, ingredients["milk chocolate"], -70, y, 140, 24)
y += 24
draw_rectangle(myPen, ingredients["strawberry"], -70, y, 140, 36)
y += 36
addIcing(myPen, ingredients["icing sugar"], 70, y)
y += 10
draw_rectangle(myPen, ingredients["matcha"], -4, y, 8, 60)
y += 65
draw_star(myPen, "white", 2, y, 10)

time.sleep(30)
