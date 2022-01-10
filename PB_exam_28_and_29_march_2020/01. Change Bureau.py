number_bitcoin = int(input())
number_ioan = float(input())
commission = float(input())

bitcoins_lv = number_bitcoin * 1168
ioan_dollar = number_ioan * 0.15
dollar_lv = ioan_dollar * 1.76
total_in_lv = bitcoins_lv + dollar_lv
total_in_euro = total_in_lv / 1.95
total_euro_with_commission = total_in_euro * commission / 100
result = total_in_euro - total_euro_with_commission

print(f'{result:.2f}')

