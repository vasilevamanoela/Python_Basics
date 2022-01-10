searched_book = input()
book = input()
counter = 0
is_found = False

while book != 'No More Books':
    if book == searched_book:
        is_found = True
        break

    counter += 1
    book = input()

if is_found:
    print(f"You checked {counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {counter} books.")

