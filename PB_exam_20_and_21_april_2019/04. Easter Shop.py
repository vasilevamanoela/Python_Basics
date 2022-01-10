quantity_eggs = int(input())
command = input()
total_sell_eggs = 0

while command != 'Close':
    number_eggs = int(input())

    if quantity_eggs < number_eggs and command == 'Buy':
        print("Not enough eggs in store!")
        print(f"You can buy only {quantity_eggs}.")
        exit()

    if command == 'Buy':
        quantity_eggs -= number_eggs
        total_sell_eggs += number_eggs
    elif command == 'Fill':
        quantity_eggs += number_eggs

    command = input()

print(f"Store is closed!")
print(f"{total_sell_eggs} eggs sold.")
