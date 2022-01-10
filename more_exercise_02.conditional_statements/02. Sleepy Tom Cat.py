number_days_off = int(input())

plays_days_off = number_days_off * 127
plays_working_days = (365 - number_days_off) * 63

total_plays = plays_days_off + plays_working_days
difference = abs(30000 - total_plays)

total_plays_hours = difference // 60
total_plays_minutes = difference % 60

if total_plays > 30000:
    print(f'Tom will run away')
    print(f'{total_plays_hours} hours and {total_plays_minutes} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{total_plays_hours} hours and {total_plays_minutes} minutes less for play')
