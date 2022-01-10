budget = float(input())
name_product = input()
counter_products = 0
is_bigger = False
total_order = 0

while name_product != 'Stop':
    price_product = float(input())
    counter_products += 1
    if counter_products % 3 == 0:
        price_product /= 2
    if price_product > budget:
        is_bigger = True
        break
    budget -= price_product
    total_order += price_product

    name_product = input()

difference = price_product - budget

if is_bigger:
    print("You don't have enough money!")
    print(f"You need {difference:.2f} leva!")
else:
    print(f"You bought {counter_products} products for {total_order:.2f} leva.")