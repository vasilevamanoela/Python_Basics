n = int(input())
is_valid = False
combination = 0

for x1 in range(0, n + 1):
    for x2 in range(0, n + 1):
        for x3 in range(0, n + 1):
            if x1 + x2 + x3 == n:
                is_valid = True
                combination += 1
                break
print(combination)
