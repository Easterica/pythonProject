# Ivo Johny Tony Bony Mony
# merge 0 3
# merge 3 4
# merge 0 3
# 3:1


input_list = input().split()
merged_items = ""
output = []

while True:
    command = input()
    copy_of_input = input_list.copy()
    if command == "3:1":
        break
    command = command.split()

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])
        merged_items = input_list[start_index:end_index+1]
        merged_items = "".join(merged_items)

    print(input_list)

