sum_to_be_collected = int(input())

price = input()
transaction_num = 0
cash_sum = 0
card_sum = 0
products_cash = 0
products_card = 0
whole_sum = 0

while price != "End":
    if whole_sum >= sum_to_be_collected:
        break
    price = int(price)
    transaction_num += 1



