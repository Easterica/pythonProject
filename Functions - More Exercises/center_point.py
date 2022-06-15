def center_point(x1, y1, x2, y2):

    if abs(x1) + abs(y1) < abs(x2) + abs(y2):
        return f"({round(x1)}, {round(y1)})"
    else:
        return f"({round(x2)}, {round(y2)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(center_point(x1, y1, x2, y2))