profit = float(input())
cocktail_name = input()
price_cocktail = 0
price_order = 0
total_sum = 0

while cocktail_name != 'Party!':
    number_cocktails = int(input())
    price_cocktail = len(cocktail_name)
    price_order = price_cocktail * number_cocktails

    if price_order % 2 != 0:
        price_order *= 0.75

    total_sum += price_order
    if total_sum >= profit:
        break

    cocktail_name = input()

difference = profit - total_sum
if total_sum >= profit:
    print("Target acquired.")
else:
    print(f"We need {difference:.2f} leva more.")

print(f"Club income - {total_sum:.2f} leva.")