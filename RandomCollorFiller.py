import turtle
from random import randint

height = 500
width = 500
frame = turtle.Screen()
frame.setup(width,height,None,None)
frame.title("Random Filler")

pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.setposition(0,0)
pen.setheading(90)
pen.hideturtle()

def penLeft(num):
    x = pen.xcor()
    y = pen.ycor()
    pen.rt(90)
    pen.color(flipColor(num))
    pen.dot(5)
    pen.fd(5)
def penRight(num):
    x = pen.xcor()
    y = pen.ycor()
    pen.lt(90)
    pen.color(flipColor(num))
    pen.dot(5)
    pen.fd(5)
def flipColor(num):
    switcher = {
        0: "white",
        1: "black",
        2: "green",
        3: "blue",
        4: "yellow",
        5: "red",
        6: "orange",
        7: "purple",
        8: "pink",
        9: "grey",
        }
    return switcher.get(num, "green")

while True:
    if randint(0,1) == 0:
        penRight(randint(0,9))
    else:
        penLeft(randint(0,9))




##while True:
    ##pass

