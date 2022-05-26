command = input()
coffee_needed = 0

while command != "END":
    if command.islower():
        if command == "coding":
            coffee_needed += 1
        elif command == "dog" or command == "cat":
            coffee_needed += 1
        elif command == "movie":
            coffee_needed += 1
    elif command.isupper():
        if command == "CODING":
            coffee_needed += 2
        elif command == "DOG" or command == "CAT":
            coffee_needed += 2
        elif command == "MOVIE":
            coffee_needed += 2

    command = input()
if coffee_needed > 5:
    print("You need extra sleep")
else:
    print(coffee_needed)