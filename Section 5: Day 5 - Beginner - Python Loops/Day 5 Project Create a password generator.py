import string
import random
letters = list(string.ascii_lowercase)
print(letters)
# Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']numbers = [str(i) for i in range(10)]
numbers = [str(i) for i in range(10)]
print(numbers)
symbols = ["!", "#", "$", "%", "&", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Easy mode

#password_list = ""
#for char in range(0, nr_letters):
    #password += random.choice(letters)

#for char in range(0, nr_symbols):
    #password += random.choice(symbols)

#for char in range(0, nr_numbers):
    #password += random.choice(numbers)

#print(password)
#Hard Mode

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is {password}")