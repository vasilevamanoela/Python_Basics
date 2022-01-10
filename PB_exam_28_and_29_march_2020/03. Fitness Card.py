money_have = float(input())
gender = input()
age = int(input())
sport = input()
total_price = 0

if gender == 'm':
    if sport == 'Gym':
        total_price = 42
    elif sport == 'Boxing':
        total_price = 41
    elif sport == 'Yoga':
        total_price = 45
    elif sport == 'Zumba':
        total_price = 34
    elif sport == 'Dances':
        total_price = 51
    elif sport == 'Pilates':
        total_price = 39
elif gender == 'f':
    if sport == 'Gym':
        total_price = 35
    elif sport == 'Boxing':
        total_price = 37
    elif sport == 'Yoga':
        total_price = 42
    elif sport == 'Zumba':
        total_price = 31
    elif sport == 'Dances':
        total_price = 53
    elif sport == 'Pilates':
        total_price = 37

if age <= 19:
    total_price *= 0.80

if total_price <= money_have:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${total_price - money_have:.2f} more.")
