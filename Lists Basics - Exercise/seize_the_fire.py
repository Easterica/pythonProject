# Type of Fire	Range
# High	81 - 125
# Medium	51 - 80
# Low	1 - 50

fire_cells = input().split("#")
water = int(input())
effort = 0
put_out_cells = list()
total_fire = 0

list_of_fires = " ".join(fire_cells).split()
counter = 0
while counter < len(fire_cells):
    list_of_fires.remove("=")
    counter += 1

for i in range(0, len(list_of_fires), 2):
    type_of_fire = list_of_fires[i]
    value_of_cell = int(list_of_fires[i + 1])
    if type_of_fire == "High":
        if 81 <= value_of_cell <= 125:
            if value_of_cell > water:
                continue
            else:
                water -= value_of_cell
                put_out_cells.append(value_of_cell)
                effort += 0.25 * value_of_cell
        else:
            continue
    elif type_of_fire == "Medium":
        if 51 <= value_of_cell <= 80:
            if value_of_cell > water:
                continue
            else:
                water -= value_of_cell
                put_out_cells.append(value_of_cell)
                effort += 0.25 * value_of_cell
        else:
            continue
    elif type_of_fire == "Low":
        if 1 <= value_of_cell <= 50:
            if value_of_cell > water:
                continue
            else:
                water -= value_of_cell
                put_out_cells.append(value_of_cell)
                effort += 0.25 * value_of_cell
        else:
            continue

print("Cells:")
for i in range(len(put_out_cells)):
    print(f" - {put_out_cells[i]}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")



