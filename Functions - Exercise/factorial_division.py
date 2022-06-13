def factorial_division(num1, num2):
    num1_factorial = 1
    num2_factorial = 1

    for i in range(1, num1 + 1):
        num1_factorial *= i

    for k in range(1, num2 + 1):
        num2_factorial *= k

    result = num1_factorial / num2_factorial

    return f"{result:.2f}"


number1 = int(input())
number2 = int(input())

print(factorial_division(number1,number2))