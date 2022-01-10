n = int(input())

divided_by_2_count = 0
divided_by_3_count = 0
divided_by_4_count = 0

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        divided_by_2_count += 1

    if number % 3 == 0:
        divided_by_3_count += 1

    if number % 4 == 0:
        divided_by_4_count += 1

p1_percent = divided_by_2_count / n * 100
p2_percent = divided_by_3_count / n * 100
p3_percent = divided_by_4_count / n * 100

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
