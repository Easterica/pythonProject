command = input()
phonebook = dict()

while True:

    if command.isdigit():
        break
    else:
        command = command.split("-")

    name = command[0]
    phone = command[1]
    if name not in phonebook.keys():
        phonebook[name] = 0
    phonebook[name] = phone
    command = input()

for _ in range(int(command)):
    searched_name = input()
    if searched_name in phonebook.keys():
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")



