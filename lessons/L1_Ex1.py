
## Draw a square with the Turtle ##

import turtle

wn = turtle.Screen()
wn.setup(500, 500)

myTtl = turtle.Turtle()

## Write your code below this line ##

for i in range(4):
    myTtl.forward(100)
    myTtl.left(90)