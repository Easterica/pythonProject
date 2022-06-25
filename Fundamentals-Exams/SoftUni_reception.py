worker1 = int(input())
worker2 = int(input())
worker3 = int(input())

questions = int(input())

hours = 0

while questions >= 0:
    if hours % 4 == 0 and hours != 0:
        hours += 1
    elif questions != 0:
        questions -= worker1 + worker2 + worker3
        hours += 1
    elif questions == 0:
        break


print(f"Time needed: {hours}h.")

