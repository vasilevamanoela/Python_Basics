start = int(input())
end = int(input())

first_start = start // 1000
second_start = (start // 100) % 10
third_start = (start // 10) % 10
fourth_start = start % 10

first_end = end // 1000
second_end = (end // 100) % 10
third_end = (end // 10) % 10
fourth_end = end % 10

for n1 in range(first_start, first_end + 1):
    for n2 in range(second_start, second_end + 1):
        for n3 in range(third_start, third_end + 1):
            for n4 in range(fourth_start, fourth_end + 1):
                if n1 % 2 == 1 and n2 % 2 == 1 and n3 % 2 == 1 and n4 % 2 == 1:
                    print(f'{n1}{n2}{n3}{n4}', end=' ')
