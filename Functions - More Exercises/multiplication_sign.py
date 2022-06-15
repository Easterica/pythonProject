def multiplication_sign(list_of_numbers):
    is_zero = False
    is_negative = False
    for num in list_of_numbers:
        if num == 0:
            is_zero = True
        elif num < 0:
            is_negative = True
    if is_zero:
        return "zero"
    elif is_negative:
        return "negative"
    else:
        return "positive"


first_num = int(input())
second_num = int(input())
third_num = int(input())

list_of_nums = list()
list_of_nums.append(first_num)
list_of_nums.append(second_num)
list_of_nums.append(third_num)
print(multiplication_sign(list_of_nums))