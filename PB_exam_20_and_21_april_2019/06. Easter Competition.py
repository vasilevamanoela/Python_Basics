import sys
number_kozunaks = int(input())
max_points = -sys.maxsize
best_backer = ''

for n in range(number_kozunaks):
    name_backer = input()
    inpt = input()
    backer_points = 0
    while inpt != 'Stop':
        points = int(inpt)
        backer_points += points

        inpt = input()
    print(f"{name_backer} has {backer_points} points.")
    if backer_points > max_points:
        max_points = backer_points
        best_backer = name_backer
        print(f"{best_backer} is the new number 1!")

print(f"{best_backer} won competition with {max_points} points!")