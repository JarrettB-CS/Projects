#Exercise 19 rock paper scissors

import random

def rps():

options = ("rock", "paper", "scissor")
computer = random.choice(options)
user = None

while user not in options:
    user = input("Please enter a valid choice - rock, paper, scissor: ")
    print()

print("CPU chose:", computer)
print("YOU chose:", user)


if user == computer:
    print("It's a tie.")
elif user == "rock" and computer == "scissor":
    print("You WIN!")
elif user == "paper" and computer == "rock":
    print("You WIN!")
elif user == "scissor" and computer == "paper":
    print("You WIN!")
else:
    print("You LOSE!")

print("Do you want to play again ")

return()




#Add replay ability

#1.1.0