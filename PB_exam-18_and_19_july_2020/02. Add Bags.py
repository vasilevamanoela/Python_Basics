price_luggage_over_20kg = float(input())
luggage_kg = float(input())
days_travelling = int(input())
number_luggage = int(input())

tax_for_luggage = 0
total_sum = 0

if luggage_kg < 10:
    tax_for_luggage = 0.2 * price_luggage_over_20kg
elif 10 <= luggage_kg <= 20:
    tax_for_luggage = 0.5 * price_luggage_over_20kg
elif luggage_kg > 20:
    tax_for_luggage = price_luggage_over_20kg

if days_travelling > 30:
    tax_for_luggage *= 1.1
elif 7 <= days_travelling <= 30:
    tax_for_luggage *= 1.15
elif days_travelling < 7:
    tax_for_luggage *= 1.4

total_sum = tax_for_luggage * number_luggage

print(f"The total price of bags is: {total_sum:.2f} lv.")
