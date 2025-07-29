import random

word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []
while not game_over:

    print(f"You have {lives} left!")
    called_guess = input("Choose a letter of the alphabet: ").lower()

    if called_guess in correct_letters:
        print(f"You have already guessed {called_guess}!")
    display = ""

    for letter in chosen_word:
        if letter == called_guess:
            display += letter
            correct_letters.append(called_guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if called_guess not in chosen_word:
        lives -= 1
        print(f"You guessed {called_guess}, that is not in the word. You lose a life!")

        if lives == 0:
            game_over = True
            print(f"You Lose! The word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win!")




