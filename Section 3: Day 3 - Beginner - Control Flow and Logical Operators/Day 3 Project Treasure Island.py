print("Welcome to treasure island")
print("Your mission is to try and find all of the treasure")

choice1 = input("You\'re at a crossroad, where do you want to go?\nType 'Left' or 'Right'.").lower()

if choice1 == "right":
    print("Game Over!\n You fell into a hole!")
elif choice1 == "left":
    #You will continue the game.
    choice2 = input("You are safe for now, "
                    "you move towards the left-side door and creep through. "
                    "The room is dark and there is a ladder or a set of stairs.\nChoose 'Ladder' or 'Stairs'\n").lower()
    if choice2 == "stairs":
        #Game will continue
         choice3 = input("You move down the stairs and go through the back,"
                         "you come to a lake unharmed,"
                         "On the edge of the lake you see a house with 3 doors,"
                         "\nOne yellow\nOne red\nOne blue\n"
                         "Which colour do you choose?\n").lower()
         if choice3 == 'yellow':
            print("It is a room through of fire, you burn to death."
                  "Game Over")
         elif choice3 == 'red':
            print("You found the treasure,"
                  "You win!")
         elif choice3 == 'blue':
            print("You chose a room full of untamed beasts. "
                  "Game Over!")
         else:
            print("You chose a door that does not exist."
                  "Game Over!")
    else:
        print("You were attacked by a tormented demon and died")

else:
    print("Invalid input, you must choose your path")


