number_chicken_menu = int(input())
number_fish_menu = int(input())
number_vegetarian_menu = int(input())

sum_chicken = number_chicken_menu * 10.35
sum_fish = number_fish_menu * 12.4
sum_vegetarian = number_vegetarian_menu * 8.15

sum_with_desert = (sum_chicken + sum_fish + sum_vegetarian) * 1.2
total_sum_with_delivery = sum_with_desert + 2.5

print(f"Total: {total_sum_with_delivery:.2f}")
