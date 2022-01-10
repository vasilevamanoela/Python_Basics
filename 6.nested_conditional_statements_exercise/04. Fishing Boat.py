budget = int(input())
season = input()
fisherman_count = int(input())

price_rent = 0

if season == 'Spring':
    price_rent = 3000
elif season == 'Summer':
    price_rent = 4200
elif season == 'Autumn':
    price_rent = 4200
elif season == 'Winter':
    price_rent = 2600

if fisherman_count <= 6:
    price_rent *= 0.9
elif 7 <= fisherman_count <= 11:
    price_rent *= 0.85
elif fisherman_count > 12:
    price_rent *= 0.75

if fisherman_count % 2 == 0 and season != 'Autumn':
    price_rent *= 0.95

difference = abs(price_rent - budget)

if price_rent <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
