to_do_list = [0] * 10

while True:

    command = input()
    if command == "End":
        break
    else:
        command = command.split("-")

    index = int(command[0])
    task = command[1]
    to_do_list.insert(index, task)
result = [task for task in to_do_list if task != 0]
print(result)