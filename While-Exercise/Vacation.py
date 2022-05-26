trip_money = float(input())
available_money = float(input())

spend_days = 0
days = 0

while available_money < trip_money:
    if spend_days == 5:
        print("You can't save the money.")
        print(days)
        break

    action = input()
    money = float(input())



    if action == "spend":
        available_money -= money
        if available_money < 0:
            available_money = 0
        spend_days += 1
        days += 1
    elif action == "save":
        available_money += money
        spend_days = 0
        days += 1

if available_money >= trip_money:
    print(f"You saved the money for {days} days.")
