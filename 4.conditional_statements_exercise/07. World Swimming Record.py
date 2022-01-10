import math

record_seconds = float(input())
distance_meters = float(input())
time_seconds = float(input())

swim_time_seconds = distance_meters * time_seconds
slow_time_count = math.floor(distance_meters / 15)
added_time = slow_time_count * 12.5

total_time = swim_time_seconds + added_time

difference = abs(record_seconds - total_time)

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
