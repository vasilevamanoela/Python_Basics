import math

type_figure = input()

if type_figure == 'square':
    side = float(input())
    result = side * side
elif type_figure == 'rectangle':
    side_one = float(input())
    side_two = float(input())
    result = side_one * side_two
elif type_figure == 'circle':
    radios = float(input())
    result = math.pi * math.pow(radios, 2)
else:
    side = float(input())
    high = float(input())
    result = (side * high) / 2

print(f'{result:.3f}')
