print("Welcome to Python Pizza Deliveries")
size = input("What size do you want? S, M or L?: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

#work out how much they need to pay based on their size and their choice

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Your input is invalid")


#What is their bill based on their pepperoni preference.
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3


#What is their final amount based on their cheese preference

if cheese == "Y":
    bill += 1


print(f"Your final bill is ${bill}.")

