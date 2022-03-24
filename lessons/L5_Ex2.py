# Alfred's security guard program

friends = "Bruce"

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Alfred  ##
## or a friend of Alfred.                          ##
## Everyone else is told, politely, to go away     ##
#####################################################

name = input("What is your name? ") ## Ask for the name

if name == "Alfred" or name == "Bruce": ## If the name is Alfred or Bruce,
    print("Welcome!") ## Welcome
else: ## If the name is not Alfred or Bruce,
    print("You are not Alfred or Bruce, please leave.") ## Tell them to leave