string_input = input()

command = input()

while True:

    if command == "Done":
        break
    else:
        command = command.split()

    curr_command = command[0]
    if curr_command == "Change":
        char_to_replace = command[1]
        replacement = command[2]
        while char_to_replace in string_input:
            string_input = string_input.replace(char_to_replace, replacement)
        print(string_input)
    elif curr_command == "Includes":
        substring = command[1]
        if substring in string_input:
            print(True)
        else:
            print(False)
    elif curr_command == "End":
        substring = command[1]
        if string_input.endswith(substring):
            print(True)
        else:
            print(False)
    elif curr_command == "Uppercase":
        string_input = string_input.upper()
        print(string_input)
    elif curr_command == "FindIndex":
        char_to_find = command[1]
        index = string_input.index(char_to_find)
        print(index)
    elif curr_command == "Cut":
        start_index = int(command[1])
        count = int(command[2])
        string_input = string_input[start_index:start_index+count]
        print(string_input)
    command = input()
