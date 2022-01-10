number_windows = int(input())
type_windows = input()
shipment_method = input()

total_sum = 0

if type_windows == '90X130':
    total_sum = number_windows * 110
    if 30 < number_windows <= 60:
        total_sum *= 0.95
    elif number_windows > 60:
        total_sum *= 0.92

elif type_windows == '100X150':
    total_sum = number_windows * 140
    if 40 < number_windows <= 80:
        total_sum *= 0.94
    elif number_windows > 80:
        total_sum *= 0.90

elif type_windows == '130X180':
    total_sum = number_windows * 190
    if 20 < number_windows <= 50:
        total_sum *= 0.93
    elif number_windows > 50:
        total_sum *= 0.88

elif type_windows == '200X300':
    total_sum = number_windows * 250
    if 25 < number_windows <= 50:
        total_sum *= 0.91
    elif number_windows > 50:
        total_sum *= 0.86

if shipment_method == 'With delivery':
    total_sum += 60

if number_windows > 99:
    total_sum *= 0.96

if number_windows < 10:
    print("Invalid order")
else:
    print(f"{total_sum:.2f} BGN")
