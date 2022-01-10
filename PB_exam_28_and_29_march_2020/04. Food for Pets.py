days = int(input())
total_food = float(input())
eaten_biscuits = 0
total_eaten_food = 0
food_dog = 0
food_cat = 0

for day in range(1, days + 1):
    quantity_eaten_dog = int(input())
    quantity_eaten_cat = int(input())

    if day % 3 == 0:
        eaten_biscuits = (quantity_eaten_dog + quantity_eaten_cat) * 0.1

    food_dog += quantity_eaten_dog
    food_cat += quantity_eaten_cat

total_eaten_food = food_dog + food_cat
total_eaten_food_percent = total_eaten_food / total_food * 100
food_dog_percent = food_dog / total_eaten_food * 100
food_cat_percent = food_cat / total_eaten_food * 100

print(f"Total eaten biscuits: {round(eaten_biscuits)}gr.")
print(f"{total_eaten_food_percent:.2f}% of the food has been eaten.")
print(f"{food_dog_percent:.2f}% eaten from the dog.")
print(f"{food_cat_percent:.2f}% eaten from the cat.")


