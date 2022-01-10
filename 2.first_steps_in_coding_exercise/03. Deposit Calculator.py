deposit = float(input())
period_deposit = int(input())
annual_interest_rate = float(input())

total_rate = (deposit * annual_interest_rate) / 100
month_rate = total_rate / 12
total_sum = deposit + (period_deposit * month_rate)

print(f'{total_sum:.2f}')