number_ppl = int(input())
presentation_name = input()
presentation_count = 0
presentation_grades = 0
total_grades = 0
average_presentation_grade = 0

while presentation_name != 'Finish':
    for i in range(number_ppl):
        grade = float(input())
        presentation_grades += grade
    average_presentation_grade = presentation_grades / number_ppl
    print(f"{presentation_name} - {average_presentation_grade:.2f}.")
    presentation_grades = 0
    total_grades += average_presentation_grade
    presentation_count += 1
    presentation_name = input()

print(f"Student's final assessment is {(total_grades / presentation_count):.2f}.")
