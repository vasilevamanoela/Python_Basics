number_open_taps = int(input())
salary = int(input())

for i in range(number_open_taps):
    web_site = input()
    if web_site == 'Facebook':
        salary -= 150
    elif web_site == 'Instagram':
        salary -= 100
    elif web_site == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
