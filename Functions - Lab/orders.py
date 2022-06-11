type_of_product = input()
quantity = int(input())


def calculate_order(type_of_the_product, count):
    price = 0
    if type_of_the_product == "coffee":
        price = 1.50
    elif type_of_the_product == "water":
        price = 1.00
    elif type_of_the_product == "coke":
        price = 1.40
    elif type_of_the_product == "snacks":
        price = 2
    return f"{price * count:.2f}"


print(calculate_order(type_of_product, quantity))