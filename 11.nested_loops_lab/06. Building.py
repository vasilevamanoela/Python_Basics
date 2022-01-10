number_floors = int(input())
number_rooms = int(input())

for f in range(number_floors, 0, -1):
    for r in range(0, number_rooms):
        if f == number_floors:
            print(f'L{f}{r}', end=" ")
        else:
            if f % 2 == 0:
                print(f'O{f}{r}', end=" ")
            else:
                print(f'A{f}{r}', end=" ")
    print("")

