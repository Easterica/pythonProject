list_of_ints = input().split(", ")
count_of_beggars = int(input())
list_of_sum = list()
counter_of_beggars = 0
for i in range(count_of_beggars):
    list_of_sum.append(0)
    for j in range(counter_of_beggars, len(list_of_ints), count_of_beggars):
        curr_num = int(list_of_ints[j])
        list_of_sum[i] += curr_num
    counter_of_beggars += 1


print(list_of_sum)
