def is_perfect_number(number):
    list_of_divisors = list()
    for i in range(1,number):
        if number % i == 0:
            list_of_divisors.append(i)
    result = sum(list_of_divisors)
    return result

magic_number = int(input())

if magic_number == is_perfect_number(magic_number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
