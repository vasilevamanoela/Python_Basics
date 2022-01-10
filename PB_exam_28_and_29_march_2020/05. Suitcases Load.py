volume_cargo = float(input())
inpt = input()
count_loaded_luggage = 0

while inpt != 'End':
    volume_luggage = float(inpt)
    count_loaded_luggage += 1
    if count_loaded_luggage % 3 == 0 and count_loaded_luggage != 0:
        volume_luggage *= 1.1
    volume_cargo -= volume_luggage

    if volume_cargo < 0:
        print("No more space!")
        count_loaded_luggage -= 1
        break
    inpt = input()

if volume_cargo >= 0:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {count_loaded_luggage} suitcases loaded.")