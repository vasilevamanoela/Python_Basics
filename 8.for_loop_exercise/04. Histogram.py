n = int(input())

p1_diapason = 0
p2_diapason = 0
p3_diapason = 0
p4_diapason = 0
p5_diapason = 0

for i in range(n):
    number = int(input())

    if number < 200:
        p1_diapason += 1
    elif 200 <= number <= 399:
        p2_diapason += 1
    elif 400 <= number <= 599:
        p3_diapason += 1
    elif 600 <= number <= 799:
        p4_diapason += 1
    elif number >= 800:
        p5_diapason += 1

p1_percent = (p1_diapason / n) * 100
p2_percent = (p2_diapason / n) * 100
p3_percent = (p3_diapason / n) * 100
p4_percent = (p4_diapason / n) * 100
p5_percent = (p5_diapason / n) * 100

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')
