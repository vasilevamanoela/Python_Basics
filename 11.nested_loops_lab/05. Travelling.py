destination = input()
money_saved = 0

while destination != 'End':
    budget = float(input())
    while money_saved < budget:
        money = float(input())
        money_saved += money
        if money_saved >= budget:
            print(f"Going to {destination}!")
            money_saved = 0
            break

    destination = input()

