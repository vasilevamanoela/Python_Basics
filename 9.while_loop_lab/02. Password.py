name = input()
password = input()

while True:
    password_guess = input()

    if password_guess == password:
        print(f'Welcome {name}!')
        break
