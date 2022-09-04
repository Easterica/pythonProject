raw_activation_key = input()

command = input()

while True:

    if command == "Generate":
        print(f"Your activation key is: {raw_activation_key}")
        break
    else:
        command = command.split('>>>')

    curr_command = command[0]
    if curr_command == "Contains":
        substring = command[1]

        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif curr_command == "Flip":
        flag = command[1].lower()
        start_index = int(command[2])
        end_index = int(command[3])

        for i in range(start_index, end_index):
            if flag == "lower":
                raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].lower() + raw_activation_key[end_index:]

            elif flag == "upper":
                raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[start_index:end_index].upper() + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif curr_command == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)
    command = input()