
import turtle

wn = turtle.Screen()
wn.setup(500, 500)
myTtl = turtle.Turtle()

################################
## Draw a Triangle in 3 lines ##
################################

for i in range(3):
    myTtl.right(120)
    myTtl.forward(100) 