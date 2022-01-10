money_needed = float(input())
money_have = float(input())
counter_days = 0
counter_spend_days = 0
are_spend_above_5 = False

while money_have < money_needed:
    type_action = input()
    amount = float(input())
    counter_days += 1

    if type_action == 'save':
        money_have += amount
        counter_spend_days = 0
    elif type_action == 'spend':
        counter_spend_days += 1
        money_have -= amount
        if amount > money_have:
            money_have = 0

        if counter_spend_days >= 5:
            are_spend_above_5 = True
            break

if are_spend_above_5:
    print("You can't save the money.")
    print(f"{counter_days}")
else:
    print(f"You saved the money for {counter_days} days.")
