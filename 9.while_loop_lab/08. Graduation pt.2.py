name = input()

grade = float(input())
sum_grades = 0
count_grades = 1
count_failed_grades = 0
is_excluded = False

while count_grades <= 12:
    sum_grades += grade

    if count_grades == 12:
        break

    if grade < 4.00:
        count_failed_grades += 1

    if count_failed_grades > 1:
        is_excluded = True
        break

    count_grades += 1
    grade = float(input())

average_grade = sum_grades / count_grades

if is_excluded:
    print(f'{name} has been excluded at {count_grades - 1} grade')
else:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
