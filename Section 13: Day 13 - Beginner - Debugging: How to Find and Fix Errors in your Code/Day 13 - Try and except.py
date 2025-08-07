try:
    age = int(input("How old are you?: "))
except ValueError:
    print("You have typed an invalid input, please enter a numerical value")
    age = int(input("How old are you?: "))


if age > 18:
    print(f"You can drive when you {age}")
