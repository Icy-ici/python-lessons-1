import turtle

## setup screen and turtle ##
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Copilot")

myTtl = turtle.Turtle()
myTtl.color("blue")
myTtl.pensize(3)
myTtl.shape("turtle")
myTtl.speed(1)

## draw a square ##
for i in range(4):
    myTtl.forward(100)
    myTtl.left(90)
