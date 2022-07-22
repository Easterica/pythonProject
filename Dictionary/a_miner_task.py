resources = dict()

while True:

    type = input()
    if type == "stop":
        break
    quantity = int(input())
    if type not in resources.keys():
        resources[type] = 0

    resources[type] += quantity


for key, value in resources.items():
    print(f"{key} -> {value}")


