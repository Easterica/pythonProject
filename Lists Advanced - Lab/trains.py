wagons_count = int(input())
train = [0] * wagons_count
while True:
    command = input()

    if command == "End":
        break
    else:
        command = command.split()


    type_of_command = command[0]

    if type_of_command == "add":
        number_of_people = int(command[1])
        train[-1] += number_of_people
    elif type_of_command == "insert":
        index = int(command[1])
        number_of_people = int(command[2])
        train[index] += number_of_people
    elif type_of_command == "leave":
        index = int(command[1])
        number_of_people = int(command[2])
        train[index] -= number_of_people

print(train)