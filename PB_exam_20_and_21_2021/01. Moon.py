import math

average_speed = float(input())
fuel_needed_100_km = float(input())

distance_go_and_back = 384400 * 2
time_go_and_back = math.ceil(distance_go_and_back / average_speed)
total_time = time_go_and_back + 3
total_fuel = int(fuel_needed_100_km * distance_go_and_back / 100)

print(total_time)
print(total_fuel)
