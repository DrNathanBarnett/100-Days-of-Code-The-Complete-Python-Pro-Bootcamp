#Day 4 Project: Rock Paper Scissors
from random import choice
import random
rock = "rock"
scissors = "scissors"
paper = "paper"


print("Welcome to the rock paper scissors game")
print("Please choose either 'rock', 'paper' or 'scissors'")
print("Do this by selecting:\n0 for Rock\n1 for Paper\n2 for Scissor")

choice1 = int(input("What will your choice be? 0, 1 or 2"))
computer_choice1 = random.randint(0,2)

if choice1 == 0:
    print("rock")
    computer_choice1 = random.randint(0,2)
    if computer_choice1 == 1:
        print("The computer chose Paper, you lose")
    elif computer_choice1 == 2:
        print("The computer chose Scissors, You Win!!")
    else:
        print("Tie")
elif choice1 == 1:
    print("paper")
    computer_choice1 = random.randint(0,2)
    if computer_choice1 == 2:
        print("The computer chose Scissors, you lose")
    elif computer_choice1 == 0:
        print("The computer chose Rock, You Win!!")
    else:
        print("Tie")
elif choice1 == 2:
    print("scissors")
    computer_choice1 = random.randint(0,2)
    if computer_choice1 == 0:
        print("The computer chose Rock, you lose")
    elif computer_choice1 == 1:
        print("The computer chose Paper, You Win!!")
    else:
        print("Tie")
else:
    print("Invalid Input, Please input 0, 1, or 2!")