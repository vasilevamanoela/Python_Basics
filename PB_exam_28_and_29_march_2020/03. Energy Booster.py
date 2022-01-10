fruit = input()
type_set = input()
number_sets = int(input())
total_sum = 0

if type_set == 'small':
    if fruit == 'Watermelon':
        total_sum = 2 * 56
    elif fruit == 'Mango':
        total_sum = 2 * 36.66
    elif fruit == 'Pineapple':
        total_sum = 2 * 42.10
    elif fruit == 'Raspberry':
        total_sum = 2 * 20
elif type_set == 'big':
    if fruit == 'Watermelon':
        total_sum = 5 * 28.70
    elif fruit == 'Mango':
        total_sum = 5 * 19.60
    elif fruit == 'Pineapple':
        total_sum = 5 * 24.80
    elif fruit == 'Raspberry':
        total_sum = 5 * 15.20

total_sum *= number_sets

if 400 <= total_sum <= 1000:
    total_sum *= 0.85
elif total_sum > 1000:
    total_sum *= 0.5

print(f"{total_sum:.2f} lv.")
