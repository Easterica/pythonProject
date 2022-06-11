list_of_numbers = list(map(float, input().split()))


def round_numbers(numbers):
    rounded_numbers = list()

    for number in numbers:
        rounded_numbers.append(round(number))
    return rounded_numbers


print(round_numbers(list_of_numbers))
