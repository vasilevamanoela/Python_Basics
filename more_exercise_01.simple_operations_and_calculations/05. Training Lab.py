import math

length_in_cm = float(input()) * 100
width_in_cm = float(input()) * 100

width_without_corridor = width_in_cm - 100
desks_on_row = math.floor(width_without_corridor / 70)

rows = math.floor(length_in_cm / 120)

number_places = (rows * desks_on_row) - 3

print(number_places)
