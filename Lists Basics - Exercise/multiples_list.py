factor = int(input())
count = int(input())

multiplier = 1
list_of_ints = list()

for i in range(count):
    list_of_ints.append(multiplier * factor)
    multiplier += 1

print(list_of_ints)