# Alfred's security guard program

#####################################################
## Write a program that asks for a person's name   ##
## and then grants entry of that person is Alfred  ##
## everyone else is told, politely, to go away     ##
#####################################################

name = input("What is your name? ") ## Ask for the name

if name == "Alfred": ## If the name is Alfred,
    print("Welcome!") ## Welcome
else: ## If the name is not Alfred,
    print("You are not Alfred, please leave.") ## Tell them to leave
