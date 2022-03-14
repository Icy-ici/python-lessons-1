
## Draw a hexagon with the Turtle ##

import turtle

wn = turtle.Screen()
wn.setup(500, 500)

myTtl = turtle.Turtle()

## Write your code below this line ##

for i in range(6):
    myTtl.left(60)
    myTtl.forward(50)
