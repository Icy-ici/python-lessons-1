import turtle

# set up screen
screen = 500
window = turtle.Screen()
window.setup(screen, screen)

# create turtle instance
my_ttl = turtle.Turtle()
my_ttl.shape("circle")

##################################
## Using the tutrle command you ##
## have learnt, draw a house.   ##
##################################

for i in range(4):
    my_ttl.forward(100)
    my_ttl.left(90)

my_ttl.left(90)
my_ttl.forward(100)
my_ttl.left(90)
my_ttl.forward(50)
my_ttl.right(140)
my_ttl.forward(120)
my_ttl.right(90)
my_ttl.forward(120)
my_ttl.right(140)
my_ttl.forward(50)