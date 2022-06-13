def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(num1, num2):
    return num1 - num2


def add_and_subtract(num1, num2, num3):
    curr_result = sum_numbers(num1, num2)
    final_result = subtract_numbers(curr_result, num3)

    return final_result


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = add_and_subtract(first_num,second_num,third_num)
print(result)