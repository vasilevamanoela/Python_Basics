number_cats = int(input())
small_cats_count = 0
big_cats_count = 0
huge_cats_count = 0
total_grams_eaten = 0

for cat in range(number_cats):
    eaten_food = float(input())

    if 100 <= eaten_food < 200:
        small_cats_count += 1
    elif 200 <= eaten_food < 300:
        big_cats_count += 1
    elif 300 <= eaten_food < 400:
        huge_cats_count += 1

    total_grams_eaten += eaten_food

price_food_per_day = (total_grams_eaten / 1000) * 12.45

print(f"Group 1: {small_cats_count} cats.")
print(f"Group 2: {big_cats_count} cats.")
print(f"Group 3: {huge_cats_count} cats.")
print(f"Price for food per day: {price_food_per_day:.2f} lv.")
