movie_name = input()
student_count = 0
standard_count = 0
kid_count = 0

while movie_name != 'Finish':
    free_places = int(input())
    busy_seats = 0

    for i in range(free_places):
        ticket_type = input()
        if ticket_type == 'student':
            student_count += 1
        elif ticket_type == 'standard':
            standard_count += 1
        elif ticket_type == 'kid':
            kid_count += 1
        elif ticket_type == 'End':
            break

        busy_seats += 1

    total_tickets = standard_count + student_count + kid_count
    percent_full = busy_seats / free_places * 100
    print(f"{movie_name} - {percent_full:.2f}% full.")

    movie_name = input()

student_percent = student_count / total_tickets * 100
standard_percent = standard_count / total_tickets * 100
kid_percent = kid_count / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{student_percent:.2f}% student tickets.")
print(f"{standard_percent:.2f}% standard tickets.")
print(f"{kid_percent:.2f}% kids tickets.")
