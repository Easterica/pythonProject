products = dict()

input_line = input()

while True:

    if input_line == "statistics":
        break
    else:
        input_line = input_line.split(": ")

    product = input_line[0]
    quantity = int(input_line[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity

    input_line = input()
print("Products in stock:")
[print(f"-{product}: {quantity}") for (product, quantity) in products.items()]
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")
