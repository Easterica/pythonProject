list_of_input = input().split()
opposites = list()

for i in range(len(list_of_input)):
    curr_num = int(list_of_input[i])
    opposite_num = curr_num * -1
    opposites.append(opposite_num)

print(opposites)