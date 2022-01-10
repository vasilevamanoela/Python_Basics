price_vegetables = float(input())
price_fruits = float(input())
total_quantity_vegetables = int(input())
total_quantity_fruits = int(input())

total_vegetables = price_vegetables * total_quantity_vegetables
total_fruits = price_fruits * total_quantity_fruits

total_in_euro = (total_vegetables + total_fruits) / 1.94

print(f'{total_in_euro:.2f}')
