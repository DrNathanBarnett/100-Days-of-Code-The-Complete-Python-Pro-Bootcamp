import math
def is_prime(num):
    """
    Prime numbers are numbers that can only be cleanly divided by themselves and 1.
    You need to write a function called is_prime() that checks whether if the number passed into it is a prime number or not.
    It should return True or False.
    """
    if num == 2:
        return True
    if num <= 1:
        return False
    if num % 2 == 0:
        return False

    for i in range(2, num):
        if num % i == 0:
            print("False")
            return False
    print("True")
    return True

num = 2
print(is_prime(num))
num = 10
print(is_prime(num))
