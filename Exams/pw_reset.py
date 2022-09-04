string_input = input()
command = input()
new_password = ''
while True:

    if command == "Done":
        print(f"Your password is: {new_password}")
        break
    else:
        command = command.split()

    if command[0] == "TakeOdd":
        # for i in range(1,len(string_input),2):
        #     new_password += string_input[i]
        new_password = "".join([new_password[i] for i in range(1, len(new_password) + 1) if i % 2 != 0])
        print(new_password)
    elif command[0] == "Cut":
        index = int(command[1])
        length = int(command[2])
        new_password = "".join([new_password[i] for i in range(len(new_password)) if i < index or i >= index + length])
        print(new_password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in new_password:
            new_password = new_password.replace(substring, substitute)
            print(new_password)
        else:
            print("Nothing to replace!")


    command = input()
