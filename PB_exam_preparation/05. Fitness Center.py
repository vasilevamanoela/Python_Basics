number_visitors = int(input())
back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
proteint_shake_count = 0
protein_bar_count = 0

for i in range(number_visitors):
    activity = input()

    if activity == "Back":
        back_count += 1
    elif activity == 'Chest':
        chest_count += 1
    elif activity == 'Legs':
        legs_count += 1
    elif activity == 'Abs':
        abs_count += 1
    elif activity == 'Protein shake':
        proteint_shake_count += 1
    elif activity == 'Protein bar':
        protein_bar_count += 1

sport_count = back_count + chest_count + legs_count + abs_count
buy_count = proteint_shake_count + protein_bar_count
percent_sport_activities = sport_count / number_visitors * 100
percent_buyers = buy_count / number_visitors * 100

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{proteint_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{percent_sport_activities:.2f}% - work out")
print(f"{percent_buyers:.2f}% - protein")
