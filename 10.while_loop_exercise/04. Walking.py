goal_steps = 10000
total_steps = 0

while total_steps < goal_steps:
    inpt = input()
    if inpt == 'Going home':
        steps_to_home = int(input())
        total_steps += steps_to_home
        break

    steps_during_day = int(inpt)
    total_steps += steps_during_day

difference = abs(total_steps - goal_steps)

if total_steps >= goal_steps:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f'{difference} more steps to reach goal.')
