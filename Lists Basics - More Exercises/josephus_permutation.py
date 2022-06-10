list_of_numbers = list(map(int, input().split()))
number_k = int(input())

executed = list()

while len(list_of_numbers) > 0:
    for index in range(number_k - 1, len(list_of_numbers) + 1, number_k - 1):
        if index > len(list_of_numbers):
            break
        if number_k > len(list_of_numbers):
            index = (number_k % len(list_of_numbers)) - 1
        current_execution = list_of_numbers.pop(index)
        executed.append(current_execution)

print(executed)