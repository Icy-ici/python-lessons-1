
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

###############################
## Draw a Hexagon in 3 lines ##
###############################

for i in range(6):
    myTtl.left(60)
    myTtl.forward(50)