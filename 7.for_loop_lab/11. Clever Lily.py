age = int(input())
price_laundry = float(input())
price_toy = int(input())

money_received = 0
toys_received_count = 0
even_birthdays_count = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        even_birthdays_count += 1
        money_received += 10 * even_birthdays_count
    else:
        toys_received_count += 1

taken_money = even_birthdays_count * 1
money_from_toys = toys_received_count * price_toy

actual_money_saved = money_received + money_from_toys - taken_money

difference = abs(actual_money_saved - price_laundry)

if actual_money_saved >= price_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
