import turtle

#####################################################
## Adjust the code below to allow the user to      ##
## choose the coordinates where the shape is drawn ##
#####################################################

def draw_poly(length, sides, color):
    fred.color("black",color)
    fred.begin_fill()
    for i in range(sides):
        fred.forward(length)
        fred.right(360/sides)
    fred.end_fill()
        
def get_number(prompt):
    num = input(prompt)
    if num.lstrip("-").isdigit():
        return int(num)
    else:
        print("Invalid input")
        quit()
        
def get_color():
    color = input("Fill colour (red, blue, green)?> ").lower()
    if color == "red":
        return color
    elif color == "blue":
        return color
    elif color == "green":
        return color
    else:
        print("Invalid input")
        quit()

def move_pen():
    # write your code here to get coordinates from user #
    x = get_number("X coordinate?> ")
    y = get_number("Y coordinate?> ")
    fred.penup()
    fred.goto(x,y)
    fred.pendown()

# setup window
screen = 500
window = turtle.Screen()
window.screensize(screen, screen)

# create instance of turtle
fred = turtle.Turtle()
fred.shape("turtle")

# get user input
num_sides = get_number("How many sides?> ")
size = get_number("How long are the sides?> ")
fill = get_color()

move_pen()
draw_poly(size, num_sides, fill)