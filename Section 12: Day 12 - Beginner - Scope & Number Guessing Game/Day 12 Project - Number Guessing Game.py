
#Decising a random number between 1 and 100
import random

answer = random.randint(1, 100)
# Function to set the difficulty
called_difficulty = input("\nWhat is the difficulty that you wish to have? Choose 'Easy' OR 'Hard':\n").lower()

lives = 0
if called_difficulty == 'easy':
    lives = 10
elif called_difficulty == 'hard':
    lives = 5
else:
    print("Please Choose A Difficulty")

game_over = False
guessed_number = []

while not game_over:

    print(f"You have {lives} Lives left!")
    called_guess = int(input("Choose a number between '1' and '100': \n"))

    if called_guess != answer:
        lives -= 1
        print(f"You guessed {called_guess}, that is not the number. You lose a life!")

    if lives == 0:
        game_over = True
        print(f"You Lose! The number was {answer}")


    if called_guess > answer:
        print(f"{called_guess} is too high!")
    elif called_guess < answer:
        print(f"{called_guess} is too low!")

    if called_guess != answer:
        guessed_number = called_guess
        print(f"The previous number chosen was {guessed_number}")

    if called_guess == answer:
        game_over = True
        print("\n" * 15)
        print(f"The correct number is {answer}")
        print("    Game Over!    ")


if lives == 0:
    game_over = True
    print("\n" * 15)
    print(f"The correct number was {answer}")
    print("    Game Over!    ")

# Let the user guess a number