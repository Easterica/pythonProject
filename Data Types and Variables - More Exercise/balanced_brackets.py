lines = int(input())
parentheses_counter = 0

for i in range(lines):
    str_input = input()

    if str_input == "(" or str_input == ")":
        parentheses_counter += 1
    else:
        continue

if parentheses_counter % 2 == 0:
    print("BALANCED")
else:
    print("UNBALANCED")
