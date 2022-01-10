import math

number_guests = int(input())
budget = int(input())

number_kozunaks = math.ceil(number_guests / 3)
number_eggs = number_guests * 2

total_kozunaks = number_kozunaks * 4
total_eggs = number_eggs * 0.45
total_sum = total_kozunaks + total_eggs
difference = abs(total_sum - budget)

if budget >= total_sum:
    print(f"Lyubo bought {number_kozunaks} Easter bread and {number_eggs} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")
