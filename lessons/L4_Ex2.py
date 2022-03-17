import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

############################################
## Use you knowledge of Python and Turtle ##
## to draw a car. Use functions to ensure ##
## that you Donot Repeat Yourself.        ##
############################################

def circle(lineColor, color, size):
    my_ttl.color(lineColor, color)
    my_ttl.begin_fill()
    my_ttl.circle(size)
    my_ttl.end_fill()

def move(x, y):
    my_ttl.penup()
    my_ttl.goto(x,y)
    my_ttl.pendown()

def rec(width, height):
    for i in range(2):
        my_ttl.forward(width)
        my_ttl.left(90)
        my_ttl.forward(height)
        my_ttl.left(90)

move(-100, -100)
circle("black", "white", 50)
move(100, -100)
circle("black", "white", 50)
move(-200, -50)
rec(400, 100)
