days_stayed = int(input())
room_type = input()
feedback = input()

nights_stayed = days_stayed - 1
total_price = 0

if room_type == 'room for one person':
    total_price = nights_stayed * 18.00
elif room_type == 'apartment':
    total_price = nights_stayed * 25.00
    if days_stayed < 10:
        total_price *= 0.70
    elif 10 <= days_stayed <= 15:
        total_price *= 0.65
    elif days_stayed > 15:
        total_price *= 0.50
elif room_type == 'president apartment':
    total_price = nights_stayed * 35.00
    if days_stayed < 10:
        total_price *= 0.90
    elif 10 <= days_stayed <= 15:
        total_price *= 0.85
    elif days_stayed > 15:
        total_price *= 0.80

if feedback == 'positive':
    total_price += total_price * 0.25
else:
    total_price *= 0.90

print(f'{total_price:.2f}')
