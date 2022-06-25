list_of_nums = list(map(int, input().split()))

while True:
    command = input()

    if command == "end":
        break
    else:
        command = command.split()

    curr_command = command[0]

    for i in range(len(list_of_nums)):
        if curr_command == "swap":
            index1 = int(command[1])
            index2 = int(command[2])

            tmp = list_of_nums[index1]
            list_of_nums[index1] = list_of_nums[index2]
            list_of_nums[index2] = tmp
            break
        elif curr_command == "multiply":
            index1 = int(command[1])
            index2 = int(command[2])

            list_of_nums[index1] *= list_of_nums[index2]
            break
        elif curr_command == "decrease":
            list_of_nums[i] -= 1

print(", ".join(list(map(str, list_of_nums))))
