budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = 1.25 * flour_price
milk_counter = 0
current_bread_count = 0
eggs_count = 0

while True:
    milk_counter += 1
    if milk_counter % 4 == 0 or milk_counter == 1:
        budget -= milk_price
    loaf_price = flour_price + eggs_price
    budget -= loaf_price
    current_bread_count += 1

    if current_bread_count % 3 == 0:
