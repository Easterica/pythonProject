list_of_strings = input().split()
input_string = input()
output = ''
index = 0
word = list()

for i in range(len(list_of_strings)):
    curr_num = list_of_strings[i]
    for j in range(len(curr_num)):
        index += int(curr_num[j])
    if index > len(input_string):
        index = index % len(input_string)

    word.append(input_string[index])
    input_string = input_string.replace(input_string[index], "", 1)
    index = 0

print("".join(word))