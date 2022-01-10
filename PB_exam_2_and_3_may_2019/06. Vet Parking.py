days = int(input())
hours = int(input())
total_tax = 0

for day in range(1, days + 1):
    tax = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            tax += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    print(f"Day: {day} - {tax:.2f} leva")
    total_tax += tax

print(f"Total: {total_tax:.2f} leva")
