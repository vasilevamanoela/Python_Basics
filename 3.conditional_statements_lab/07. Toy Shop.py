price_holiday = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzles = number_puzzles * 2.60
dolls = number_dolls * 3
bears = number_bears * 4.10
minions = number_minions * 8.20
trucks = number_trucks * 2

sum_order = puzzles + dolls + bears + minions + trucks
total_number_toys = number_puzzles + number_dolls + number_bears + number_minions + number_trucks

if total_number_toys >= 50:
    sum_order *= 0.75

sum_order *= 0.90

difference = abs(sum_order - price_holiday)

if sum_order >= price_holiday:
    text = f'Yes! {difference:.2f} lv left.'
else:
    text = f'Not enough money! {difference:.2f} lv needed.'

print(text)
