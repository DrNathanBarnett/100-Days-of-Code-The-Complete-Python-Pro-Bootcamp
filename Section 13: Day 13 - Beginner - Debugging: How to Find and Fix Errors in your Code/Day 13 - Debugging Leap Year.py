#Original code

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


#corrected to be

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 4000 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


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
