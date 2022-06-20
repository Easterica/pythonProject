number_list = list(map(int, input().split(", ")))

indices = list()
for num in number_list:
    if num % 2 == 0:
        index = number_list.index(num)
        indices.append(index)

print(indices)