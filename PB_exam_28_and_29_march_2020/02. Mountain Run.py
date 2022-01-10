import math

record_sec = float(input())
distance = float(input())
time_climb_1m = float(input())

time_climbing_sec = distance * time_climb_1m
time_delay = math.floor(distance / 50)
time_delay_sec = time_delay * 30
total_time = time_climbing_sec + time_delay_sec

if total_time < record_sec:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    print(f"No! He was {(total_time - record_sec):.2f} seconds slower.")