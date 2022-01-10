number_balls = int(input())
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
others_count = 0
total_points = 0

for i in range(number_balls):
    color = input()

    if color == 'red':
        total_points += 5
        red_count += 1
    elif color == 'orange':
        total_points += 10
        orange_count += 1
    elif color == 'yellow':
        total_points += 15
        yellow_count += 1
    elif color == 'white':
        total_points += 20
        white_count += 1
    elif color == 'black':
        total_points /= 2
        black_count += 1
    else:
        others_count += 1
        continue

print(f'Total points: {int(total_points)}')
print(f'Points from red balls: {red_count}')
print(f'Points from orange balls: {orange_count}')
print(f'Points from yellow balls: {yellow_count}')
print(f'Points from white balls: {white_count}')
print(f'Other colors picked: {others_count}')
print(f'Divides from black balls: {black_count}')
