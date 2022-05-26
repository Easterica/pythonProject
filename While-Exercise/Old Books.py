searched_book = input()
books_count = 0
input_line = input()

while input_line != "No More Books":
    if input_line == searched_book:
        print(f"You checked {books_count} books and found it.")
        exit()
    else:
        books_count += 1

    input_line = input()
print("The book you search is not here!")
print(f"You checked {books_count} books.")