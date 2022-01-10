import sys

inpt = input()
min_number = sys.maxsize

while inpt != 'Stop':
    number = int(inpt)

    if number < min_number:
        min_number = number

    inpt = input()

print(min_number)
