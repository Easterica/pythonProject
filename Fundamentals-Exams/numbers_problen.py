
list_of_nums = list(map(int, input().split()))

avg_num = sum(list_of_nums) / len(list_of_nums)

top_5_above_average = []

while len(top_5_above_average) < 5 and any([num for num in list_of_nums if num > avg_num]):
    max_num = max(list_of_nums)
    if max_num > avg_num:
        top_5_above_average.append(max_num)
        list_of_nums.remove(max_num)
    elif max_num >= avg_num and len(top_5_above_average) == 0:
        print("No")
        exit()




print(" ".join(list(map(str,sorted(top_5_above_average, reverse=True)))))
