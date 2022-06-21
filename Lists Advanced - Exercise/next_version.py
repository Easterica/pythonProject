list_of_nums = list(map(int, input().split('.')))

list_of_nums[-1] += 1
for i in range(len(list_of_nums) - 1, -1, -1):
    if list_of_nums[i] > 9:
        list_of_nums[i] = 0
        list_of_nums[i - 1] += 1

print(".".join([str(num) for num in list_of_nums]))
