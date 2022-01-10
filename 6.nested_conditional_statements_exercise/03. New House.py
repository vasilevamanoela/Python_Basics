flower_type = input()
number_flowers = int(input())
budget = int(input())

total_flowers = 0

if flower_type == 'Roses':
    if number_flowers > 80:
        total_flowers = (number_flowers * 5) * 0.9
    else:
        total_flowers = number_flowers * 5
elif flower_type == 'Dahlias':
    if number_flowers > 90:
        total_flowers = (number_flowers * 3.8) * 0.85
    else:
        total_flowers = number_flowers * 3.8
elif flower_type == 'Tulips':
    if number_flowers > 80:
        total_flowers = (number_flowers * 2.8) * 0.85
    else:
        total_flowers = number_flowers * 2.8
elif flower_type == 'Narcissus':
    if number_flowers < 120:
        total_flowers = (number_flowers * 3) * 0.15 + (number_flowers * 3)
    else:
        total_flowers = number_flowers * 3
elif flower_type == 'Gladiolus':
    if number_flowers < 80:
        total_flowers = (number_flowers * 2.5) * 0.20 + (number_flowers * 2.5)
    else:
        total_flowers = number_flowers * 2.5

difference = abs(total_flowers - budget)

if budget >= total_flowers:
    print(f"Hey, you have a great garden with {number_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
