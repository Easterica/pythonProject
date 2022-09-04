import re

count_of_lines = int(input())

for _ in range(count_of_lines):
    data = input()
    pattern = r"@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}"
    result = re.match(pattern, data)

    if not result:
        print("Invalid barcode")
    else:
        pass