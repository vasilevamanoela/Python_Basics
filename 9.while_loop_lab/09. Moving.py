w_free_place = int(input())
l_free_place = int(input())
h_free_place = int(input())
inpt = input()

free_place = w_free_place * l_free_place * h_free_place
taken_place = 0

while inpt != 'Done':
    number_boxes = int(inpt)

    taken_place += number_boxes

    if taken_place > free_place:
        break

    inpt = input()

difference = abs(taken_place - free_place)

if free_place >= taken_place:
    print(f"{difference} Cubic meters left.")
else:
    print(f"No more free space! You need {difference} Cubic meters more.")
