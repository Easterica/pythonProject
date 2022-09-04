import re

command = input()
pattern = r'>>([A-Za-z]+)<<(\d+[\.]*\d+)!(\d+)'
total_cost = 0
bought_furniture = []
while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        bought_furniture.append(matches.group(1))
        total_cost +=  (matches.group(2)) * int(matches.group(3))


    command = input()
print("Bought furniture:")
for item in bought_furniture:
    print(item)
print(f"Total money spend: {total_cost}")