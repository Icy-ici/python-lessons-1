# Alfred's security guard program

friends = "Bruce"

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Alfred  ##
## or a friend of Alfred.                          ##
## Everyone else is told, politely, to go away     ##
#####################################################

name = input("What is your name? ")

if name == "Alfred" or name == friends:
    print("Welcome!")
else:
    print("You are not Alfred or a friend of Alfred, please leave.")