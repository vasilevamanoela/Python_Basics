number_eggs_first = int(input())
number_eggs_second = int(input())
command = input()

while command != 'End of battle':
    if command == 'one':
        number_eggs_second -= 1
    elif command == 'two':
        number_eggs_first -= 1

    if number_eggs_first <= 0:
        print(f"Player one is out of eggs. Player two has {number_eggs_second} eggs left.")
        break

    if number_eggs_second <= 0:
        print(f"Player two is out of eggs. Player one has {number_eggs_first} eggs left.")
        break

    command = input()

if number_eggs_first > 0 and number_eggs_second > 0:
    print(f"Player one has {number_eggs_first} eggs left.")
    print(f"Player two has {number_eggs_second} eggs left.")
