speed = float(input())

if speed <= 10:
    print('slow')
elif (speed > 10) & (speed <= 50):
    print('average')
elif (speed > 50) & (speed <= 150):
    print('fast')
elif (speed > 150) & (speed <= 1000):
    print('ultra fast')
else:
    print('extremely fast')
