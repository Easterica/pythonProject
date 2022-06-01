lines = int(input())
parentheses_counter = 0
is_balanced = False

for i in range(lines):
    str_input = input()

    if str_input == "(":
        parentheses_counter += 1
        continue
    if str_input == ")" and parentheses_counter == 1:
        is_balanced = True
        parentheses_counter = 0

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")

#
#     if str_input == "(" or str_input == ")":
#         parentheses_counter += 1
#     else:
#         continue
#
# if parentheses_counter % 2 == 0:
#     print("BALANCED")
# else:
#     print("UNBALANCED")

