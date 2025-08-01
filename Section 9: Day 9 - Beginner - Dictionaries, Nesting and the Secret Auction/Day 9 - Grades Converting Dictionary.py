#Write a program that converts their scores to grades.

#By the end of your program, you should have a new dictionary called student_grades
#that should contain student names as keys and their assessed grades for values.

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
student_grades['Harry'] = "Exceeds Expectations"
student_grades['Ron'] = "Acceptable"
student_grades['Hermione'] = "Outstanding"
student_grades['Draco'] = "Acceptable"
student_grades['Neville'] = "Fail"

print(student_grades)


#student_grades = {
 #   'Harry': "Exceeds Expectations",
  #  'Ron': "Acceptable",
   # 'Hermione': "Outstanding",
    #'Draco': "Acceptable",
    #'Neville': "Fail"
#}