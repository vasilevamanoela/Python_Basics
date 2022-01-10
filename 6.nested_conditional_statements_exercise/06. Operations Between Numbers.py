number_one = int(input())
number_two = int(input())
symbol = input()

result = 0

if symbol == '+':
    result = number_one + number_two
elif symbol == '-':
    result = number_one - number_two
elif symbol == '*':
    result = number_one * number_two
elif symbol == '/' and number_two != 0:
    result = number_one / number_two
elif symbol == '%' and number_two != 0:
    result = number_one % number_two

if symbol == '+' or symbol == '-' or symbol == '*':
    if result % 2 == 0:
        print(f'{number_one} {symbol} {number_two} = {result} - even')
    else:
        print(f'{number_one} {symbol} {number_two} = {result} - odd')
elif symbol == '/':
    if number_two != 0:
        print(f"{number_one} / {number_two} = {result:.2f}")
    else:
        print(f"Cannot divide {number_one} by zero")
elif symbol == '%':
    if number_two != 0:
        print(f"{number_one} % {number_two} = {result}")
    else:
        print(f"Cannot divide {number_one} by zero")
