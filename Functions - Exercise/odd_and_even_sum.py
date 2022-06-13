def odd_and_even(number):
    odd_nums = list()
    even_nums = list()

    for digit in number:
        if int(digit) % 2 == 0:
            even_nums.append(int(digit))
        else:
            odd_nums.append(int(digit))

    sum_odd_nums = sum(odd_nums)
    sum_even_nums = sum(even_nums)
    result = f"Odd sum = {sum_odd_nums}, Even sum = {sum_even_nums}"
    return result


number = input()
print(odd_and_even(number))