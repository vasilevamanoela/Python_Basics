number = int(input())

valid = number == 0 or 100 <= number <= 200
if not valid:
    print('invalid')
