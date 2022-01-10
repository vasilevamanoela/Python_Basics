w_cake = int(input())
h_cake = int(input())

cake_size = w_cake * h_cake
eaten_pieces = 0

inpt = input()

while inpt != 'STOP':
    piece = int(inpt)

    eaten_pieces += piece

    if eaten_pieces > cake_size:
        break

    inpt = input()

difference = abs(eaten_pieces - cake_size)

if eaten_pieces > cake_size:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")
