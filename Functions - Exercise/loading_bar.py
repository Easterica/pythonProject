def loading_bar(percent):
    percent_count = percent // 10
    dot_count = 10 - percent_count
    result = list()

    for i in range(percent_count):
        result.append("%")
    for j in range(dot_count):
        result.append(".")
    if percent != 100:
        print(f"{percent}% [", end="")
        for char in result:
            print(char, end="")
        print("]")
        return "Still loading..."
    else:
        return "100% Complete!"



percent = int(input())
print(loading_bar(percent))
if percent == 100:
    print("[%%%%%%%%%%]")

