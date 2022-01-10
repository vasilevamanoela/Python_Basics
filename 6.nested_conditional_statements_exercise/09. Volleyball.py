import math

year_type = input()
number_holidays = int(input())
number_weekends_traveling = int(input())

number_weekends_Sofia = 48 - number_weekends_traveling
saturday_games_Sofia = number_weekends_Sofia * 3/4
number_holiday_games = number_holidays * 2/3

total_number_games = saturday_games_Sofia + number_weekends_traveling + number_holiday_games

if year_type == 'leap':
    total_number_games += total_number_games * 0.15

print(math.floor(total_number_games))
