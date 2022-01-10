import sys

inpt = input()
max_number = -sys.maxsize

while inpt != 'Stop':
    number = int(inpt)

    if number > max_number:
        max_number = number

    inpt = input()

print(max_number)
