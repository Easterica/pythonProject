# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1


input_list = input().split()
output = []

while True:
    command = input()
    if command == "3:1":
        break
    command = command.split()

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index < 0:
            start_index = 0
            input_list[start_index:end_index+1] = ["".join(input_list[start_index:end_index+1])]
    elif command[1] == "divide":
        index = int(command[1])
        partitions = int(command[2])
        to_be_divided = input_list[index]

        input_list.pop(index)
        pieces = len(to_be_divided) // partitions




    print(input_list)

