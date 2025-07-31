#Life in weeks

#Create a function called life_in_weeks() using maths and
# f-Strings that tells us how many
# weeks we have left, if we live until 90 years old.


#It will take your current age as the input and output a
# message with our time left in this format:

#You have x weeks left.

#Where x is replaced with the actual calculated
#number of weeks the input age has left until age 90.

#Warning** The function must be called life_in_weeks for the
# tests to pass. Also the output must have the same
# punctuation and spelling as the example.
# Including the full stop!

def life_in_weeks(age):
    weeks_in_year = 52 * 90
    time_left = weeks_in_year - (age * 52)
    print(f"You have {time_left} weeks left.")

test_age_20 = life_in_weeks(20)
print(test_age_20)

test_age_40 = life_in_weeks(40)
print(test_age_40)

test_age_70 = life_in_weeks(70)
print(test_age_70)