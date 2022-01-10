budget = float(input())
fuel_needed = float(input())
day = input()

price_fuel = fuel_needed * 2.1
total_sum = price_fuel + 100

if day == 'Saturday':
    total_sum *= 0.9
elif day == 'Sunday':
    total_sum *= 0.8

difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
