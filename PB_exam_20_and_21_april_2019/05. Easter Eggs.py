import sys

number_eggs = int(input())
red_count = 0
orange_count = 0
blue_count = 0
green_count = 0
max_egg = -sys.maxsize
max_color = ''

for egg in range(number_eggs):
    color = input()
    if color == 'red':
        red_count += 1
    elif color == 'orange':
        orange_count += 1
    elif color == 'blue':
        blue_count += 1
    elif color == 'green':
        green_count += 1

    if red_count > max_egg:
        max_egg = red_count
        max_color = color
    elif orange_count > max_egg:
        max_egg = orange_count
        max_color = color
    elif blue_count > max_egg:
        max_egg = blue_count
        max_color = color
    elif green_count > max_egg:
        max_egg = green_count
        max_color = color

print(f"Red eggs: {red_count}")
print(f"Orange eggs: {orange_count}")
print(f"Blue eggs: {blue_count}")
print(f"Green eggs: {green_count}")
print(f"Max eggs: {max_egg} -> {max_color}")
