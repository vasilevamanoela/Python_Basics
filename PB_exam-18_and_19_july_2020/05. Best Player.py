import sys

name_player = input()
best_player = ""
best_player_goals = -sys.maxsize

while name_player != 'END':
    number_goals = int(input())
    if number_goals > best_player_goals:
        best_player = name_player
        best_player_goals = number_goals

    if number_goals >= 10:
        break

    name_player = input()

print(f"{best_player} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
