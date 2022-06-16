input_line = input()
price_without_taxes = 0
taxes = 0
total_price = 0

while input_line != "special" and input_line != "regular":
    price_of_component = float(input_line)
    if price_of_component < 0:
        print("Invalid price!")
        input_line = input()
        continue
    else:
        price_without_taxes += price_of_component
        taxes += 0.2 * price_of_component
    input_line = input()
total_price = taxes + price_without_taxes

if input_line == "special":
    total_price *= 0.9

if total_price <= 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
