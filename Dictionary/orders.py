products = dict()

command = input()

while True:

    if command == "buy":
        break
    else:
        command = command.split()

    product = command[0]
    price = command[1]
    quantity = int(command[2])

    if product not in products:
        products[product] = [quantity, price]
    else:
        if products[product][1] != price:
            products[product][1] = price
            products[product][0] += quantity

    command = input()

for key, value in products.items():
    print(f"{key} -> {(float(value[0]) * float(value[1])):.2f}")