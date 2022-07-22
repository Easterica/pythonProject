command = input()
users = {}

while True:

    if command == "End":
        break
    else:
        command = command.split(" -> ")

    company = command[0]
    id = command[1]

    if company in users.keys():
        if id not in users[company]:
            users[company].append(id)
    else:
        users[company] = [id]


    command = input()

for company in users.keys():
    print(f"{company}")
    for id in users[company]:
        print(f"-- {id}")
