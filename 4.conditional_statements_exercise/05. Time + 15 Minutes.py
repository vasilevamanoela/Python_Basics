hour = int(input())
minutes = int(input())

minutes_after_15_minutes = minutes + 15

if minutes_after_15_minutes >= 60:
    hour += 1
    minutes_after_15_minutes -= 60

if hour > 23:
    hour = 0

if minutes_after_15_minutes < 10:
    print(f'{hour}:0{minutes_after_15_minutes}')
else:
    print(f'{hour}:{minutes_after_15_minutes}')
