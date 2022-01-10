number_guests = int(input())
price_per_person = float(input())
budget = float(input())

if 10 <= number_guests <= 15:
    price_per_person *= 0.85
elif 15 < number_guests <= 20:
    price_per_person *= 0.8
elif number_guests > 20:
    price_per_person *= 0.75

price_cake = budget * 0.1

total_sum = number_guests * price_per_person + price_cake
difference = abs(total_sum - budget)
if budget >= total_sum:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
