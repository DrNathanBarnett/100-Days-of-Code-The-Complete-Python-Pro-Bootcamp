"""Write a program that returns True or False whether if a given year is a leap year.

A normal year has 365 days, leap years have 366, with an extra day in February.


The reason why we have leap years is really fascinating, this video does it more justice"""


def is_leap_year(year):
    leap_year = False
    if year % 400 == 0 and year % 4 == 0:
        leap_year = True
    else:
        leap_year = False

    if leap_year == True:
        print(f"{year} is leap year")
    else:
        print(f"{year} is not a leap year")



is_leap_year(2000)
is_leap_year(2020)
is_leap_year(2024)
is_leap_year(2400)


#Other Solution Provided by Udemy

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False