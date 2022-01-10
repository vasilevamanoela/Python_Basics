length = int(input())
width = int(input())
height = int(input())
volume_taken_percentage = float(input()) / 100

volume = length * width * height
total_capacity_liters = volume * 0.001
liters_needed = total_capacity_liters * (1 - volume_taken_percentage)

print(liters_needed)