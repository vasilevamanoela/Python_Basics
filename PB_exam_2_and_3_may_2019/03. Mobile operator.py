period = input()
contract_type = input()
mobil_internet = input()
number_months = int(input())
tax = 0

if period == 'one':
    if contract_type == 'Small':
        tax = 9.98
    elif contract_type == 'Middle':
        tax = 18.99
    elif contract_type == 'Large':
        tax = 25.98
    elif contract_type == 'ExtraLarge':
        tax = 35.99
elif period == 'two':
    if contract_type == 'Small':
        tax = 8.58
    elif contract_type == 'Middle':
        tax = 17.09
    elif contract_type == 'Large':
        tax = 23.59
    elif contract_type == 'ExtraLarge':
        tax = 31.79

if mobil_internet == 'yes':
    if tax <= 10:
        tax += 5.5
    elif tax <= 30:
        tax += 4.35
    elif tax > 30:
        tax += 3.85

if period == 'two':
    tax *= 0.9625

total_price = tax * number_months

print(f"{total_price:.2f} lv.")
