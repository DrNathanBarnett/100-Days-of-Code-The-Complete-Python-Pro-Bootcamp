#TASK 1

#make some code that prints the type of each data type
#print(type(123))
#print(type(1.1))
#print(type(True))
#print(type("String ?\n X"))

#Task 2 - Make this code work

#print("Print the number of letters in your name: " + len(input("Enter your name")))

#Answer

#print("Print the number of letters in your name: " + str(len(input("Enter your name"))))


print("Welcome to the tip calculator!")
bill = float(input("What was the total of the bill"))
tip = int(input("What is the total percentage of the tip? 5 10 15? "))
people = int(input("How many people will split the bill? "))
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
toal_bill = bill + total_tip_amount
bill_per_person = toal_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: $ {final_amount}")