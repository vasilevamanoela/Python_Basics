number_bad_grades = int(input())

counter_bad_grades = 0
sum_grades = 0
number_problems = 0
last_problem = ''
is_enough = False

while counter_bad_grades < number_bad_grades:
    name_problem = input()
    if name_problem != 'Enough':
        last_problem = name_problem

    if name_problem == 'Enough':
        is_enough = True
        break

    grade = int(input())

    sum_grades += grade
    number_problems += 1

    if grade <= 4:
        counter_bad_grades += 1

average_score = sum_grades / number_problems

if is_enough:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {number_problems}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {counter_bad_grades} poor grades.")
