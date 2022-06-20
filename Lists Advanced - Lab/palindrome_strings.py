input_line = input().split()
searched_palindrome = input()
palindromes = list()

for word in input_line:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_palindrome)} times")