type_projection = input()
number_rows = int(input())
number_columns = int(input())

price_premiere = 12
price_normal = 7.5
price_discount = 5

total_income = number_columns * number_rows

if type_projection == 'Premiere':
    total_income *= price_premiere
elif type_projection == 'Normal':
    total_income *= price_normal
elif type_projection == 'Discount':
    total_income *= price_discount

print(f'{total_income:.2f} leva')
