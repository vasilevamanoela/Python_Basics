city = input()
type_pack = input()
vip_discount = input()
number_days = int(input())
total_sum = 0

if city == 'Bansko' or city == 'Borovets':
    if type_pack == 'withEquipment':
        total_sum = 100
        if vip_discount == 'yes':
            total_sum *= 0.8
    elif type_pack == 'noEquipment':
        total_sum = 80
        if vip_discount == 'yes':
            total_sum *= 0.95
elif city == 'Varna' or city == 'Burgas':
    if type_pack == 'withBreakfast':
        total_sum = 130
        if vip_discount == 'yes':
            total_sum *= 0.88
    elif type_pack == 'noBreakfast':
        total_sum = 100
        if vip_discount == 'yes':
            total_sum *= 0.93

if number_days < 1:
    print("Days must be positive number!")
else:
    if total_sum == 0:
        print("Invalid input!")
    else:
        if number_days > 7:
            number_days -= 1
        print(f"The price is {number_days * total_sum:.2f}lv! Have a nice time!")
