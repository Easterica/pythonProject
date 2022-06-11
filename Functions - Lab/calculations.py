operator = input()
num1 = int(input())
num2 = int(input())


def calculate(operation, number_1, number_2):
    if operation == "multiply":
        return number_1 * number_2
    elif operation == "divide":
        return int(number_1 / number_2)
    elif operation == "add":
        return number_1 + number_2
    elif operation == "subtract":
        return number_1 - number_2


print(calculate(operator, num1, num2))