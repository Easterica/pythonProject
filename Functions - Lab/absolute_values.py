seq_of_numbers = list(map(float, input().split()))

abs_numbers = list()

for number in seq_of_numbers:
    abs_numbers.append(abs(number))

print(abs_numbers)