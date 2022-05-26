length = int(input())
width = int(input())

cake = length * width
pieces = input()

while pieces != "STOP":
    pieces = int(pieces)

    cake -= pieces
    if cake <= 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        exit()

    pieces = input()
if cake > 0:
    print(f"{cake} pieces are left.")