text = input()
total = 0

while text != "NoMoreMoney":
    money = float(text)

    if money < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {money:.2f}')
    total += money
    text = input()

print(f'Total: {total:.2f}')