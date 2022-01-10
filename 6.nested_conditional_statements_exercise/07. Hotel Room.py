month = input()
nights_count = int(input())

price_studio = 0
price_apartment = 0

if month == 'May' or month == 'October':
    price_studio = nights_count * 50
    price_apartment = nights_count * 65
    if 7 < nights_count <= 14:
        price_studio *= 0.95
    elif nights_count > 14:
        price_studio *= 0.70
elif month == 'June' or month == 'September':
    price_studio = nights_count * 75.20
    price_apartment = nights_count * 68.70
    if nights_count > 14:
        price_studio *= 0.80
elif month == 'July' or month == 'August':
    price_studio = nights_count * 76
    price_apartment = nights_count * 77

if nights_count > 14:
    price_apartment *= 0.9

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
