days = int(input())
total_win_games = 0
total_lose_games = 0
total_money = 0

for day in range(days):
    game = input()
    win_games_per_day = 0
    lose_games_per_day = 0
    money = 0
    while game != 'Finish':
        game_result = input()

        if game_result == 'win':
            win_games_per_day += 1
            money += 20
        elif game_result == 'lose':
            lose_games_per_day += 1

        game = input()

    if win_games_per_day > lose_games_per_day:
        money *= 1.1

    total_win_games += win_games_per_day
    total_lose_games += lose_games_per_day
    total_money += money

if total_win_games > total_lose_games:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
