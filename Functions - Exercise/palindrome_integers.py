def is_palindrome(number):
    start_digit_counter = 0
    end_digit_counter = -1
    num_as_string = str(number)
    is_palindrome = False
    while start_digit_counter < len(num_as_string):
        starting_digit = num_as_string[start_digit_counter]
        ending_digit = num_as_string[end_digit_counter]
        if starting_digit != ending_digit:
            return is_palindrome
        else:
            start_digit_counter += 1
            end_digit_counter -= 1
            is_palindrome = True
    return is_palindrome


list_of_numbers = list(map(int, input().split(", ")))
list_of_answers = list()

for num in list_of_numbers:
    if is_palindrome(num):
        list_of_answers.append(True)
    else:
        list_of_answers.append(False)

for answer in list_of_answers:
    print(f"{answer}")



