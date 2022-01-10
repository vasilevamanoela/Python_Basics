beginning = int(input())
end = int(input())
magic_number = int(input())
combination = 0
valid_combination = 0
is_valid = False
n1 = 0
n2 = 0

for n1 in range(beginning, end + 1):
    for n2 in range(beginning, end + 1):
        combination += 1
        if n1 + n2 == magic_number:
            valid_combination = combination
            n1 = n1
            n2 = n2
            is_valid = True
            break
    if is_valid:
        break

if is_valid:
    print(f"Combination N:{valid_combination} ({n1} + {n2} = {magic_number})")
else:
    print(f"{combination} combinations - neither equals {magic_number}")
