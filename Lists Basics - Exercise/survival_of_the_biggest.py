list_of_input = input().split()
count_of_num_to_remove = int(input())

min_num = 0

for _ in range(count_of_num_to_remove):
    for i in range(len(list_of_input)):
        curr_num = int(list_of_input[i])
        if i == 0:
            min_num = curr_num
            continue
        if curr_num < min_num:
            min_num = curr_num
    list_of_input.remove(str(min_num))

print(", ".join(list_of_input))