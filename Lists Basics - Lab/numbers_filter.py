num_of_lines = int(input())

unfiltered_list = list()
filtered_list = list()

for _ in range(num_of_lines):
    current_num = int(input())
    unfiltered_list.append(current_num)

command = input()

for i in range(len(unfiltered_list)):
    if command == "even" and unfiltered_list[i] % 2 == 0:
        filtered_list.append(unfiltered_list[i])
    elif command == "odd" and unfiltered_list[i] % 2 != 0:
        filtered_list.append(unfiltered_list[i])
    elif command == "negative" and unfiltered_list[i] < 0:
        filtered_list.append(unfiltered_list[i])
    elif command == "positive" and unfiltered_list[i] >= 0:
        filtered_list.append(unfiltered_list[i])

print(filtered_list)
