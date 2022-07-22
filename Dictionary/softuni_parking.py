database = dict()

count = int(input())

for _ in range(0, count):
    command = input().split()
    name = command[1]


    if command[0] == "register":
        plate = command[2]
        if name not in database:
            database[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {database[name]}")
    elif command[0] == "unregister":
        if name not in database:
            print(f"ERROR: user {name} not found")
        else:
            database[name] = 0
            print(f"{name} unregistered successfully")

for name, plate in database.items():
    if plate != 0:
        print(f"{name} => {plate}")
