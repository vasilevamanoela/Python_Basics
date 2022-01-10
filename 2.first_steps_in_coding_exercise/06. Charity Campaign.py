days_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

total_cakes = cakes_count * 45
total_waffles = waffles_count * 5.8
total_pancakes = pancakes_count * 3.2

total_sum = (total_cakes + total_waffles + total_pancakes) * days_count * bakers_count
costs = total_sum * 0.125
total_sum_after_costs = total_sum - costs

print(total_sum_after_costs)