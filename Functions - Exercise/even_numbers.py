numbers = list(map(int, input().split()))

even_numbers_func = lambda a: a % 2 == 0
list_of_even = list()
even_numbers = list(filter(even_numbers_func, numbers))

print(even_numbers)