month = input()
hours_spent = int(input())
number_ppl = int(input())
daytime = input()
price = 0

if month == 'march' or month == 'april' or month == 'may':
    if daytime == 'day':
        price = 10.50
    elif daytime == 'night':
        price = 8.40
elif month == 'june' or month == 'july' or month == 'august':
    if daytime == 'day':
        price = 12.60
    elif daytime == 'night':
        price = 10.20

if number_ppl >= 4:
    price *= 0.9

if hours_spent >= 5:
    price *= 0.5

total_price = price * number_ppl * hours_spent

print(f"Price per person for one hour: {price:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
