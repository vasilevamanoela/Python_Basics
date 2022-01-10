minutes_walking = int(input())
number_walks = int(input())
taken_calories = int(input())

total_walking_minutes = minutes_walking * number_walks
spend_calories = total_walking_minutes * 5
calories_target = taken_calories * 0.5

if spend_calories >= calories_target:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {spend_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {spend_calories}.")
