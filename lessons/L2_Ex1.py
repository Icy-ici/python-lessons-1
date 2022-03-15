
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

##############################
## Draw a square in 3 lines ##
##############################

for i in range(4):
    myTtl.forward(100)
    myTtl.left(90)

