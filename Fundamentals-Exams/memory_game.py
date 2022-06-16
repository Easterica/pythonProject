list_of_input = input().split()
moves = 0
while True:
    command = input().split()

    if command[0] == "end" and len(list_of_input) > 0:
        print("Sorry you lose :(")
        print(" ".join(list_of_input))
        break
    if len(list_of_input) == 0:
        print(f"You have won in {moves} turns!")
        break
    index1 = int(command[0])
    index2 = int(command[1])
    if list_of_input[index2] == list_of_input[index1]:
        print(f"Congrats! You have found matching elements - {list_of_input[index2]}!")
        curr_num = list_of_input[index2]
        list_of_input.remove(curr_num)
        list_of_input.remove(curr_num)
        moves += 1
    elif index1 < 0 or index2 < 0:
        moves += 1
        print("Invalid input! Adding additional elements to the board")
        middle = len(list_of_input) // 2
        list_of_input.insert(middle, f"-{moves}a")
        list_of_input.insert(middle, f"-{moves}a")

    elif list_of_input[index2] != list_of_input[index1]:
        print("Try again!")
        moves += 1



