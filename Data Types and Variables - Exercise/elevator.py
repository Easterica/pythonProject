import math

number_of_people = int(input())
capacity = int(input())
courses = 0

courses = math.ceil(number_of_people / capacity)
print(courses)