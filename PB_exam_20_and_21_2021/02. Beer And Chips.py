import math
name = input()
budget = float(input())
number_beers = int(input())
number_chips = int(input())

sum_beers = number_beers * 1.2
price_chips = sum_beers * 0.45
sum_chips = math.ceil(number_chips * price_chips)

total_sum = sum_beers + sum_chips

difference = abs(budget - total_sum)

if budget >= total_sum:
    print(f"{name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{name} needs {difference:.2f} more leva!")
