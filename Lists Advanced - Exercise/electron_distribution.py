import math

electrons = int(input())

electron_distribution = list()

counter_of_cells = 1


while electrons > 0:
    current_value_of_cell = int(2 * math.pow(counter_of_cells, 2))
    if electrons >= current_value_of_cell:
        electron_distribution.append(current_value_of_cell)
        electrons -= current_value_of_cell
        counter_of_cells += 1
    else:
        electron_distribution.append(electrons)

print(electron_distribution)