line_of_input = input().split("->")
final_budget = float(input())

list_of_clothes = " ".join(line_of_input).split("|")
list_of_clothes1 = " ".join(list_of_clothes).split()
clothes_sold = list()
starting_budget = final_budget
new_prices = list()

for i in range(0, len(list_of_clothes1), 2):
    type_of_clothing = list_of_clothes1[i]
    clothing_price = float(list_of_clothes1[i + 1])

    if type_of_clothing == "Clothes":
        if clothing_price <= 50 and final_budget > clothing_price:
            final_budget -= clothing_price
            clothes_sold.append(clothing_price)
        else:
            continue
    elif type_of_clothing == "Shoes":
        if clothing_price <= 35 and final_budget > clothing_price:
            final_budget -= clothing_price
            clothes_sold.append(clothing_price)
        else:
            continue
    elif type_of_clothing == "Accessories":
        if clothing_price <= 20.50 and final_budget > clothing_price:
            final_budget -= clothing_price
            clothes_sold.append(clothing_price)
        else:
            continue

for i in range(len(clothes_sold)):
    clothes_sold[i] *= 1.4
    new_prices.append(clothes_sold[i])
    final_budget += clothes_sold[i]
profit = final_budget - starting_budget

for i in range(len(new_prices)):
    print(f"{new_prices[i]:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")

if final_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")


