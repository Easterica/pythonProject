list_of_presents = input().split()

command = input()

while command != "No Money":

    command = command.split()
    for i in range(len(list_of_presents)):
        if list_of_presents[i] == command[1] and command[0] == "OutOfStock":
            index = list_of_presents.index(command[1])
            list_of_presents.pop(index)
            list_of_presents.insert(index, "None")
            continue
        elif command[0] == "Required":
            index = int(command[2])
            if index < len(list_of_presents):
                list_of_presents.pop(index)
                list_of_presents.insert(index, command[1])
                break
        elif command[0] == "JustInCase":
            list_of_presents.pop()
            list_of_presents.append(command[1])
            break

    command = input()

for i in range(len(list_of_presents)):
    if list_of_presents[i] != "None":
        print(f"{list_of_presents[i]}", end=" ")