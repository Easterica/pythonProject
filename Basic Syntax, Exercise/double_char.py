input_line = input()
new_string = ''

while input_line != "End":

    new_string = ''
    if input_line == "SoftUni":
        input_line = input()
        continue
    for i in range(len(input_line)):
        new_string += input_line[i] + input_line[i]
    input_line = input()

    print(new_string)

