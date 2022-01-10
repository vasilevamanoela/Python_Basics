budget = float(input())
number_video_card = int(input())
number_processors = int(input())
number_ram = int(input())

sum_video_card = number_video_card * 250
sum_processors = sum_video_card * 0.35 * number_processors
sum_ram = sum_video_card * 0.1 * number_ram

total_sum = sum_video_card + sum_processors + sum_ram

if number_video_card > number_processors:
    total_sum *= 0.85

difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
