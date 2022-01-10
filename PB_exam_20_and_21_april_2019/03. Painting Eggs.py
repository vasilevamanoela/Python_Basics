size_eggs = input()
color_eggs = input()
number_shipments = int(input())
price_eggs = 0

if size_eggs == 'Large':
    if color_eggs == 'Red':
        price_eggs = 16
    elif color_eggs == 'Green':
        price_eggs = 12
    elif color_eggs == 'Yellow':
        price_eggs = 9
elif size_eggs == 'Medium':
    if color_eggs == 'Red':
        price_eggs = 13
    elif color_eggs == 'Green':
        price_eggs = 9
    elif color_eggs == 'Yellow':
        price_eggs = 7
elif size_eggs == 'Small':
    if color_eggs == 'Red':
        price_eggs = 9
    elif color_eggs == 'Green':
        price_eggs = 8
    elif color_eggs == 'Yellow':
        price_eggs = 5

total = number_shipments * price_eggs
costs = total * 0.35
result = total - costs

print(f"{result:.2f} leva.")
