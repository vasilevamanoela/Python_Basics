volume_pool = int(input())
debit_first_pipe_hour = int(input())
debit_second_pipe_hour = int(input())
hours_away = float(input())

volume_first_pipe = hours_away * debit_first_pipe_hour
volume_second_pipe = hours_away * debit_second_pipe_hour

total_volume_pipes = volume_first_pipe + volume_second_pipe
percent_first_pipe = volume_first_pipe / total_volume_pipes * 100
percent_second_pipe = volume_second_pipe / total_volume_pipes * 100
percent_total = total_volume_pipes / volume_pool * 100

if volume_pool >= total_volume_pipes:
    print(f"The pool is {percent_total:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.")
else:
    print(f"For {hours_away} hours the pool overflows with {(total_volume_pipes - volume_pool):.2f} liters.")
