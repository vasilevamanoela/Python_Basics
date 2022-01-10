import math

number_ppl = int(input())
price_entrance = float(input())
price_sunbed = float(input())
price_umbrella = float(input())

sum_entrance = number_ppl * price_entrance
sum_umbrella = math.ceil(number_ppl / 2) * price_umbrella
sum_sunbed = math.ceil(number_ppl * 0.75) * price_sunbed

total_sum = sum_entrance + sum_umbrella + sum_sunbed

print(f'{total_sum:.2f} lv.')
