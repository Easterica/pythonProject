list_of_targets = list(map(int, input().split()))

while True:

    command = input()
    if command == "End":
        print("|".join([str(num) for num in list_of_targets]))
        break
    else:
        command = command.split()

    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])

        if index < len(list_of_targets):
            list_of_targets[index] -= power
            if list_of_targets[index] <= 0:
                list_of_targets.pop(index)
    elif command[0] == "Add":
        index = int(command[1])
        value = int(command[2])

        if index <= len(list_of_targets) - 1:
            list_of_targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        index = int(command[1])
        radius = int(command[2])

        valid_index = index - radius >= 0 and index + radius < len(list_of_targets)
        if valid_index:
            start_index = index - radius
            final_index = index + radius
            list_of_targets = [list_of_targets[i] for i in range(len(list_of_targets)) if i < start_index or i > final_index]

        else:
            print("Strike missed!")
            print("|".join([str(num) for num in list_of_targets]))
            break

