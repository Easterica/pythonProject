num_of_lines = int(input())
keyword = input()

first_list = list()
filtered_list = list()

for _ in range(num_of_lines):
    line_of_input = input()
    first_list.append(line_of_input)

    if keyword in line_of_input:
        filtered_list.append(line_of_input)

print(first_list)
print(filtered_list)