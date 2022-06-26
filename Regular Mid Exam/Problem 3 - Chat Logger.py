chat_history = list()
# [x[:-1] for x in mylist]
while True:
    command = input()

    if command == "end":
        break
    else:
        command = command.split()

    curr_command = command[0]

    if curr_command == "Chat":
        message = command[1]
        chat_history.append(message)
    elif curr_command == "Delete":
        message = command[1]
        if message in chat_history:
            chat_history.remove(message)
        else:
            continue
    elif curr_command == "Edit":
        message = command[1]
        new_message = command[2]
        if message in chat_history:
            index = chat_history.index(message)
            chat_history[index] = new_message
        else:
            continue
    elif curr_command == "Pin":
        message = command[1]
        if message in chat_history:
            index = chat_history.index(message)
            chat_history.pop(index)
            chat_history.append(message)
        else:
            continue
    elif curr_command == "Spam":
        for i in range(1, len(command)):
            chat_history.append(command[i])


print("\n".join(chat_history))
