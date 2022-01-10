budget = float(input())
number_people = int(input())
price_for_clothes = float(input())

money_decor = budget * 0.1
money_clothes = number_people * price_for_clothes

if number_people > 150:
    money_clothes *= 0.9

total_amount = money_decor + money_clothes

difference = abs(budget - total_amount)

if total_amount > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
