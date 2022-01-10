number = float(input())
input_metric = input()
output_metric = input()

result = 0

if (input_metric == 'm') & (output_metric == 'cm'):
    result = number * 100
elif(input_metric == 'm') & (output_metric == 'mm'):
    result = number * 1000
elif (input_metric == 'mm') & (output_metric == 'm'):
    result = number / 1000
elif (input_metric == 'mm') & (output_metric == 'cm'):
    result = number * 0.1
elif (input_metric == 'cm') & (output_metric == 'm'):
    result = number * 0.01
elif (input_metric == 'cm') & (output_metric == 'mm'):
    result = number * 10

print(f'{result:.3f}')
