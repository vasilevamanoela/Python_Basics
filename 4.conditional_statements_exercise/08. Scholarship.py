import math

income = float(input())
average_grade = float(input())
min_salary = float(input())

social = False
grade = False

social_scholarship = math.floor(min_salary * 0.35)
grade_scholarship = math.floor(average_grade * 25)

if (income < min_salary) & (average_grade > 4.5):
    social = True

if average_grade >= 5.5:
    grade = True

if (social == True) & (grade == True):
    if social_scholarship <= grade_scholarship:
        print(f"You get a scholarship for excellent results {grade_scholarship} BGN")
    else:
        print(f"You get a Social scholarship {social_scholarship} BGN")
elif social == True:
    print(f"You get a Social scholarship {social_scholarship} BGN")
elif grade == True:
    print(f"You get a scholarship for excellent results {grade_scholarship} BGN")
else:
    print("You cannot get a scholarship!")
