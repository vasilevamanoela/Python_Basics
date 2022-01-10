budget = float(input())
season = input()

vacation_type = ''
destination = ''
money_spend = 0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        money_spend = budget * 0.30
        vacation_type = 'Camp'
    elif season == 'winter':
        money_spend = budget * 0.70
        vacation_type = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        money_spend = budget * 0.40
        vacation_type = 'Camp'
    elif season == 'winter':
        money_spend = budget * 0.80
        vacation_type = 'Hotel'
elif budget > 1000:
    destination = 'Europe'
    money_spend = budget * 0.90
    vacation_type = 'Hotel'

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {money_spend:.2f}")


