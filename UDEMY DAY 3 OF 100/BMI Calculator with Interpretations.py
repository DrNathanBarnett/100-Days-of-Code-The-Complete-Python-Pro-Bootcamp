#Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

#If the bmi is under 18.5 (not including), print out "underweight"

#If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

#If the bmi is 25 (including) or over, print out "overweight"

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

print("Welcoem to the BMI Calculator")
if bmi < 18.5:
    print("underweight")
elif bmi >= 18.5:
    print("normal weight range")
elif bmi < 25:
    print("nomral weight range")
else:
    print("overweight")
