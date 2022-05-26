change = float(input())
coins = 0

change_cents = round(change * 100)

while change_cents > 0:
    if change_cents >= 200:
        change_cents -= 200
        coins += 1
    elif change_cents >= 100:
        change_cents -= 100
        coins += 1
    elif change_cents >= 50:
        change_cents -= 50
        coins += 1
    elif change_cents >= 20:
        change_cents -= 20
        coins += 1
    elif change_cents >= 10:
        change_cents -= 10
        coins += 1
    elif change_cents >= 5:
        change_cents -= 5
        coins += 1
    elif change_cents >= 2:
        change_cents -= 2
        coins += 1
    elif change_cents >= 1:
        change_cents -= 1
        coins += 1

print(coins)
