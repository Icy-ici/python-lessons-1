
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

#################################################
## Draw a circle (hint - you only need 3 lines ##
#################################################

for i in range(360):
    myTtl.left(1)
    myTtl.forward(1)