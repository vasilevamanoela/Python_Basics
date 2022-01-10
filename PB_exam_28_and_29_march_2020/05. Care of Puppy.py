bought_food_kg = int(input())
inpt = input()
total_eaten_food_gr = 0

while inpt != 'Adopted':
    eaten_food_gr = int(inpt)
    total_eaten_food_gr += eaten_food_gr
    inpt = input()

bought_food_gr = bought_food_kg * 1000
difference = abs(bought_food_gr - total_eaten_food_gr)

if bought_food_gr >= total_eaten_food_gr:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")
