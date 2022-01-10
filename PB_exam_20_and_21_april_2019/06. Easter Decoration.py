number_clients = int(input())
total_purchase = 0

for n in range(number_clients):
    purchase_type = input()
    purchase_clients = 0
    purchase_count = 0
    while purchase_type != 'Finish':
        if purchase_type == 'basket':
            purchase_clients += 1.50
        elif purchase_type == 'wreath':
            purchase_clients += 3.80
        elif purchase_type == 'chocolate bunny':
            purchase_clients += 7

        purchase_count += 1
        purchase_type = input()

    if purchase_count % 2 == 0:
        purchase_clients *= 0.8
    print(f"You purchased {purchase_count} items for {purchase_clients:.2f} leva.")
    total_purchase += purchase_clients

average_purchase = total_purchase / number_clients
print(f"Average bill per client is: {average_purchase:.2f} leva.")
