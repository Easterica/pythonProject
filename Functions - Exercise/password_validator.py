def password_is_valid(password : str):
    is_valid = True
    list_of_statements = list()
    digit_counter = 0
    if len(password) < 6 or len(password) >= 10:
        list_of_statements.append("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        list_of_statements.append("Password must consist only of letters and digits")
        is_valid = False
    for char in password:
        if char.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        list_of_statements.append("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        list_of_statements.append("Password is valid")

    return list_of_statements


password_input = input()
list_of_statements = password_is_valid(password_input)
for statement in list_of_statements:
    print(statement)
