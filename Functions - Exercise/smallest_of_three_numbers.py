def smallest_of_three(num1, num2, num3):
    list_of_nums = list()
    list_of_nums.append(num1)
    list_of_nums.append(num2)
    list_of_nums.append(num3)

    min_number = min(list_of_nums)
    return min_number


first_num = int(input())
second_num = int(input())
third_num = int(input())

min_number = smallest_of_three(first_num, second_num,third_num)

print(min_number)