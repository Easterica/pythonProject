list_of_input = list(map(int, input().split(',')))
upper_boundary = 10
lower_boundary = 0
copy_of_input_list = list_of_input.copy()
new_list = []
new_list1 = []

max_num = max(list_of_input)
boundary = max_num // 10
if max_num > boundary * 10:
    boundary += 1

while list_of_input:
    new_list1 = []

    for num in copy_of_input_list:
        if boundary * 10 - 10 < num <= boundary * 10:
            new_list1.append(num)
            list_of_input.remove(num)
        if not list_of_input:
            break

    new_list.append(f"Group of {boundary * 10}'s: {new_list1}")
    boundary -= 1

print("\n".join((new_list)[::-1]))

