import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("turtle")

############################################
## Convert the code below using functions ##
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

# move pen
move(0, -200)

# draw head
circle("black", "yellow", 200)

# move pen
move(-75, 0)

# draw eye
circle("black", "black", 50)

# move pen
move(75, 0)

# draw eye
circle("black", "black", 50)

# move pen
move(-100, -75)

# draw mouth
my_ttl.color("black","black")
my_ttl.begin_fill()
for i in range(2):
    my_ttl.forward(200)
    my_ttl.right(90)
    my_ttl.forward(25)
    my_ttl.right(90)
my_ttl.end_fill()

my_ttl.hideturtle()