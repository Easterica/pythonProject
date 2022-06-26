city_count = int(input())
total_profit = 0
counter_of_cities = 0
for i in range(city_count):
    curr_profit = 0
    name_of_the_city = input()
    income = float(input())
    expenses = float(input())
    counter_of_cities += 1
    if counter_of_cities % 3 == 0 and not counter_of_cities % 5 == 0:
        expenses = 1.5 * expenses

    if counter_of_cities % 5 == 0:
        income = 0.9 * income
    curr_profit = income - expenses
    total_profit += curr_profit

    print(f"In {name_of_the_city} Burger Bus earned {curr_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")
