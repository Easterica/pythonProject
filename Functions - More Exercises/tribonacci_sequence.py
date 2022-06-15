def tribonacci_seq(number):
    list_of_numbers = list()

    for num in range(number):
        if len(list_of_numbers) == 0:
            list_of_numbers.append(1)
        elif len(list_of_numbers) == 1:
            list_of_numbers.append(1)
        elif len(list_of_numbers) == 2:
            list_of_numbers.append(2)
        else:
            tribonacci_num = list_of_numbers[num - 1] + list_of_numbers[num - 2] + list_of_numbers[num - 3]
            list_of_numbers.append(tribonacci_num)
    return list_of_numbers

number = int(input())
list_of_numbers = tribonacci_seq(number)
print(" ".join(list(map(str, list_of_numbers))))
