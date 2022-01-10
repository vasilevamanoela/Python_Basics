fruit = input()
day = input()
quantity = float(input())

result = 0
is_error = False

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        result = quantity * 2.50
    elif fruit == 'apple':
        result = quantity * 1.20
    elif fruit == 'orange':
        result = quantity * 0.85
    elif fruit == 'grapefruit':
        result = quantity * 1.45
    elif fruit == 'kiwi':
        result = quantity * 2.70
    elif fruit == 'pineapple':
        result = quantity * 5.50
    elif fruit == 'grapes':
        result = quantity * 3.85
    else:
        is_error = True
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        result = quantity * 2.70
    elif fruit == 'apple':
        result = quantity * 1.25
    elif fruit == 'orange':
        result = quantity * 0.90
    elif fruit == 'grapefruit':
        result = quantity * 1.60
    elif fruit == 'kiwi':
        result = quantity * 3.00
    elif fruit == 'pineapple':
        result = quantity * 5.60
    elif fruit == 'grapes':
        result = quantity * 4.20
    else:
        is_error = True
else:
    is_error = True

if is_error:
    print('error')
else:
    print(f'{result:.2f}')
